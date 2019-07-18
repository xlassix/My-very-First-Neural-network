<template>
    <div class="wrapper">
        <div class="navigation">
            <div class="title">
                <h3>Lorem, ipsum</h3>
            </div>
            <div class="nav-items large">
                <span class="nav-item" :class="{active:current=='food'}" @click="changeCurrent('food')" >Food</span>
                <span class="nav-item" :class="{active:current=='drinks'}" @click="changeCurrent('drinks')">Drinks</span>
                <i :class="{fullcart:cart.length>0}" class="scale fa fa-shopping-cart"></i>
                <i class="incart">{{cart.length}}</i>
            </div>
            <div class="small-screen">
                <span class="small-screen small-item"><i  :class="{fullcart:cart.length>0}" class="scale fa fa-shopping-cart"></i></span>
                <span class="small-screen small-item"><i class="fa fa-2x fa-bars dropbutton" @click="changeSlide()"></i></span>
            </div>

        </div>
        <div :class="{slidedown:slideOn,hide:!slideOn}" ref="dropdown" class="drop-down ">
            <div class="dropdown-wrapper">
                <div class="dropdown-item" :class="{active:current=='food'}" @click="changeCurrent('food')">Food</div>
                <div class="dropdown-item" :class="{active:current=='drinks'}" @click="changeCurrent('drinks')">Drinks</div>
            </div>
        </div>
        <div class="items food" v-if="current!='food'">
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
        </div>
        <div class="items drinks" v-if="current!='drinks'">
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
            <item @pupu="addToCart" :foodInfo="test"/>
        </div>
    </div>
</template>


<script>
import item from "./item.vue"
export default {
    data(){
        return{
            test:{
                imageLink:require("../assets/menu/friedrice.jpg"),
                foodName:"fried rice",
                minPrice:100,
                increament:50
            },
            cart:[],
            current:"food",
            slideOn:false
        }
    },
    methods:{
        addToCart(state){
            this.cart.push(state);
        },
        changeCurrent(arg){
            this.current=arg;
        },
        changeSlide(){
            this.slideOn=!this.slideOn;
        }
    },
    components:{
        item
    }
}
</script>

<style scoped>
.wrapper{
    position: relative;
}

.items{
    height:100vh;
    display:flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
}
.navigation{
    display: flex;
    width: 95%;
    margin-left: 3%;
    color:white;
    padding-top: 1%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between
}

.nav-items{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 30%;
    align-items: center;
    cursor: pointer;
}

.nav-item{
    text-align: center;
    border-radius: 4px;
    height: 30px;
    width: 60px;
    padding-top: 10px;
    padding-left:8px;
    padding-right: 8px; 
    font-weight: 600;
    background-color: hsla(0, 23%, 95%,.1 );
    /* box-shadow: 2px 2px 5px black; */
    transition-duration: 500ms;
}

.nav-item:active{
    color: rgb(177, 177, 177);
    transform: scale(0.95);
}

.active{
    color: hsl(0, 0%, 60%);
}
.scale{
    transform: scale(1.5);
}

.fullcart{
    color: rgb(45, 173, 90);
}
.incart{
    padding: 0;
    margin-left:-9%;
}

.dropbutton{
    cursor: pointer;
    transition-duration: 0.5s;
}


.dropbutton:active{
    transform: scale(1.1)
}

.dropdown-wrapper{
    color: white;
    text-align: center;
    text-transform: capitalize;
}

.dropdown-item{
    cursor: pointer;
    padding:5px;
    box-shadow: 2px 0.3px 5px white,2px 0.3px 5px green;
    font-weight: 500;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
}

@keyframes slidedown {
    from{
        transform: scale3d(1,0,1)
    }
    to{
        transform: scale3d(1,1,1)
    }
}

.slidedown{
    animation: slidedown 2s ease-in fowards;
}

.hide{
    display:none;
}
.small-screen{
    display:flex;
    flex-direction: row;
    align-items: center;
}

.small-item{
    padding:0 15px;
}

@media (max-width : 800px){
    .large{
        display: none;
    }
}
@media (min-width : 800px){
    .small-screen{
        display: none;
    }
}

</style>


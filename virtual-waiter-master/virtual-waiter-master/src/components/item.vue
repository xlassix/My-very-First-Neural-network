<template>
    <div id=wrapper>
       <div class="menu-item">
            <div class="content">
                <div class="image">
                    <img class="custom" :src="foodInfo.imageLink"  alt="" srcset="">
                </div>
                <div class="content-body">
                    <div class="text">
                        {{foodInfo.foodName}}
                    </div>
                    <div class="price-tag">
                        <div class="arrow">
                            <i @click="changePrice('increase')" class="arrows fa fa-arrow-circle-o-up"></i>
                            <i @click="changePrice('decrease')" class="arrows fa fa-arrow-circle-o-down"></i>
                        </div>
                        <div class="price-display">
                            {{state.currentPrice}}
                        </div>
                        <div @click="emitAddToCart()"  class="button">
                            <i class="fa fa-shopping-cart"></i>
                        </div>
                    </div>
                </div>
            </div>
       </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            name:"alex",
            state:{
                foodName:this.foodInfo.foodName,
                currentPrice:this.foodInfo.minPrice
            }
        }
    },
    props:["foodInfo"],
    methods:{
        changePrice(action){
            if(action=="increase"){
                this.state.currentPrice+=this.foodInfo.increament;
            }
            else{
                if(this.state.currentPrice==this.foodInfo.minPrice){
                    return;
                }
                this.state.currentPrice-=this.foodInfo.increament;
            }
        },
        emitAddToCart(){
            this.$emit("pupu",this.state);
        }
    }
}
</script>

<style scoped>


img.custom{
    height: 200px;
    width: 270px;
}
.menu-item{
    background-color: white;
    width: 270px;
    box-shadow: 3px 5px 10px #837c7c;
    border-radius: 5px;
}

.image{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#wrapper{
    padding: 30px;
    color:rgb(57, 57, 73);
}

.text{
    font-weight: 600;
    color: rgb(57, 57, 73);
    text-transform: capitalize;
    letter-spacing:2px;
    padding: 5px;
    text-align:center;
}
.price-tag{
    padding: 0 10px;
}
   
.arrows{
    padding:0 6px;
    transform: scale(1.5);
    cursor: pointer;
}

.arrows:active{
    transform: scale(1.6);
    color: black;
}

.button{
    text-align: left;
    display: inline-block;
}
.content-body{
    padding-bottom: 10px;
}

.price-tag{
    display: flex;
    justify-content: space-between;
    padding-top: 3px;
}

.price-display{
    border:2px solid green;
    width: 20%;
    text-align: center;
    background-color: rgba(251, 255, 0,0.65);
    font-weight: 600;
    border-radius: 4px;
}


.button{
    background-color: rgb(45, 173, 90);
    width: 30%;
    text-align: center;
    border-radius: 2px;
    padding-top: 2px;
    cursor: pointer;
    color: white;
}

.button:active{
    background-color: green;
    box-shadow: 2px 2px 2px rgb(202, 193, 193);
    color: black;
}

</style>


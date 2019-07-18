<template>
    <div class="wrapper">
        <div class="cart-container">
            <div class="dummy"></div>
            <div class="cart-items">
                <div class="cart-item">
                    <span class="name">fufu</span>
                    <span class="price">100</span>
                </div>
                <div class="cart-item">
                    <span class="name">fufu</span>
                    <span class="price">100</span>
                </div>
                <div class="cart-item">
                    <span class="name">fufu</span>
                    <span class="price">100</span>
                </div>
                .button
            </div>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>

<style scoped>
.wrapper{
    box-sizing: border-box;
    position: absolute;
    width: 100vw;
    height: 100vh;
    background-color: hsla(0, 0%, 0%, .7);
    background-blend-mode: overlay;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.cart-container{
    width: 70vw;
    background: white;
    box-shadow: 2px 2px 5px black;
    border-radius: 9px;
    padding: 50px;
}

.cart-items{
    display: flex;
    flex-direction: column;
}

.cart-item{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    border-left:1px solid black;
    border-right:1px solid black;
    border-bottom:1px solid black;
    padding: 5px
}

.dummy{
    border-bottom: 1px solid black;
}

span{
    font-weight: 600;
    color: rgb(43, 43, 63);
    text-transform: capitalize;
}
</style>

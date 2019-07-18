<template>
  <div id="app">
    <!-- <Index/> -->
    <!-- <Order/> -->
    <Cart/>
  </div>
</template>

<script>
import Index from './components/index.vue'
import Order from './components/order.vue'
import Cart from "./components/cart.vue"

export default {
  name: 'app',
  components: {
    Index,
    Order,
    Cart
  },
  data(){
    return{

    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* color: #2c3e50; */
  background-image: url("./assets/background.jpg");
  background-repeat: no-repeat;
  background-size: 220vh;
  background-attachment: fixed;
  background-position: 50% 60%;
  min-height: 100vh;
  background-color: rgba(37, 37, 37,0.35);
  background-blend-mode: darken;
}


</style>

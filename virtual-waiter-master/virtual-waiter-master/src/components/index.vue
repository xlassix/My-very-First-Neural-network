<template>
  <div class="body">
    <div class="navigation">
      <div class="title">
        <h2>Savor tech</h2>
      </div>
      <div class="items">
        <div class="large-screen">
            <div class="sub-item">Home</div>
            <div class="sub-item">Order</div>
            <div class="sub-item">Feedback</div>
        </div>
        <div class="small-screen">
          <i class="fa fa-2x fa-bars" @click="dropDown()"></i>
        </div>
      </div> 
    </div>
    
    <div ref="dropdown" class="drop-down hide">
      <div class="dropdown-wrapper">
        <div class="dropdown-item">home</div>
        <div class="dropdown-item">order</div>
        <div class="dropdown-item">feedback</div>
      </div>
    </div>

    <div class="content-wrap">
      <div class="content-body">
        <span class="greeting"><span class="flash fadeIn" ref="flash">{{flashContent}}</span> food service </span>
          <span class="button zoom-in ">
            ORDER
          </span>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      flashContent:"better",
      options:["..better","..faster","reliable"],
      dropped:false,
      initial:true
    }
  },
  mounted() {
    setInterval(()=>{
      let index=(this.options.indexOf(this.flashContent)+1)%this.options.length;
      this.$refs.flash.classList.replace("fadeIn","fadeOut");

      setTimeout(() => {
        this.flashContent=this.options[index]
        this.$refs.flash.classList.replace("fadeOut","fadeIn");
      }, 1000);
    },2000)
  },
  methods:{
    dropDown(){
      if(this.initial){
        this.$refs.dropdown.classList.remove("hide");
        this.initial=false;
      }
      if(!this.dropped){
        this.$refs.dropdown.classList.remove("slideup")
        this.$refs.dropdown.classList.add("slidedown")
      }
      else{
        this.$refs.dropdown.classList.add("slideup")
        this.$refs.dropdown.classList.remove("slidedown")
      }
      this.dropped=!this.dropped;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .navigation{
    display: flex;
    width: 100vw;
    color:white;
    padding-top: 1%;
  }

  .title{
    width: 30%;
    margin-left: 5%;
  }

  .items{
    width: 65%;
    display: flex;
    justify-content: flex-end;
    /* margin-left: 40%; */
    margin-top: 25px;
    cursor: pointer;
  }
  
  .sub-item{
    margin:0 40px;
    font-weight: bold;
  }

  .content-body{
    color: white;  
    margin-top: 10px;
  }

  .content-wrap{
    display: flex;
    justify-content: center;
    align-items: center;
    /* text-align: center; */
    width: 100vw;
    height: 100vh;
  }

  .body{
    overflow: hidden;
  }

  span.greeting{
    font-size: 2.5em;
    display: block;
    text-transform: capitalize;
  }

  .content-body{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }


  .button{
    border: green 3px solid;
    background-color: rgb(247, 176, 23);
    display: flex;
    justify-content: center;
    align-items: center;
    margin:20px;
    cursor: pointer;
    height:50px;
    width: 110px;
    border-radius: 20px;
  }

  .flash{
    display: inline-block;
    color: rgb(247, 176, 23);
    width: 140px;
  }

  .fadeIn{
      animation: fadeIn 0.5s ease-in forwards;
  }
  
  .fadeOut{
    animation: fadeOut 0.5s ease-in forwards;
  }

  .zoom-in{
    animation: zoom-in 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) infinite forwards;
  }
  
  .rotate{
    animation: rotate 1s cubic-bezier(0.6, -0.28, 0.735, 0.045) forwards;
  }

  .slidedown{
    animation: slidedown 1.5s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
    transform-origin: top;
  }
  .slideup{
    animation: slideup 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
    transform-origin: top;
  }

  @keyframes rotate {
    from{
      transform: rotate(20deg);
    }
    to{
    transform: rotate(0deg)
    }
  }
  @keyframes zoom-in {
    0%{
      transform: scale3d(1.0)
    }
    50%{
      transform: scale(1.08)
    }
    100%{
      transform: scale(1.0)
    }
  }

  @keyframes fadeOut {
    to{
      opacity:0
    }
  }

  @keyframes fadeIn {
    from{
      opacity: 0;
    }
    to{
      opacity: 1;
    }
  }

  .large-screen{
    display: flex;
  }
  @media(max-width:786px) {
    .large-screen{
      display: none;
    }
    .small-screen{
      display: flex;
    }

  }
  @media(min-width:786px) {
    .small-screen{
      display: none;
    }
    .large-screen{
      display: flex;
    }
    
    .drop-down{
      display: none;
    }
  }

  .small-screen{
    margin-right: 40px;
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
  }

  .hide{
    display: none;
  }

  @keyframes slidedown {
    from{
      transform: scale3d(1,0,1)
    }
    to{
      transform: scale3d(1,1,1)
    }
  }
  @keyframes slideup {
    from{
      transform: scale3d(1,1,1)
    }
    to{
      transform: scale3d(1,0,1)
    }
  }

  .hide{
    display: none;
  }
</style>

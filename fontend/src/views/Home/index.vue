<template>
  <div id="app">
    <myheader></myheader>
    <section style="display:flex;flex:1;">
      <div  style="min-width:201px;background:#333">
        <myleft></myleft>
      </div>
      <article style="flex:1;padding:10px;">
		<NavBar></NavBar> 
		<router-view></router-view>  
      </article>
    </section>
  </div>
 
</template>

<script>
import myheader from './components/Head.vue';
import myleft from './components/Left.vue';
import NavBar from './components/NavBar.vue';

  export default {
    components: {
      myheader,
      myleft,
	  NavBar,  
    },
    data() {
      return {

      };
    }
  };
</script>

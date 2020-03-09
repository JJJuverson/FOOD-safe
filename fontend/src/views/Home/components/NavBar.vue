<template>
	<el-tabs type="border-card" :class='{ fixedNavbar: isfixTab }'>
	    <el-row>
		    <el-button type="success" plain @click="ToShouye">首页</el-button>
		    <el-button type="success" plain @click="ToNews">热门新闻</el-button>
		    <el-button type="success" plain @click="ToBlacklist">企业黑名单</el-button>
		    <el-button type="success" plain @click="ToCases">食品安全案例</el-button>
	    </el-row>
	</el-tabs>
</template>

<script>
	export default {
		data() {
			return {
				isfixTab: false
			}
		},
		/* mounted () {	
		    window.addEventListener('scroll', this.handleTabFix, true)
		  },*/
		methods : {			
			/*handleTabFix() {
			      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
			      var offsetTop = document.querySelector('#testNavBar').offsetTop
			      scrollTop > offsetTop ? this.isfixTab = true : this.isfixTab = false
			    },   */
			ToShouye() {
				this.$router.push({ path: '/' })
			},
			ToNews() {
				this.$router.push({ path: '/news' })
			},
			ToBlacklist() {
				this.$router.push({ path: '/blacklist' })
			},
			ToCases() {
				this.$router.push({ path: '/case' })
			},
			
		},
		
		/* beforeRouteLeave (to, from, next) {
		   window.removeEventListener('scroll', this.handleTabFix, true)
		   next()
		} */
	}
</script>

<style>
	 .fixedNavbar {
	
	    position: fixed;
	    width: 100%;
	
	  }
</style>

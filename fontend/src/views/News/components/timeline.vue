<template>
	<div>
		<div class="search-2">
			<el-input placeholder="请输入内容" v-model="keywords" class="input-with-select">
				<el-button slot="append" @click="search" icon="el-icon-search"></el-button>
			</el-input>
		</div>
		
		<div class="time-line">
			  <el-timeline :reverse="reverse">
			    <el-timeline-item
			      v-for="(activity, index) in activities"
			      :key="index"
			      :timestamp="activity.timestamp">
				  <p>{{ activity.news_time }}</p>
				  <el-card class="box-card">
				      <div slot="header" class="clearfix">
				          <span>{{ activity.news_name }}</span>
				      </div>
					{{ activity.content }}
					  <div class="newsfooter">
					      <p>
					          来源:<span class="origin">{{ activity.news_source }}</span>
					      </p>
					  </div>
				  </el-card>
			    </el-timeline-item>
			  </el-timeline>
			</div>
		</div>
		
	</div>
	
</template>



<script>
export default {
    data() {
      return {
		keywords: '',
        reverse: true,
        activities: []
      };
    },
	methods: {
		search(){
			this.getnews()
		},
		getnews() {
			this.$axios
			.get("/api/news/", {
				 params: {
					keywords: this.keywords,
				} 
			})
			.then(res => {
				console.log(res.data),
				this.activities = res.data;
			});
		}
	},
		created(){
			this.getnews()
		}
}
</script>

<style scoped>
	.time-line{
		margin-top: 20px;
	}
	.newsfooter{
	    display: flex;
	    justify-content: space-between;
	    font-size: 12px;
	}
	/* .area{
	    padding-left: 5px;
	} */
	.origin{
	    color: #6C63FF;
	    padding-left: 5px;
	}
	
	.search-2{
		z-index:9999 ;
		width:400px;
		position: fixed;
	 	top:10px;
		left:1050px;
	}
</style>
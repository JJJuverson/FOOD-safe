<template>
	<div>
		<div class="search-bar">
			<el-input placeholder="请输入内容" v-model="keywords" class="input-with-select">
				<el-button slot="append" @click="search" icon="el-icon-search"></el-button>
			</el-input>
		</div>
		
		<div style="margin-top: 20px;">
				<el-table :data="tableData" border stripe style="width: 100%" v-loading="loading">
						<el-table-column prop="id" label="编号" width="150" align="center"></el-table-column>
						<el-table-column prop="case_name" label="案件名称" width="280" align="center"></el-table-column>
						<el-table-column prop="offender" label="犯罪人" width="100" align="center"></el-table-column>
						<el-table-column prop="gender" label="性别" width="180" align="center"></el-table-column>
						<el-table-column prop="age" label="年龄" width="150" align="center"></el-table-column>
						<el-table-column prop="domicile" label="籍贯" width="150" align="center"></el-table-column>
						<el-table-column prop="criminal_behavior" label="犯罪行为" width="300" align="center"></el-table-column>
				</el-table>
				
				<div style="text-align:center;margin: 10px 0;">
					<el-pagination 
						background 
						layout="prev, pager, next" 
						@current-change = "getcases"
						:current-page.sync = "pageIndex"
						:page-size = "pageSize"
						:total="totalcount"
						></el-pagination>
				</div> 
		</div>
	</div>
    
</template>

<script>
export default {	
    data() {
      return {
		pageIndex: 1,
		keywords: '',
        loading: false,
        tableData: [],
		pageSize:2,
		totalcount:4
      };
    },	
	methods: {
		search(){
			this.pageIndex = 1,
			this.getcases()
		},
		getcases(pageIndex = 1) {
			this.loading = true,
			this.$axios
			.get("/api/case/", {
				 params: {
					keywords: this.keywords,
					pageIndex,
					pageSize: this.pageSize
				} 
			})
			.then(res => {
				this.loading = false,
				this.tableData = res.data;
			});
			
		}
	},
	created() {
		this.getcases();
	},	
}
</script>

<style>
.search-bar{
	z-index:9999 ;
	width:400px;
	position: fixed;
 	top:10px;
	left:1050px;
}
</style>

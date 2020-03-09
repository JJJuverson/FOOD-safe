<template>
    <div id="barChart" style="width:100%; height:300px;"></div>
</template>

<script>
import echarts from 'echarts'
export default {
    mounted () {
		// 基于准备好的dom，初始化echarts实例
		var myChart = echarts.init(document.getElementById('barChart'));
			// 绘制图表
		var option = {
			title : {
			text: '7天用户访问统计',
			subtext: '纯属虚构',
			//x:'center'
			x:'right'
			},
			tooltip : {
			trigger: 'axis',
			axisPointer : {            // 坐标轴指示器，坐标轴触发有效
			type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
			}
			},
			legend: {
			data:['综合案例','企业黑名单','新闻查询'],
			left: 'left'
			},
			grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
			},
			xAxis : [
			{
				type : 'category',
				data : ['周一','周二','周三','周四','周五','周六','周日']
			}
			],
			yAxis : [
			{
				type : 'value'
			}
			],
			series : [
			{
				name:'综合案例',
				type:'bar',
				data:[320, 332, 301, 334, 390, 330, 320]
			},
			{
				name:'企业黑名单',
				type:'bar',
				stack: '广告',
				data:[120, 132, 101, 134, 90, 230, 210]
			},
			{
				name:'新闻查询',
				type:'bar',
				stack: '广告',
				data:[220, 182, 191, 234, 290, 330, 310]
			},
			   
			]
		};
		myChart.setOption(option);
    }
}
</script>

<style>

</style>

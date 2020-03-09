<template>
    <div id="pieChart" style="width:100%; height:300px;"></div>
</template>

<script>
import echarts from 'echarts'
export default {
    mounted () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('pieChart'));
        // 绘制图表
    var option = {
					/* title: {
								text: '某站点用户访问来源',
								subtext: '纯属虚构', 
								left: 'center'
							}, */
					tooltip:{
									trigger: 'item',
									formatter: '{a} <br/>{b} : {c} ({d}%)'
							},
					legend: {
								orient: 'vertical',
								left: 'left',
								//data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
							},
					series: [
								{
									name: '访问来源',
									type: 'pie',
									radius: '25%',
									center: ['50%', '60%'],
									data: [
										{value:335, name:'微生物造成的食品安全问题'},
										{value:310, name:'物理性异物造成的食品安全问题'},
										{value:234, name:'化学性物质造成的食品安全问题'},
										{value:135, name:'其他物质造成的食品安全问题'},
									],
									emphasis: {
										itemStyle: {
											shadowBlur: 10,
											shadowOffsetX: 0,
											shadowColor: 'rgba(0, 0, 0, 0.5)'
										}
									}
								}
							]
				};
    myChart.setOption(option);
    }
}
</script>

<style>

</style>
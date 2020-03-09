<template>
    <div id="chartLine" style="width:100%;height:400px;"></div>
</template>

<script>
import echarts from 'echarts'
export default {
    mounted () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('chartLine'));
        // 绘制图表
    var option = {
        xAxis: {
            type: 'category',
            data: ['周一','周二','周三','周四','周五','周六','周末']
        },
        yAxis: {
            type: 'value'
        },
        tooltip: {},
        series: [{
            data:[820, 932, 901, 934, 1290, 1330, 1320],
            type:'line'
        }]
    };
    myChart.setOption(option);
    }
}
</script>

<style>

</style>

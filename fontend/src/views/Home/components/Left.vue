<!-- <template>
	<el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        background-color="#333"
        text-color="#fff"
        active-text-color="#ffd04b"
        :collapse="iscollapse"
        router  
        >
        <el-menu-item index="1" route="/">
          <i class="el-icon-setting"></i>
          <span slot="title">首&nbsp;&nbsp;&nbsp;页</span>
        </el-menu-item>        
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>食品安全管理</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="news" route="/news">热门新闻</el-menu-item>
            <el-menu-item index="blacklist" route="/blacklist">企业黑名单</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="cases" route="/case">
          <i class="el-icon-menu"></i>
          <span slot="title">食品安全案例</span>
        </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
      iscollapse: false,
      activeIndex:"1"
    }
  }
}
</script> -->

<template>
  <!-- 导航栏 -->
  <el-menu
    :default-active="$route.path"
    class="el-menu-vertical-demo"
    background-color="#333"
    text-color="#FFF"
    active-text-color="#ffd04b"
    unique-opened
    :collapse="iscollapse"
    router>
    <template v-for="(item, index) in $router.options.routes">
      <!-- 二级菜单渲染 -->
      <el-submenu :index="index+''" v-if="!item.hidden && !item.leaf" :key="index">
        <template slot="title">
          <i :class="item.iconCls"></i>
          <span slot="title">{{item.name}}</span>
        </template>
        <template v-for="child in item.children">
          <el-menu-item :index="child.path" :key="child.path" v-if="!child.hidden" :class="{subMenu: true}">
            <i :class="child.iconCls"></i>
            <span slot="title">{{child.name}}</span>
          </el-menu-item>
        </template>
      </el-submenu>
      <!-- 一级菜单渲染 -->
      <el-menu-item v-if="!item.hidden && item.leaf && item.children.length>0" :index="item.children[0].path" :key="item.children[0].path">
        <i :class="item.iconCls"></i>
        <span slot="title">{{item.children[0].name}}</span>
      </el-menu-item>
    </template>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
      iscollapse: false
    }
  }
}
</script>
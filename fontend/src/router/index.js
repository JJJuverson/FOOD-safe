import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home/index.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    component: Home,
    redirect: '/dashboard',
    name: '',
    iconCls: 'el-icon-s-help',
    leaf: true,
    children: [
      {
        path: '/dashboard',
        name: '首页',
        component: () => import('../views/Dashboard/index.vue')
      }
    ]
  }, 
  {
    path: '/',
    component: Home,
    name: '食品安全管理',
    iconCls: 'el-icon-s-data',
    leaf: false,
    children: [
      {
        name: '食品安全新闻',
        iconCls: 'el-icon-help',
        path: '/news',
       component: () => import('../views/News/index.vue')
      },
      {
        name: '企业黑名单',
        iconCls: 'el-icon-bicycle',
        path: '/blacklist',
		component: () => import('../views/Blacklist/index.vue')
      }
    ]
  }, 
  
  {
    path: '/',
    component: Home,
    name: '',
    iconCls: 'el-icon-share',
    leaf: true,
    children: [
      {
        name: '食品安全案例',
        path: '/case',
        component: () => import('../views/Cases/index.vue')
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
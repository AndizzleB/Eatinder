import Vue from 'vue'
import VueSwing from 'vue-swing'
import BootstrapVue from 'bootstrap-vue'

import App from './App.vue'
import router from './router'
import store from './store'

import './filters'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.component('vue-swing', VueSwing)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

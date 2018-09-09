<template>
  <div class="hello">
    <h2>{{ msg }}</h2>
    <p class="lead">
      A project started at <a href="https://hack.opendata.ch/event/21">Open Food Data</a> Hackdays in Zug by<br>
      <a href="https://github.com/Vera1692">Vanathy</a>, <a href="https://github.com/AndizzleB">Andrew</a>, <a href="https://github.com/loleg">Oleg</a>
    </p>
    <p><i>
    Contact us on <a href="https://team.opendata.ch/food/channels/foodclimateimpact">team.opendata.ch</a>
    or via <a href="https://github.com/AndizzleB/Eatinder/issues">GitHub Issues</a>.
    </i></p>
    <h3>Ecosystem</h3>
    <ul>
      <li><a href="https://www.sqlalchemy.org/" target="_blank">SQL Alchemy</a></li>
      <li><a href="https://flask-restful.readthedocs.io/en/latest/" target="_blank">Flask RESTful</a></li>
      <li><a href="https://flask-admin.readthedocs.io/en/latest/" target="_blank">Flask-Admin</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank">Babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank">Eslint</a></li>
    </ul>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/docs" target="_blank">vue-cli</a></li>
      <li><a href="https://router.vuejs.org/en/essentials/getting-started.html" target="_blank">vue-router</a></li>
      <li><a href="https://vuex.vuejs.org/en/intro.html" target="_blank">vuex</a></li>
      <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank">vue-devtools</a></li>
      <li><a href="https://vue-loader.vuejs.org/en" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

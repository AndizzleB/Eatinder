<template>
  <div class="about">

    <b-button class="login-button" size="lg"
      v-if="resources.length == 0" @click="fetchResource" color="info" large>Log in</b-button>

    <UserList
      v-if="resources.length > 0 && !user.username"
      v-bind:users="resources"
      v-on:selectUser="selectUser"
      />

    <MealSwing
      v-if="user.username"
      v-bind:cards="meals"
      />

    <div class="user"
         v-if="user.username">
      <b-card
            :img-src="user.gravatar"
            :img-alt="user.username"
            img-top
            style="max-width: 6rem; border: none; padding: 1em; position: absolute"
            class="mb-1"
        >
      </b-card>
    </div>

    <div class="debug">
      <h4>Dungeon of debug</h4>
      <p class="error">{{error}}</p>
      <p>
        <a href="/api/users">Users</a> | <a href="/api/labels">Labels</a> | <a href="/api/meals">Meals</a>
      |
        we <tt>&lt;3</tt>&nbsp; <a href="/admin">Open Data</a>
      </p>
      <p><tt><i>Security is a (future) feature, not a bug! --Chäpli</i></tt></p>
    </div>
  </div>
</template>

<script>

import $backend from '../backend'

import UserList from '@/components/UserList.vue'
import MealSwing from '@/components/MealSwing.vue'

export default {
  name: 'about',
  components: {
    UserList, MealSwing
  },
  data () {
    return {
      resources: [],
      meals: [],
      user: {},
      error: ''
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.resources = responseData
        }).catch(error => {
          this.error = error.message
        })
      console.log('Fetching meals')
      $backend.fetchMeals()
        .then(responseData => {
          this.meals = responseData
        }).catch(error => {
          this.error = error.message
        })
    },
    selectUser () {
      this.user = this.resources[0]
    }
  }
}

</script>

<style lang="scss">
.login-button { margin: 3em; }
.debug { opacity: 0.5; padding: 1em; margin-top: 2em; background: #eee; }
</style>

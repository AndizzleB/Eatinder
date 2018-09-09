<template>
  <div class="about">

    <b-button size="lg" v-if="resources.length == 0" @click="fetchResource" color="info" large>Log in</b-button>

    <UserList
      v-if="resources.length > 0 && !user.username"
      v-bind:users="resources"
      v-on:selectUser="selectUser"
      />

    <div class="swing"
         v-if="user.username">
         <vue-swing
          @throwout="onThrowout"
          :config="config"
          ref="vueswing"
        >
          <div
            v-for="card in cards"
            :key="card"
            class="swing-card"
          >
            <span>{{ card }}</span>
          </div>
        </vue-swing>
    </div>

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

import VueSwing from 'vue-swing'

export default {
  name: 'about',
  components: {
    UserList
  },
  data () {
    return {
      resources: [],
      user: {},
      error: '',
      config: {
        allowedDirections: [
          VueSwing.Direction.LEFT,
          VueSwing.Direction.RIGHT
        ],
        minThrowOutDistance: 250,
        maxThrowOutDistance: 300
      },
      cards: ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
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
    },
    selectUser () {
      this.user = this.resources[0]
    }
  }
}

</script>

<style lang="scss">
.debug { opacity: 0.5; padding: 1em; margin-top: 2em; background: #eee; }

.swing { height: 400px; }
.swing-card {
  align-items: center;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  font-size: 72px;
  height: 200px;
  justify-content: center;
  left: calc(50% - 100px);
  position: absolute;
  top: calc(50% - 100px);
  width: 200px;
}
</style>

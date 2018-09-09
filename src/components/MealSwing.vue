<template>
  <div class="swing">
       <vue-swing
        @throwout="onThrowout"
        :config="config"
        ref="vueswing"
      >
        <div
          v-for="card in cards"
          :key="card.id"
          class="swing-card"
        >
         <div class="container">
          <img
            :src="card.thumbnail">
          <p v-for="label in card.labels"
            :key="label.id">
            <span :title="label.name">{{ label.icon }}</span>
          </p>
          <small>{{ card.created }}</small>
         </div>
        </div>
      </vue-swing>
    <img src="@/assets/openfooddata.png">
  </div>
</template>

<script>
import VueSwing from 'vue-swing'

export default {
  name: 'swing',

  components: { VueSwing },

  props: {
    cards: Array
  },

  data () {
    return {
      config: {
        allowedDirections: [
          VueSwing.Direction.LEFT,
          VueSwing.Direction.RIGHT
        ],
        minThrowOutDistance: 250,
        maxThrowOutDistance: 300
      }
    }
  },
  methods: {
    onThrowout ({ target, throwDirection }) {
      target.hidden = true
      console.log(`Threw out ${target.textContent}!`)
    }
  }
}
</script>

<style scoped lang="scss">

.swing {
  height: 400px;
  margin-top: 50px;
}
.swing-card {
  align-items: center;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  height: 400px;
  justify-content: center;
  position: absolute;
  left: calc(50% - 150px);
  width: 300px;
}
.swing-card img {
  pointer-events: none;
}
.swing-card p {
  font-size: 32pt;
  margin: 0;
}
</style>

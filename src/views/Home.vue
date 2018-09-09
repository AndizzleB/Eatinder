<template>
  <div class="home">

    <HelloWorld msg="Hello, open data hackers!"/>

    <p>
      <img src="@/assets/openfooddata.png">
    </p>

    <!-- FORK Me -->
    <a href="https://github.com/AndizzleB/Eatinder"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_orange_ff7600.png" alt="Fork me on GitHub"></a>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>

<style lang="scss">

</style>

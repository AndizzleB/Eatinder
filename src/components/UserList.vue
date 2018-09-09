<template>
  <div>
    <b-container fluid class="p-4 bg-dark">
      <b-row>
        <b-col></b-col>
        <b-col
            v-for="item in users"
            :key="item.id"
            style="padding:0;text-align:center"
          >
          <b-card
                :img-src="item.gravatar"
                img-top
                style="max-width: 10rem"
                class="mb-1"
                @click="$emit('selectUser')"
            >
            <p class="card-text">
              {{ item.username }}
            </p>
          </b-card>
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'userlist',
  props: {
    users: Array,
    selected: Object
  }
}
</script>

<style scoped lang="scss">
</style>

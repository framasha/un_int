<template>
  <div class="more-details">
    <v-container>
      <v-btn
        color="primary"
        outlined
        class="my-2"
        @click="$router.push('/')"
      >
        <v-icon
          dark
          right
        >
          mdi-arrow-left
        </v-icon>
      </v-btn>
      <h4>Item details</h4>
      <v-row no-gutters>
        <v-col v-for="(header, headerIndex) in headers" :key="headerIndex">
          <template v-if="header.value !== 'action'">
            <v-list-item three-line>
              <v-list-item-content>
                <v-list-item-title>{{ header.text }}</v-list-item-title>
                <v-list-item-subtitle>{{ items[header.value] }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'MoreDetails',
  data () {
    return {
      items: this.$route.params.item,
      headers: [
        {
          text: 'Dessert (100g serving)',
          value: 'name'
        },
        { text: 'Calories', value: 'calories' },
        { text: 'Fat (g)', value: 'fat' },
        { text: 'Carbs (g)', value: 'carbs' },
        { text: 'Protein (g)', value: 'protein' },
        { text: 'Iron (%)', value: 'iron' },
        { text: 'Action', value: 'action' }
      ]
    }
  },
  mounted () {
    console.log(this.$route.params)
  }
}
</script>

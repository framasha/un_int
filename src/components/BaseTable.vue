<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="10"
      class="elevation-1"
    >
      <template v-slot:item.action="{ item }">
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              outlined
              v-bind="attrs"
              v-model="item.name"
              v-on="on"
            >
              <v-icon
                dark
                right
              >
                mdi-arrow-down-drop-circle
              </v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(innerItem, index) in actions"
              :key="index"
            >
              <v-btn
                :color="innerItem.color"
                outlined
                @click="processAction(item, innerItem.action)"
              >
                <v-icon
                  dark
                  right
                >
                  {{ innerItem.icon }}
                </v-icon>
                <span class="ml-2">{{ innerItem.action }}</span>
              </v-btn>
            </v-list-item>
          </v-list>
        </v-menu>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
// import tableData from './data.json'
export default {
  name: 'BaseTables',
  data () {
    return {
      actions: [
        { action: 'Edit', icon: 'mdi-pencil', color: 'primary' },
        { action: 'View', icon: 'mdi-eye', color: 'success' },
        { action: 'Delete', icon: 'mdi-delete', color: 'error' }
      ],
      headers1: [
        { text: 'ProjectID', value: 'ProjectID' },
        {
          ProjectID: 1000,
          'Project Title': 'FSGLO10S05:Youth Empowerment for Urban Development',
          'PAAS Code': 'H139',
          'Approval Status': 'Approved',
          Fund: 'FNO',
          'PAG Value': 4218607,
          'Start Date': '1-Jan-12',
          'End Date': '31-Dec-13',
          'Country(ies)': 'GLOBAL',
          'Lead Org Unit': 'Urban Economy',
          'Theme(s)': 'Urban Economy',
          'Donor(s)': 'BASF Stiftung, PM of Norway to the United Nations, The Palestinian Ministry of Public Works and Housing, , GROUP OF SPONSORS, PM OF NORWAY TO THE UNITED NATIONS',
          'Total Expenditure': 4439757,
          'Total Contribution': 4329257,
          'Total Contribution - Total Expenditure': -110500,
          'Total PSC': 316548
        }
      ],
      headers: [
        {
          text: 'Dessert (100g serving)',
          align: 'start',
          sortable: false,
          value: 'name'
        },
        { text: 'Calories', value: 'calories' },
        { text: 'Fat (g)', value: 'fat' },
        { text: 'Carbs (g)', value: 'carbs' },
        { text: 'Protein (g)', value: 'protein' },
        { text: 'Iron (%)', value: 'iron' },
        { text: 'Action', value: 'action' }
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%'
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%'
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: '7%'
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: '8%'
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: '16%'
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: '0%'
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: '2%'
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: '45%'
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: '22%'
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: '6%'
        }
      ]
    }
  },
  methods: {
    processAction (item, action) {
      switch (action) {
        case 'View':
          this.$router.push({
            name: 'About',
            params: {
              item: item
            }
          })
          break
        case 'Delete':
          this.deleteItem(item)
          break
      }
    },
    deleteItem (item) {
      const indexOf = this.desserts.map(function (e) {
        return e.calories
      }).indexOf(item.calories)
      if (indexOf > -1) {
        this.desserts.splice(indexOf, 1)
      }
    }
  }
}
</script>

<script setup>
import { onMounted, ref, unref } from "vue";
import { Chart, Grid, Line, Marker, Area, Tooltip } from "vue3-charts";

const data = ref([]);
const coins = ref([]);

onMounted(() => {
  console.log("mounted");
  fetch("/api")
    .then((resp) => resp.json())
    .then(
      (json) =>
        (data.value = Object.entries(json.data).map((x) => {
          return {
            date: x[0],
            ...x[1],
          };
        }))
    )
    .then((date) =>
      date.forEach((d) =>
        Object.keys(d).forEach((coinName) => {
          if (
            !coins.value.map((c) => c.name).includes(coinName.toUpperCase()) &&
            coinName !== "date"
          ) {
            coins.value.push({
              name: coinName.toUpperCase(),
              color: `#${Math.floor(Math.random() * 16777215).toString(16)}`,
            });
          }
        })
      )
    );
});

const getCoinColors = () => {
  return coins.value.reduce((state, curr) => {
    state[curr.name] = { color: curr.color };
    return state;
  }, {});
};

const direction = ref("horizontal");
const margin = ref({
  left: 0,
  top: 20,
  right: 20,
  bottom: 0,
});

const axis = ref({
  primary: {
    type: "band",
  },
  secondary: {
    domain: ["dataMin", "dataMax+40"],
    type: "linear",
    ticks: data.value.length,
  },
});
</script>

<template>
  <div>
    aaa{{
      {
        date: { color: "black" },
        ...getCoinColors(),
      }
    }}
  </div>
  <Chart
    :size="{ width: 4000, height: 600 }"
    :data="data"
    :margin="margin"
    :direction="direction"
    :axis="axis"
  >
    <template #layers>
      <Grid strokeDasharray="2,2" />
      <!-- <Area
        :dataKeys="['name', 'pl']"
        type="monotone"
        :areaStyle="{ fill: 'url(#grad)' }"
      /> -->
      <!-- <Line
        :dataKeys="['date', 'BTC']"
        type="monotone"
        :lineStyle="{
          stroke: '#9f7aea',
        }"
      />
      <div v-for="coin in coins" :key="coin.name">{{ coin.name }}</div> -->
      <Line
        v-for="coin in coins"
        :key="coin.name"
        :dataKeys="['date', coin.name]"
        type="monotone"
        :lineStyle="{
          stroke: coin.color,
        }"
      />
    </template>

    <template #widgets>
      <Tooltip
        borderColor="#48CAE4"
        :config="{
          date: { color: 'black' },
          ...getCoinColors(),
        }"
      />
    </template>
  </Chart>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>

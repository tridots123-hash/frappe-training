<template>
   <div class="m-5">
      <Button @click="totdoList.fetch()">Show Movies</Button>
      <LoadingText v-if="totdoList.list.loading"/>
      <div v-if="totdoList.data">
          <ul>
            <li v-for="todo in totdoList.data">{{ todo.name }}</li>
          </ul>
      </div>
   </div>
</template>

<script setup>
import { LoadingText, Button } from "frappe-ui";
import { createListResource } from "frappe-ui";

const totdoList = createListResource({
  doctype: "Class Records",
  fields: ["name"],
})
</script>

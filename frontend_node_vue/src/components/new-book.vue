<script setup>

import {ref} from "vue";

const bookName = ref('')
const bookNameError = ref(false)
const authorName = ref('')
const authorError = ref(false)

const message = ref('')

function onSubmit() {
  message.value = ''
  bookNameError.value = false
  authorError.value = false

  if (bookName.value === '') {
    bookNameError.value = true
    message.value = 'Please add a book name.'
  }
  if (authorName.value === '') {
    authorError.value = true
    message.value += ' Please add an author name.'
  }

  if(authorError.value || bookNameError.value) return

  fetch('http://localhost:4000/books/', {
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      title: bookName.value,
      author: authorName.value,
    }),
    method: 'POST',
  }).then((res) => {
    console.log(res)
  })
}
</script>

<template>
  <div class="card">
    <h1>Add new book</h1>
    <p v-if="message">{{message}}</p>
    <input id="book-name" :class="bookNameError ? 'error' : ''" v-model="bookName" placeholder="Enter a book name..." />
    <input id="author-name" :class="authorError ? 'error' : ''" v-model="authorName" placeholder="Enter author name..."  />
    <button @click="onSubmit">Submit</button>
  </div>
</template>

<style scoped>
.card {
  margin: 56px;
  padding: 16px;
  border-radius: 16px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  display: flex;
  flex-direction: column;
}

p {
  color: #f87676;
}

input {
  margin: 16px 32px;
  padding: 16px;
  border-radius: 16px;
  border: 1px solid darkgray;
}

.error {
  border: 1px solid #fd8888;
}

button {
  margin: 16px 32px;
  padding: 16px;
  border-radius: 16px;
  background-color: #0d70cd;
  color: #fff;
  font-size: 16px;
  font-weight: bold;
}
</style>
<template>
    <div>
      <h1>房产信息管理</h1>
      <button @click="addProperty">添加房产</button>
      <ul>
        <li v-for="property in properties" :key="property.id">
          {{ property.name }} - {{ property.price }}元
          <button @click="editProperty(property.id)">编辑</button>
          <button @click="deleteProperty(property.id)">删除</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ManagePropertiesPage', // 修改为多单词名称
    data() {
      return {
        properties: [
          { id: 1, name: '房产A', price: 1000000 },
          { id: 2, name: '房产B', price: 1200000 },
        ],
      };
    },
    methods: {
      addProperty() {
        alert('添加房产功能未实现');
      },
      editProperty(id) {
        alert(`编辑房产 ID: ${id}`);
      },
      deleteProperty(id) {
        this.properties = this.properties.filter(property => property.id !== id);
      },
    },
  };
  </script>
  
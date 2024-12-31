<template>
    <div>
      <h1>销售人员管理</h1>
      <button @click="addSalesPerson">添加销售人员</button>
      <ul>
        <li v-for="salesPerson in salesPeople" :key="salesPerson.id">
          {{ salesPerson.name }} - {{ salesPerson.email }}
          <button @click="editSalesPerson(salesPerson.id)">编辑</button>
          <button @click="deleteSalesPerson(salesPerson.id)">删除</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ManageSalesPage', // 修改为多单词名称
    data() {
      return {
        salesPeople: [
          { id: 1, name: '张三', email: 'zhangsan@example.com' },
          { id: 2, name: '李四', email: 'lisi@example.com' },
        ],
      };
    },
    methods: {
      addSalesPerson() {
        alert('添加销售人员功能未实现');
      },
      editSalesPerson(id) {
        alert(`编辑销售人员 ID: ${id}`);
      },
      deleteSalesPerson(id) {
        this.salesPeople = this.salesPeople.filter(salesPerson => salesPerson.id !== id);
      },
    },
  };
  </script>
  
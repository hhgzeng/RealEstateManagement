<template>
    <div>
      <h2>注册</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="用户名" />
        <input type="password" v-model="password" placeholder="密码" />
        <select v-model="role">
          <option value="customer">顾客</option>
          <option value="salesperson">销售员</option>
        </select>
        <button type="submit">注册</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'RegisterPage', 
    data() {
      return {
        username: '',
        password: '',
        role: 'customer',
      };
    },
    methods: {
      async register() {
        try {
          await axios.post('http://localhost:8000/accounts/register/', {
            username: this.username,
            password: this.password,
            role: this.role,
          });
          alert('注册成功！');
          this.$router.push('/login');
        } catch (error) {
          alert('注册失败，请重试');
        }
      },
    },
  };
  </script>
  
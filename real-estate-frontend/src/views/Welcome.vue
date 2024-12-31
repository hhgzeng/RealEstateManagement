<template>
  <div>
    <h1>欢迎来到管理员界面</h1>
    <nav>
      <ul>
        <li><router-link to="/manage-properties">房产信息管理</router-link></li>
        <li><router-link to="/manage-sales">销售人员管理</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage', // 修改为多单词名称
};
</script>
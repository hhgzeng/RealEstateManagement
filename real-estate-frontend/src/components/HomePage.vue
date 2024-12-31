<template>
  <div class="home-page">
    <div class="header">
      <h2>房产销售管理系统</h2>
      <div class="auth-buttons">
        <button class="login-btn" @click="$router.push('/login')">登录</button>
        <button class="register-btn" @click="$router.push('/login?register=true')">注册</button>
      </div>
    </div>

    <div class="main-content">
      <!-- 在售房产列表 -->
      <div class="section">
        <h3>在售房产</h3>
        <div class="card">
          <div class="filters">
            <div class="filter-group">
              <label>价格区间：</label>
              <input 
                v-model.number="filters.minPrice" 
                type="number" 
                placeholder="最低价" 
              />
              <span>-</span>
              <input 
                v-model.number="filters.maxPrice" 
                type="number" 
                placeholder="最高价" 
              />
            </div>
            <div class="filter-group">
              <label>面积区间：</label>
              <input 
                v-model.number="filters.minArea" 
                type="number" 
                placeholder="最小面积" 
              />
              <span>-</span>
              <input 
                v-model.number="filters.maxArea" 
                type="number" 
                placeholder="最大面积" 
              />
            </div>
            <button class="filter-btn" @click="applyFilters">筛选</button>
            <button class="reset-btn" @click="resetFilters">重置</button>
          </div>

          <div class="houses-grid">
            <div v-for="house in filteredHouses" :key="house.id" class="house-card">
              <div class="house-info">
                <h4>房产编号: {{ house.id }}</h4>
                <div class="info-row">
                  <span class="label">价格：</span>
                  <span class="value price">{{ formatPrice(house.price) }}</span>
                </div>
                <div class="info-row">
                  <span class="label">面积：</span>
                  <span class="value">{{ house.area }}㎡</span>
                </div>
                <div class="info-row">
                  <span class="label">楼层：</span>
                  <span class="value">{{ house.floor }}层</span>
                </div>
                <div class="info-row">
                  <span class="label">销售人员：</span>
                  <span class="value">{{ house.salesperson_name }}</span>
                </div>
              </div>
              <div class="house-actions">
                <button class="buy-btn" @click="promptLogin">购买</button>
              </div>
            </div>
          </div>

          <div v-if="filteredHouses.length === 0" class="no-data">
            暂无符合条件的房产
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
  data() {
    return {
      houses: [],
      filters: {
        minPrice: '',
        maxPrice: '',
        minArea: '',
        maxArea: ''
      }
    };
  },
  computed: {
    filteredHouses() {
      return this.houses.filter(house => {
        const price = parseFloat(house.price);
        const area = parseFloat(house.area);
        
        if (this.filters.minPrice && price < this.filters.minPrice) return false;
        if (this.filters.maxPrice && price > this.filters.maxPrice) return false;
        if (this.filters.minArea && area < this.filters.minArea) return false;
        if (this.filters.maxArea && area > this.filters.maxArea) return false;
        
        return true;
      });
    }
  },
  created() {
    this.fetchHouses();
  },
  methods: {
    formatPrice(price) {
      return parseFloat(price).toLocaleString('zh-CN');
    },
    async fetchHouses() {
      try {
        const response = await axios.get('http://localhost:8000/houses/get_houses/');
        this.houses = response.data;
      } catch (error) {
        console.error('获取房产列表失败:', error);
      }
    },
    promptLogin() {
      if (confirm('需要登录后才能购买房产，是否前往登录？')) {
        this.$router.push('/login');
      }
    },
    applyFilters() {
      // 过滤功能已通过计算属性实现
    },
    resetFilters() {
      this.filters = {
        minPrice: '',
        maxPrice: '',
        minArea: '',
        maxArea: ''
      };
    }
  }
};
</script>

<style scoped>
.home-page {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.header h2 {
  margin: 0;
  color: #2c3e50;
}

.auth-buttons {
  display: flex;
  gap: 10px;
}

.login-btn, .register-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s;
}

.login-btn {
  background-color: #2196F3;
  color: white;
}

.register-btn {
  background-color: #4CAF50;
  color: white;
}

.main-content {
  display: grid;
  gap: 20px;
}

.section {
  margin-bottom: 30px;
}

.section h3 {
  color: #2c3e50;
  margin-bottom: 15px;
}

.card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-group input {
  width: 100px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.houses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.house-card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.house-info {
  flex: 1;
}

.info-row {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
}

.label {
  color: #666;
}

.value {
  font-weight: 500;
}

.value.price::before {
  content: "¥";
  margin-right: 8px;
}

.value.price {
  color: #e53935;
  font-weight: bold;
}

.house-actions {
  display: flex;
  justify-content: flex-end;
}

.buy-btn {
  background-color: #4CAF50;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s;
}

.filter-btn {
  background-color: #2196F3;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.reset-btn {
  background-color: #9e9e9e;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.no-data {
  text-align: center;
  color: #666;
  padding: 20px;
}

button:hover {
  opacity: 0.9;
}

@media (max-width: 768px) {
  .filters {
    flex-direction: column;
  }
  
  .filter-group {
    width: 100%;
  }
  
  .filter-group input {
    flex: 1;
  }
  
  .houses-grid {
    grid-template-columns: 1fr;
  }
}
</style> 
import React, { useEffect, useState } from 'react';
import TransactionList from './components/TransactionList';
import AddTransactionForm from './components/AddTransactionForm';
import Dashboard from './components/Dashboard';
import axios from 'axios';

function App() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    axios.get('/api/categories/')
      .then(res => setCategories(res.data));
  }, []);

  return (
    <div>
      <h1>LedgerFlow</h1>
      <AddTransactionForm categories={categories} />
      <TransactionList />
      <Dashboard />
    </div>
  );
}

export default App;
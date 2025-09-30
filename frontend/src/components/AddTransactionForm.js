import React, { useState } from 'react';
import axios from 'axios';

function AddTransactionForm({ categories }) {
    const [form, setForm] = useState({
        amount: '',
        description: '',
        date: '',
        category: '',
        transaction_type: 'expense',
    });
    const [suggestedCategory, setSuggestedCategory] = useState('');

    const handleChange = e => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSuggestCategory = () => {
        axios.post('/api/categorize/', { description: form.description })
            .then(res => setSuggestedCategory(res.data.category))
            .catch(err => alert('Error suggesting category'));
    };

    const handleSubmit = e => {
        e.preventDefault();
        axios.post('/api/transactions/', form)
            .then(() => alert('Transaction added!'))
            .catch(() => alert('Error adding transaction'));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input name="amount" value={form.amount} onChange={handleChange} placeholder="Amount" required />
            <input name="description" value={form.description} onChange={handleChange} placeholder="Description" required />
            <input name="date" type="date" value={form.date} onChange={handleChange} required />
            <select name="category" value={form.category} onChange={handleChange} required>
                <option value="">Select Category</option>
                <option value={suggestedCategory}>{suggestedCategory ? `Suggested: ${suggestedCategory}` : 'No Suggestion'}</option>
                {categories.map(cat => <option key={cat.id}>{cat.name}</option>)}
            </select>
            <select name="transaction_type" value={form.transaction_type} onChange={handleChange}>
                <option value="expense">Expense</option>
                <option value="income">Income</option>
            </select>
            <button type="button" onClick={handleSuggestCategory}>Suggest Category</button>
            {suggestedCategory && <div>Suggested: {suggestedCategory}</div>}
            <button type="submit">Add Transaction</button>
        </form>
    )
}

export default AddTransactionForm;
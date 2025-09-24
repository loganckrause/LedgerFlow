import React, { useEffect, useState } from 'react';
import axios from 'axios';

function TransactionList() {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        axios.get('/api/transactions/')
            .then(res => setTransactions(res.data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div>
            <h2>Transactions</h2>
            <ul>
                {transactions.map(tx => (
                    <li key={tx.id}>
                        {tx.date} - {tx.description} - ${tx.amount} ({tx.category})
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TransactionList;
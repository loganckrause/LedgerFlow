import React, { useEffect, useState } from 'react';
import { Pie } from 'react-chartjs-2';
import axios from 'axios';

function Dashboard() {
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
        axios.get('/api/transactions/')
            .then(res => {
                const data = res.data;
                const categories = {};
                data.forEach(tx => {
                    const cat = typeof tx.category === 'string' ? tx.category : (tx.category?.name || tx.category?.id || 'Uncategorized');
                    categories[tx.category] = (categories[tx.category] || 0) + parseFloat(tx.amount);
                });
                setChartData({
                    labels: Object.keys(categories),
                    datasets: [{
                        data: Object.values(categories),
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
                    }]
                });
            });
    }, []);

    return (
        <div>
            <h2>Spending by Category</h2>
            {chartData && chartData.labels.length > 0 ? (
                <Pie data={chartData} />
            ) : (
                <p>No data to display.</p>
            )}
        </div>
    );
}

export default Dashboard;
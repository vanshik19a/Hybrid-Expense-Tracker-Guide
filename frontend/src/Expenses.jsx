import api from './api';
import { useEffect, useState } from 'react';

function Expenses() {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    api.get('/api/expenses/')
       .then(res => setExpenses(res.data))
       .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Expenses</h2>
      <ul>
        {expenses.map(exp => (
          <li key={exp.id}>{exp.title}: ₹{exp.amount}</li>
        ))}
      </ul>
    </div>
  );
}

export default Expenses;

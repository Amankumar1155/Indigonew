import React, { useState } from 'react';
import './App.css';

function App() {
  const [flightId, setFlightId] = useState('');
  const [status, setStatus] = useState(null);

  const checkStatus = async () => {
    const response = await fetch(`/api/status/${flightId}`);
    const data = await response.json();
    setStatus(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Flight Status Checker</h1>
        <input 
          type="text" 
          value={flightId} 
          onChange={(e) => setFlightId(e.target.value)} 
          placeholder="Enter Flight ID" 
        />
        <button onClick={checkStatus}>Check Status</button>
        {status && (
          <div>
            <h2>Status: {status.status}</h2>
            <p>Gate: {status.gate}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;

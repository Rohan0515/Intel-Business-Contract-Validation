import React, { useState } from 'react';
import axios from 'axios';

const ReportGenerator = () => {
    const [contractId, setContractId] = useState('');
    const [report, setReport] = useState(null);

    const handleGenerateReport = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get(`http://localhost:5000/validate/${contractId}`);
            setReport(response.data);
        } catch (error) {
            console.error('Error generating report:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleGenerateReport}>
                <input type="text" placeholder="Contract ID" value={contractId} onChange={(e) => setContractId(e.target.value)} />
                <button type="submit">Generate Report</button>
            </form>
            {report && (
                <div>
                    <h3>Deviation Report</h3>
                    <pre>{JSON.stringify(report, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default ReportGenerator;

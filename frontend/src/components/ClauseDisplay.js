import React from 'react';

const ClauseDisplay = ({ clauses }) => (
    <div>
        <h3>Parsed Clauses</h3>
        {clauses.map((clause, index) => (
            <div key={index} className={`clause ${clause.label}`}>
                {clause.text}
            </div>
        ))}
    </div>
);

export default ClauseDisplay;

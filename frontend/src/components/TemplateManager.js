import React, { useState } from 'react';
import axios from 'axios';

const TemplateManager = () => {
    const [name, setName] = useState('');
    const [structure, setStructure] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const template = { name, structure: JSON.parse(structure) };
        try {
            const response = await axios.post('http://localhost:5000/template', template);
            console.log('Template uploaded:', response.data);
        } catch (error) {
            console.error('Error uploading template:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Template Name" value={name} onChange={(e) => setName(e.target.value)} />
            <textarea placeholder="Template Structure" value={structure} onChange={(e) => setStructure(e.target.value)}></textarea>
            <button type="submit">Upload Template</button>
        </form>
    );
};

export default TemplateManager;

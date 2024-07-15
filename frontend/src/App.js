import React from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import UploadForm from './components/UploadForm';
import ClauseDisplay from './components/ClauseDisplay';
import TemplateManager from './components/TemplateManager';
import ReportGenerator from './components/ReportGenerator';
import NotificationCenter from './components/NotificationCenter';

const App = () => (
    <div>
        <Navbar />
        <Dashboard />
        <UploadForm />
        <ClauseDisplay clauses={[]} />
        <TemplateManager />
        <ReportGenerator />
        <NotificationCenter notifications={[]} />
    </div>
);

export default App;

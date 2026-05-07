const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const CSV_FILE = path.join(__dirname, 'data', 'field_reports.csv');

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(__dirname));

app.post('/save-report', (req, res) => {
    const { workerId, event } = req.body;
    
    if (!workerId || !event) {
        return res.status(400).json({ error: 'Field Worker ID and Event are required' });
    }

    const eventId = `EVT-${Date.now()}`;
    const timestamp = new Date().toISOString();
    
    // Sanitize input to avoid CSV injection or breaking the format
    const sanitize = (str) => `"${(str || '').replace(/"/g, '""')}"`;
    
    // Structure: Event_ID, Timestamp, Field_Worker_ID, Event, Municipality (empty)
    const newRow = `${eventId},${timestamp},${sanitize(workerId)},${sanitize(event)},\n`;

    fs.appendFile(CSV_FILE, newRow, (err) => {
        if (err) {
            console.error('Error writing to CSV:', err);
            return res.status(500).json({ error: 'Failed to save data' });
        }
        res.status(200).json({ message: 'Report saved successfully', eventId });
    });
});

app.get('/get-reports', (req, res) => {
    fs.readFile(CSV_FILE, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading CSV:', err);
            return res.status(500).json({ error: 'Failed to read data' });
        }
        res.status(200).send(data);
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

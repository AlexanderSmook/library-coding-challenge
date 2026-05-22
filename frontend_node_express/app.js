const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json()); // For parsing JSON requests
app.use(express.urlencoded({ extended: true })); // For parsing URL-encoded requests


app.get('/', (req, res) => {
    res.send('Hello World!')
});
  
// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
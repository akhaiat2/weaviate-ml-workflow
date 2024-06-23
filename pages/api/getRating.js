// pages/api/getRating.js

import { exec } from 'child_process';
import path from 'path';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { query } = req.body;

    const scriptPath = path.resolve('./predict.py');

    exec(`python3 ${scriptPath} "${query}"`, (error, stdout, stderr) => {
      if (error) {
        console.error('Error executing Python script:', error);
        res.status(500).json({ error: 'Error making prediction' });
        return;
      }

      if (stderr) {
        console.error('Error from Python script:', stderr);
        res.status(500).json({ error: 'Error making prediction' });
        return;
      }

      const result = JSON.parse(stdout);
      res.status(200).json(result);
    });
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}

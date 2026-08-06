
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { message, sender_number, method } = req.body;

    const supabaseUrl = 'https://aplyaoxzqcuuuyjlvrgm.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFwbHlhb3h6cWN1dXV5amx2cmgmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMzIyNjgsImV4cCI6MjA5MDkwODI2OH0.022Gp7f-eCvI_D5jv5JAq16svmuaIZp-U6CyxZJgP4g';

    const response = await fetch(`${supabaseUrl}/rest/v1/incoming_sms`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': supabaseKey,
        'Authorization': `Bearer ${supabaseKey}`,
        'Prefer': 'resolution=merge-duplicates'
      },
      body: JSON.stringify({
        trx_id: message,
        amount: message,
        sender_number: sender_number || '',
        method: method || 'bKash'
      })
    });

    const data = await response.json();
    return res.status(200).json({ success: true, data });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}

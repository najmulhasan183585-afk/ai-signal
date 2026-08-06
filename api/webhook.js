export default async function handler(req, res) {
  if (req.method === 'GET') {
    return res.status(200).json({ status: 'Webhook is active and ready!' });
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { message, sender_number, method } = req.body;

    if (!message) {
      return res.status(400).json({ error: 'Message is missing' });
    }

    // এসএমএস থেকে TrxID এবং Amount আলাদা করার ফাংশন (Parser)
    function parseSMS(text) {
      let trx_id = null;
      let amount = 0;

      // TrxID খোঁজার চেষ্টা (যেমন: TrxID 9H87G6F5D4)
      const trxMatch = text.match(/(?:trx\s*id|trxid)[:\s]*([a-z0-9]+)/i) || text.match(/\b([A-Z0-9]{8,12})\b/);
      if (trxMatch) {
        trx_id = trxMatch[1] || trxMatch[0];
      }

      // Amount খোঁজার চেষ্টা (যেমন: Tk 100 বা ৳100)
      const amountMatch = text.match(/(?:tk|৳|bdt|amount)[:\s]*([0-9]+(?:\.[0-9]+)?)/i) || text.match(/([0-9]+(?:\.[0-9]+)?)\s*(?:tk|৳|bdt)/i);
      if (amountMatch) {
        amount = parseFloat(amountMatch[1]);
      }

      return { trx_id, amount };
    }

    const parsed = parseSMS(message);

    if (!parsed.trx_id || !parsed.amount) {
      return res.status(400).json({ 
        error: 'Could not parse TrxID or Amount from message', 
        raw_message: message 
      });
    }

    const supabaseUrl = 'https://aplyaoxzqcuuuyjlvrgm.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFwbHlhb3h6cWN1dXV5amx2cmgmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMzIyNjgsImV4cCI6MjA5MDkwODI2OH0.022Gp7f-eCvI_D5jv5JAq16svmuaIZp-U6CyxZJgP4g';

    // সুপাবেজের incoming_sms টেবিলে পার্স করা ডাটা পাঠানো
    const response = await fetch(`${supabaseUrl}/rest/v1/incoming_sms`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': supabaseKey,
        'Authorization': `Bearer ${supabaseKey}`,
        'Prefer': 'resolution=merge-duplicates'
      },
      body: JSON.stringify({
        trx_id: parsed.trx_id,
        amount: parsed.amount,
        sender_number: sender_number || '',
        method: method || 'bKash'
      })
    });

    const data = await response.json();
    return res.status(200).json({ success: true, parsed, data });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}

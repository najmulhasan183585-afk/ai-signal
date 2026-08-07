export default async function handler(req, res) {
  if (req.method === 'GET') {
    return res.status(200).json({ status: 'Webhook is active and ready!' });
  }

  try {
    // অ্যাপ থেকে বডি বা কোয়েরি প্যারামিটার যাই আসুক না কেন, সব এক জায়গায় নিয়ে আসা
    const inputData = req.method === 'POST' ? { ...req.body, ...req.query } : req.query;

    // অ্যাপ ভেদে মেসেজ, টেক্সট বা বডি যেকোনো নামে আসতে পারে, সবগুলো চেক করবে
    const message = inputData.message || inputData.text || inputData.body || inputData.msg;
    const sender_number = inputData.sender_number || inputData.sender || inputData.from || '';
    const method = inputData.method || 'bKash';

    if (!message) {
      return res.status(400).json({ 
        error: 'Message is missing', 
        received_body: inputData 
      });
    }

    // এসএমএস পার্স করার উন্নত ফাংশন
    function parseSMS(text) {
      let trx_id = null;
      let amount = 0;

      // TrxID খোঁজার চেষ্টা
      const trxMatch = text.match(/(?:trx\s*id|trxid|TrxID|Trx ID)[:\s]*([a-z0-9]+)/i) || text.match(/\b([A-Z0-9]{8,12})\b/);
      if (trxMatch) {
        trx_id = trxMatch[1] || trxMatch[0];
      } else {
        // যদি TrxID না থাকে, তবে একটি ইউনিক আইডি তৈরি করে নেবে
        trx_id = 'AUTO-' + Date.now() + '-' + Math.floor(Math.random() * 1000);
      }

      // Amount খোঁজার চেষ্টা
      const amountMatch = text.match(/(?:tk|৳|bdt|amount)[:\s]*([0-9]+(?:\.[0-9]+)?)/i) || text.match(/([0-9]+(?:\.[0-9]+)?)\s*(?:tk|৳|bdt)/i);
      if (amountMatch) {
        amount = parseFloat(amountMatch[1]);
      }

      return { trx_id, amount };
    }

    const parsed = parseSMS(message);

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
        trx_id: parsed.trx_id,
        amount: parsed.amount || 0,
        sender_number: sender_number,
        method: method
      })
    });

    const data = await response.json();
    return res.status(200).json({ success: true, parsed, data });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}

<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Pattern Input</title>
    <style>
        :root {
            --big-color: #3498db;
            --small-color: #e67e22;
            --bg-color: #f4f7f6;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .card {
            background: #fff;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 450px;
        }

        .row {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
            background: #f9f9f9;
            padding: 10px;
            border-radius: 12px;
        }

        .label {
            min-width: 80px;
            padding: 10px;
            border-radius: 8px;
            color: white;
            font-weight: bold;
            text-align: center;
            font-size: 14px;
        }

        .big-label { background: var(--big-color); }
        .small-label { background: var(--small-color); }

        .btn-group {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }

        .num-btn {
            width: 35px;
            height: 35px;
            border: 1px solid #ddd;
            background: white;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.2s;
            font-weight: bold;
        }

        .num-btn:hover {
            background: #333;
            color: white;
        }

        #display {
            margin-top: 20px;
            padding: 15px;
            background: #222;
            color: #00ff00;
            border-radius: 10px;
            min-height: 40px;
            word-break: break-all;
            font-family: monospace;
        }
    </style>
</head>
<body>

<div class="card">
    <h3 style="text-align:center; margin-top:0;">Pattern Analysis System</h3>
    
    <div class="row">
        <div class="label big-label">+Big</div>
        <div class="btn-group">
            <button class="num-btn" onclick="add('B-5')">5</button>
            <button class="num-btn" onclick="add('B-6')|">6</button>
            <button class="num-btn" onclick="add('B-7')">7</button>
            <button class="num-btn" onclick="add('B-8')">8</button>
            <button class="num-btn" onclick="add('B-9')">9</button>
        </div>
    </div>

    <div class="row">
        <div class="label small-label">+Small</div>
        <div class="btn-group">
            <button class="num-btn" onclick="add('S-0')">0</button>
            <button class="num-btn" onclick="add('S-1')">1</button>
            <button class="num-btn" onclick="add('S-2')">2</button>
            <button class="num-btn" onclick="add('S-3')">3</button>
            <button class="num-btn" onclick="add('S-4')">4</button>
        </div>
    </div>

    <div id="display">Input: </div>
    <button onclick="document.getElementById('display').innerText = 'Input: '" style="width:100%; margin-top:10px; cursor:pointer; padding:5px; border-radius:5px; border:1px solid #ccc;">Reset</button>
</div>

<script>
    function add(val) {
        const screen = document.getElementById('display');
        if(screen.innerText === "Input: ") {
            screen.innerText += val;
        } else {
            screen.innerText += ", " + val;
        }
    }
</script>

</body>
</html>

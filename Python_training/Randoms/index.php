<?php
 
$db = new SQLite3('users.db');
 
function simple_waf($input) {
    $blacklist = ['UNION', 'SELECT', 'OR', 'AND', '--', '#', ' '];
    foreach ($blacklist as $bad) {
        if (stripos($input, $bad) !== false) {
            die("🚫 WAF detected malicious input!");
        }
    }
    return $input;
}
 
function show_login_form($error = '') {
    echo <<<HTML
    <html>
    <head>
        <title>Salty Spitoon Login</title>
        <style>
            body {
                background-color: #1e1e2f;
                color: #f0f0f0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: #2c2f4a;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
                text-align: center;
            }
            input {
                padding: 10px;
                margin: 10px 0;
                width: 80%;
                border: none;
                border-radius: 5px;
                background: #3c3f5c;
                color: white;
            }
            button {
                padding: 10px 20px;
                background: #6f4ef2;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            button:hover {
                background: #8a6cf5;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 10px;
            }
            .error {
                color: #ff6961;
                font-weight: bold;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 Welcome to Salty Spitoon 🔥</h1>
            <img src="login.jpg" alt="Login Image" style="width:250px;"><br><br>
            <form method="POST">
                <div class="error">{$error}</div>
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <button type="submit">💀 Enter</button>
            </form>
        </div>
    </body>
    </html>
    HTML;
    exit;
}
 
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    show_login_form();
}
 
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';
 
$username = simple_waf($username);
$password = simple_waf($password);
#
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $db->query($query);
 
if ($result->fetchArray()) {
    echo <<<HTML
    <html>
    <head>
        <title>Welcome to the Spitoon</title>
        <style>
            body {
                background-color: #121212;
                color: #e0e0e0;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            img {
                width: 60%;
                max-width: 600px;
                margin-top: 30px;
                border-radius: 12px;
            }
        </style>
    </head>
    <body>
        <h1>🎉 Welcome, warrior! 🎉</h1>
        <img src="dashboard.jpeg" alt="Dashboard Image">
    </body>
    </html>
    HTML;
} else {
    show_login_form("❌ Access denied.");
}
?>
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Docker</title>
        <style>
            body {
                background: #e0f7fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #004d40;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                animation: fadeIn 2s ease-in-out;
            }
            h1 {
                font-size: 3rem;
                animation: slideDown 1.5s ease-out;
            }
            p {
                font-size: 1.3rem;
                margin-top: 10px;
                color: #00695c;
                animation: slideUp 1.5s ease-out;
            }
            @keyframes slideDown {
                from { transform: translateY(-50px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            @keyframes slideUp {
                from { transform: translateY(50px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to Docker</h1>
        <p>Here we will learn Docker from beginning to master 👨‍💻</p>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'Server is up and running'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():    
        return '<html><body>Hello, <strong>Flask</strong>!</body></html>'

if __name__ == '__main__':
        app.run(debug=True,host="0.0.0.0")

    
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
    <body>
    <center>
    <h1>Demo on GitOps with ArgoCD and Github Actions.</h1> <br>
    <br>
    <h1>TEST 2</h1>
    </center>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("Hello, World!")
    app.run(debug=True)

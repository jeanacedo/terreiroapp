from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/filhos')
def filhos():
    return render_template('filhos.html')

@app.route('/giras')
def giras():
    return render_template('giras.html')

@app.route('/mensalidades')
def mensalidades():
    return render_template('mensalidades.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Esto le dice a Python que busque tu index.html en la carpeta templates
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    git remote add origin https://github.com/TUUSUARIO/MiAppPortfolio.git
git push -u origin master


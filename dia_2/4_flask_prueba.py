from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    print('hola')
    return
        '<h1> hola mundo </h1> '
        '<h2>sdsdsd<h2>'

    


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    print('hola')
    html='''<h1> hola mundo </h1>
    <h2>saludos para todos</2>
    titulo  '''
    return html
       

    


if __name__ == '__main__':
    app.run(debug=True)


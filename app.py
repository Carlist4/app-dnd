from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    titulo_web = "Mi Primera Web con Docker y Flask"
    mensaje = "¡Hola! Si ves esto, tu contenedor y Flask están comunicándose a la perfección."

    return render_template('index.html', titulo=titulo_web, saludo=mensaje)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
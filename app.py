import json
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'coloca_aqui_una_clave_secreta_aleatoria' # Necesario para usar sesiones

# Función para leer el archivo JSON según el idioma actual
def get_translation(key):
    # Si el usuario no ha elegido nada, por defecto ponemos inglés ('en')
    lang = session.get('lang', 'en')
    try:
        with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
            translations = json.load(f)
        return translations.get(key, key) # Devuelve la traducción, o la clave si no la encuentra
    except FileNotFoundError:
        return key

# Esto hace que la función 't' y el idioma actual estén disponibles en todos los HTML
@app.context_processor
def inject_globals():
    return dict(t=get_translation, current_lang=session.get('lang', 'en'))

# Ruta para cambiar de idioma mediante un enlace o botón
@app.route('/lang/<lang_code>')
def change_language(lang_code):
    if lang_code in ['es', 'en']:
        session['lang'] = lang_code
    # Devuelve al usuario a la página anterior donde estaba
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, jsonify
from ai_core import generar_texto_posthumano
from db import guardar_prompt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    respuesta = ''
    if request.method == 'POST':
        prompt = request.form['prompt']
        respuesta = generar_texto_posthumano(prompt)
        guardar_prompt(prompt, respuesta)
    return render_template('index.html', respuesta=respuesta)

@app.route('/api/invocar', methods=['POST'])
def api_invocar():
    data = request.get_json()
    prompt = data.get('prompt', '')
    respuesta = generar_texto_posthumano(prompt)
    guardar_prompt(prompt, respuesta)
    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)

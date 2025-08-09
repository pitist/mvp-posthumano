from transformers import pipeline

generador = pipeline('text-generation', model='gpt2')

def generar_texto_posthumano(prompt):
    resultado = generador(prompt, max_length=100, do_sample=True)[0]['generated_text']
    return resultado

import streamlit as st
from gtts import gTTS
import tempfile

# Diccionario con palabras a traducir
diccionario = {
    'a': 'uno ',
    'b': 'dos ',
    'c': 'tres ',
    'd': 'cuatro ',
    'e': 'cinco ',
    'f': 'seis ',
    'g': 'siete ',
    'mi': 'ri ',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = []
    mi_present = False

    for palabra in palabras:
        if palabra.lower() == 'mi':
            oracion_traducida.append(diccionario['mi'])
            mi_present = True
        else:
            oracion_traducida.append(diccionario.get(palabra.lower(), palabra))
    
    # Si 'mi' está presente, aseguramos que esté en segundo lugar
    if mi_present:
        # Si hay más de una palabra, movemos 'mi' al segundo lugar
        if len(oracion_traducida) > 1:
            oracion_traducida.remove(diccionario['mi'])
            oracion_traducida.insert(1, diccionario['mi'])
    
    return " ".join(oracion_traducida).strip()

def reproducir_audio(texto, lang):
    tts = gTTS(text=texto, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
        tts.save(tmp.name)
        with open(tmp.name, 'rb') as audio_file:
            audio_bytes = audio_file.read()
    return audio_bytes

st.title("Traductor de números")

# Estado de la sesión para la traducción
if 'oracion_traducida' not in st.session_state:
    st.session_state.oracion_traducida = ""

# Opción para introducir texto
oracion_usuario = st.text_input("Introduce una palabra:")

# Traducir la oración ingresada por el usuario
if oracion_usuario:
    oracion_traducida = traducir_oracion(oracion_usuario)
    st.session_state.oracion_traducida = oracion_traducida
    st.write(f"Traducción: {oracion_traducida}")
    audio_bytes = reproducir_audio(oracion_traducida, 'es')  # Usando español por defecto
    st.audio(audio_bytes, format='audio/mp3')

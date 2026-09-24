import streamlit as st
import random
from gtts import gTTS
import base64

# Configuración de la página web
st.title("🎴 Lotería de Especies")

especies = [
    "Jaguar", "Zarigüeya", "Tortuga Caguama", "Coatí", "Cocodrilo de Pantano",
    "Coral Cuernos de Alce", "Sardinilla Yucateca", "Mero", "Fragata Portuguesa",
    "Flamenco Rojo", "Martín Pescador", "Loro Yucateco", "Tortuga Carey",
    "Oso Hormiguero", "Armadillo", "Rana Manglera", "Camarón Rosado",
    "Mangle Botoncillo", "Ibis Blanco", "Garza Blanca", "Mangle Rojo",
    "Tortuga Blanca", "Mangle Blanco", "Mangle Negro", "Ocelote", "Cacerolita de Mar"
]

# Guardar estado de la partida
if 'mazo' not in st.session_state:
    st.session_state.mazo = []
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Botón para barajar e iniciar
if st.button("🎲 Barajar y Empezar Nueva Partida"):
    st.session_state.mazo = especies.copy()
    random.shuffle(st.session_state.mazo)
    st.session_state.historial = []
    st.success("¡Lotería barajada!")

# Botón para sacar la siguiente carta
if st.button("📢 Cantar Siguiente Carta"):
    if st.session_state.mazo:
        carta = st.session_state.mazo.pop()
        st.session_state.historial.append(carta)
        
        st.header(f"¡{carta}!")
        
        # Generar audio al vuelo
        tts = gTTS(text=f"¡{carta}!", lang='es', tld='com.mx')
        tts.save("carta.mp3")
        
        # Reproducir audio automáticamente
        audio_file = open("carta.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    else:
        st.warning("¡Ya se cantaron todas las cartas!")

# Mostrar historial de cartas cantadas
if st.session_state.historial:
    st.subheader("Cartas que ya salieron:")
    st.write(", ".join(st.session_state.historial))

import streamlit as st
from PIL import Image

st.title("Mi primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Primera.jpg')

st.image(image, caption='Interfaces Multimodales')


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

coll, col2 = st.columns(2)

with coll:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'Auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La auditiva es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('La táctil es fundamental para tu interfaz')

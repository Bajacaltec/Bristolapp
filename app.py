from email.utils import collapse_rfc2231_value
from enum import auto
import streamlit as st
fol1,fol2=st.columns(2)
with fol1:
    st.title("                            BristolApp")

with fol2:
    st.image("WAPP.png",None,350)

st.subheader("Identifica el tipo de evacuaciones que tienes y verémos si necesitas ajustar tu dieta")
col1,col2,col3,col4,col5,col6,col7=st.columns(7)

with col1:
    st.subheader('B1')
    st.image('B1.png')
    st.markdown("Pedazos duros separados. Como nueces y con excreción difícil")
with col2:
    st.subheader('B2')
    st.image("B2.png")
    st.markdown("Con forma de salchicha, pero grumosa (compuesta de fragmentos")
with col3:
    st.subheader("B3")
    st.image("B3.png")
    st.markdown("Con forma de salchica, pero con grietas en la superficie")
with col4:
    st.subheader('B4')
    st.image("B4.png")
    st.markdown('Con forma de salchica pero lisa y suave')
with col5:
    st.subheader("B5")
    st.image('B5.png')
    st.markdown("Trozos de pastosos con bordes bien definidos")
with col6:
    st.subheader("B6")
    st.image('B6.png')
    st.markdown("Pedazos blandos y esponjosos con bordes irregulares")
with col7:
    st.subheader("B7")
    st.image('B7.png',None,200,auto)
    st.markdown('Acuosa, sin pedazos sólidos, totalmente líquida')
selecccion=st.select_slider('Elige',['B1','B2','B3','B4','B5','B6','B7'])

if selecccion=='B1':
    st.warning("Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente")
elif selecccion=='B2':
    st.warning('Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente')
elif selecccion=='B3':
    st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
elif selecccion=='B4':
    st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
if selecccion=='B5':
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if selecccion=='B6':
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if selecccion==True:
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')

      





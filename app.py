import streamlit as st
st.image("WAPP.png",None,300)
st.title("                            BristolApp")
st.subheader("Identifica el tipo de evacuaciones que tienes y verémos si necesitas ajustar tu dieta")
col1,col2=st.columns(2)



sel=st.select_slider('Bristol', ['0','1','2','3','4','5','6','7'])
if sel=='1':
    with col1:
        st.image('B1.png')
    with col2:
        st.subheader("Pedazos duros separados. Como Nueces")

    st.info("Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente")
elif sel=='2':
    with col1:
        st.image('B2.png')
    with col2:
        st.subheader("Con forma de salchica, pero grumosa (compuesta de fragmentos)")
    st.info("Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente")

elif sel=='3':
    with col1:
        st.image('B3.png')
    with col2:
        st.subheader("Con forma de Salchica, pero con grietas en la superficie")
    st.success("Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces")
    st.balloons()
elif sel=='4':
    with col1:
        st.image('B4.png')
    with col2:
        st.subheader("Con forma de salchicha pero lisa y suave")
    st.success("Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces")
    st.balloons()
elif sel=='5':
    with col1:
        st.image('B5.png')
    with col2:
        st.subheader("Trozos pastosos con bordes bien definidos")
    st.warning("Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica")
elif sel=='6':
    with col1:
        st.image('B6.png')
    with col2:
        st.subheader("Pedazos blandos y esponjosos con bordes irregulares")
    st.warning("Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica")

elif sel=='7':
    with col1:
        st.image('B7.png')
    with col2:
        st.subheader("Acuosa, sin pedazos sólidos, totalmente")
    st.warning("Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica")

#Come
import streamlit as st
import mi_libreria as ml
import pandas as pd
import plotly.express as px

st.title ("Mi Aplicacion Python")
st.sidebar.title ("Parametros")
st.sidebar.image("logo_python.png",width=100)

modulo = st.sidebar.selectbox ("Seleccione un módulo",["Módulo 1", "Módulo 2", "Módulo 3"])
if modulo=="Módulo 1":
    st.write("Usted esta en Modulo 1")
    ge=st.number_input ("Ingrese la gravedad especifica",min_value=0.1,max_value=1.0,value=0.8)
    api= ml.grado_api (ge)
    st.write ("El grado api es:", round (api,2))
elif modulo=="Módulo 2":
    st.write("Usted esta en Modulo 2")
    df=pd.read_excel("resultado.xlsx")
    st.write(df)
    fig=px.line(df,x=df.index,y="api")
    st.write(fig)
else:
    st.write("Usted esta en Modulo 3")

 # Cargar archivo (CSV o Excel)
    uploaded_file = st.file_uploader("Sube tu archivo CSV o Excel", type=["csv", "xlsx"])
    
    # Verificar si se ha subido un archivo
    if uploaded_file is not None:
        # Determinar el tipo de archivo subido
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        # Mostrar el DataFrame cargado
        st.write(df)
    else:
        st.write("Por favor, sube un archivo CSV o Excel para continuar.")
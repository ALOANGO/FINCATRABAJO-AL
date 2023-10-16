import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import matplotlib
from scrap_total import scrap_total
import base64
import lxml




#Configurar titulo y descripcion de la app
st.set_page_config(page_title='APP FINCATRABAJO -by Andres Loango',
                   layout='wide',
                   initial_sidebar_state='auto' )

st.set_option('deprecation.showPyplotGlobalUse', False)

#CARGAR LOS DATAFRAMES HISTORICOS
df=pd.read_csv("data_contatenada.csv", sep=',')
                  



#Catalogo de paginas

barra_lateral=st.sidebar
#seleccion_pagina = barra_lateral.checkbox("Selecciona una pestaña:", ["Propiedades en venta", "Modelo"])
paginas= ["Propiedades Antioquia 🏠", "Modelo 🧮"]
pagina=barra_lateral.radio('Seleccione una pagina :',paginas)


if pagina=="Propiedades Antioquia 🏠":

    st.title("Propiedades en Antioquia 🏠")

    
     # Mostrar la tabla filtrada
    #st.write(f"Tamaño de la tabla: {df.shape}")
    #st.dataframe(df)


    

    fuentes_disponibles = df['fuente'].unique()
    fuentes_seleccionadas = barra_lateral.multiselect("Fuente", fuentes_disponibles)

    # Filtrar por tipo de vivienda
    tipos_vivienda_disponibles = df['tipopropiedad'].unique()
    tipo_vivienda_seleccionada = barra_lateral.multiselect("Tipo de propiedad", tipos_vivienda_disponibles)




    # Aplicar los filtros
    if fuentes_seleccionadas and tipo_vivienda_seleccionada:
        df_filtrado = df[df['fuente'].isin(fuentes_seleccionadas) & df['tipopropiedad'].isin(tipo_vivienda_seleccionada)]
    elif fuentes_seleccionadas:
        df_filtrado = df[df['fuente'].isin(fuentes_seleccionadas)]
    elif tipo_vivienda_seleccionada:
        df_filtrado = df[df['tipopropiedad'].isin(tipo_vivienda_seleccionada)] 
    else:
        df_filtrado = df
                            
    # Mostrar la tabla filtrada

    st.dataframe(df_filtrado)
    st.write(f"Tamaño de la tabla filtrada: {df_filtrado.shape}")




   

    #BOTON ACTUALIZAR

    boton_actualizar= (barra_lateral.button("Actualizar data"))
    
    if boton_actualizar:
        df=scrap_total()
        



    # Descargar el DataFrame filtrado
    barra_lateral.download_button(
        label="Download CSV",
        data=df_filtrado.to_csv(index=False),
        file_name='fincar_df_filtrado.csv',
        mime=('text/csv'))







if  pagina=="Modelo 🧮":
    
                    
    st.title('FINCA-TRABAJO 🧮') 
    st.markdown("Modelo para predecir el precio de una vivienda basado en los datos ingresados.")
    st.markdown("---")


    #CARGAR EL MODELO
    model=pickle.load(open('price.pkl', 'rb'))

    #CARGAR EL SCALER
    scalerlinear=pickle.load(open('scalerlinear.pkl', 'rb'))


    #lectura de datos [['aream2', 'toilets', 'garajes', 'estrato']]

    area=st.text_input('Aream2')
    toilets=st.text_input('Baños')
    garajes=st.text_input('Garajes')
    estrato=st.text_input('Estrato')

    #CREAMOS UNA FUNCION PREDICCION DEL MODELO

    def modelo_prediction(x_in, modelo, scaler):
        data=np.array([x_in])

        
        data_escalada=scaler.transform(data)

        preds=modelo.predict(data_escalada)

        return preds



    # El botón predicción se usa para iniciar el procesamiento. si se oprime, arranca este proceso
    #features=[area, toilets, garajes, estrato] 
    if st.button("Predicción :"): 
            #x_in = list(np.float_((Datos.title().split('\t'))))
        features =[(area.title()),
                    (toilets.title()),
                    (garajes.title()),
                    (estrato.title()),]
        predecir=modelo_prediction(features, model, scalerlinear)
        st.success("El valor de la vivienda es "  "COP {:,.0f}".format(predecir[0]))     







#Quitar marca de agua streamlit
#footer{visibility:hidden;}
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import matplotlib
from scraping_dataframe_fr import fincaraiz
from metrocuadrado import metrocuadrado
import base64






#Configurar titulo y descripcion de la app
st.set_page_config(page_title='APP FINCATRABAJO -by Andres Loango',
                   layout='centered',
                   initial_sidebar_state='auto' )

st.set_option('deprecation.showPyplotGlobalUse', False)

#CARGAR LOS DATAFRAMES HISTORICOS
                   
dataframe_total_fr=pd.read_csv('fincaraizdatatotal.csv')
dataframe_total_m2=pd.read_csv('metroc2.csv')


#Catalogo de paginas
selected_tab = st.sidebar.selectbox("Selecciona una pestaña:", ["Modelo", "Data Finca R","Data Metro2"])

if selected_tab == "Modelo":
    
                    
    st.title('FINCA-TRABAJO') 
    st.markdown("Esta App predice el precio de la vivienda, basado en los datos ingresados.")
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



elif selected_tab == "Data Finca R":
    st.title("Datos de viviendas del departamento de Antioquia (Finca Raiz)")
    

    boton_1= st.button("Generar data")

    if boton_1:
    
        #COORDENADAS CALI Y JAMUNDI
        antioquia=[[-75.7751988,7.0938077],[-75.3140647788699,5.6973074]]

        #DATAFRAME CASAS
        dfantioquiahouse= fincaraiz("house",antioquia)

        #DATAFRAME APARTAMENTOS
        dfantioquiapartment= fincaraiz("apartment",antioquia)

        #CONCATENAR DATAFRAME CASAS Y APTOS
        df= pd.concat([dataframe_total_fr,dfantioquiahouse,dfantioquiapartment])
        df.drop_duplicates(['idpropiedad'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv('fincaraizdatatotal.csv', index=False)

        # Mostrar la tabla filtrada
        st.write(f"Tamaño de la tabla: {df.shape}")
        st.dataframe(df)

        st.download_button(
            label="DownloadCSV",
            data=df.to_csv(index=False),
            file_name='fincar_df.csv',
            mime=('text/csv'))


elif selected_tab == "Data Metro2":
    st.title("Datos de viviendas del departamento de Antioquia (Metro cuadrado)")
    
    boton_2= st.button("Generar data")

    if boton_2:
    
        cities=["Medellin",	"Bello","Itagui",	"Envigado",	"Sabaneta",	"Estrella",	"Caldas",	"Copacabana",	"Girardota",	"Barbosa",	"Rionegro",	"Viboral",	"Retiro",	"Ceja",	"Marinilla",	"Penol",	"Guatape",	"Vicente",	"union",	"Guarne",	"Cocorna",	"Apartado",	"Turbo",	"Carepa",	"Chigorodo",	"Necocli",	"Arboletes",]
        datametrocuadrado=metrocuadrado(cities)

        df2= pd.concat([dataframe_total_m2, datametrocuadrado])
        df2.drop_duplicates(['propid'], inplace=True)
        df2.reset_index(drop=True, inplace=True)
        df2.to_csv('metroc2.csv', index=False)

        # Mostrar la tabla filtrada
        st.write(f"Tamaño de la tabla: {df2.shape}")
        st.dataframe(df2)
  
        st.download_button(
            label="DownloadCSV",
            data=df2.to_csv(index=False),
            file_name='fincar_df.csv',
            mime=('text/csv'))




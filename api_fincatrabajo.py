import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px






#Configurar titulo y descripcion de la app
st.set_page_config(page_title='APP FINCATRABAJO -by Andres Loango',
                   layout='centered',
                   initial_sidebar_state='auto' )

st.set_option('deprecation.showPyplotGlobalUse', False)
                   
dataframe_total=pd.read_csv('fincaraizdatatotal.csv')

#Catalogo de paginas
selected_tab = st.sidebar.selectbox("Selecciona una pestaña:", ["Modelo", "Dataframe", "Distrib precio"])

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



elif selected_tab == "Dataframe":
    st.title("Tabla de Datos con Gráfico de Barras")
    

    # Deslizador para ajustar el precio de la vivienda
    house_price = st.slider("Precio de la Vivienda", min_value=int((dataframe_total['precio'].min()))
                            , max_value=int((dataframe_total['precio'].max())))

    # Filtrar los datos basados en el precio seleccionado
    filtered_data = dataframe_total[dataframe_total['precio'] <= house_price]
    st.write(f"Las dimensiones de la tabla son: {filtered_data.shape}")

    # Mostrar la tabla filtrada
    st.write("Tabla filtrada:")
    st.dataframe(filtered_data)

    # Crear un gráfico de barras interactivo utilizando Plotly
    fig = px.bar(filtered_data, x='antiguedad', y='precio', title=f'Precios de viviendas hasta ${house_price}')
    st.plotly_chart(fig)


elif selected_tab == "Distrib precio":
    st.title("Distribucion vivienda por precio")
    st.write("A continuación se muestra un gráfico de dispersión:")
    
    # Generar un gráfico de dispersión usando Matplotlib
    fig1 = px.scatter_mapbox(dataframe_total, lat=('latitud'), lon=('longitud'),
                        hover_name="barrio",
                        color='precio',
                        size='aream2',
                        text="tipopropiedad",
                        title='DISTRIBUCION POR PRECIO',
                        zoom=9, height=500)

    #Update the map style
    fig1.update_layout(mapbox_style='open-street-map')

    #Show the plot
    #fig.show()
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig1.show())    



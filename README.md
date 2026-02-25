
# Análisis del Mercado Inmobiliario en Cali: Factores Clave en el Precio de Vivienda

Bienvenido al repositorio de este proyecto de analítica de datos. Aquí se aborda el ciclo de vida completo de la información: desde la extracción de datos mediante web scraping hasta la implementación de modelos predictivos para entender el mercado inmobiliario en la ciudad de Cali y sus alrededores.

## 1. Antecedentes del Proyecto
Debido a la inexistencia de un registro público de viviendas en venta actualizado, este proyecto utiliza un dataset obtenido directamente de varios portales **Finca raiz, Metrocuadrado, Lonja** mediante un proceso de wepscraping. Como analista de datos, el objetivo es identificar las variables que realmente impactan el costo de los inmuebles en la región.

Se proporcionan insights y recomendaciones en las siguientes áreas clave:
* **Correlación de Precios:** Impacto directo de las características físicas.
* **Infraestructura Interna:** Relación entre área, habitaciones y baños.
* **Factores Externos:** Análisis de influencia por zona, altura y antigüedad.
* **Modelado Predictivo:** Importancia de variables mediante Random Forest.

> **Recursos del Proyecto:**
> * Las consultas y procesos de limpieza de datos se encuentran en los notebooks de procesamiento.
> * El análisis detallado de las preguntas de negocio se detalla en las secciones de EDA.[link](https://deepnote.com/workspace/training-454c-c4d00094-0817-4ff7-adc7-305ee39e3c92/project/PROYECTO-FINCATRABAJO-ANDRES-LOANGO-0d49d79d-78b5-47a5-9daa-3c77c411c9a1/notebook/0-PROBLEMATICA-A-ABORDAR-b81d0c3f1fbe41cc8a57f34ec98eca00?secondary-sidebar-autoopen=true&secondary-sidebar=agent)
> * El modelo final de predicción de precios utiliza el algoritmo de **Random Forest**.

---

## 2. Estructura de Datos y Validaciones Iniciales
La base de datos analizada consolida la información capturada del portal inmobiliario. La descripción de los componentes principales es la siguiente:
* **Variable Objetivo:** Precio de venta de la vivienda.
* **Características Físicas:** Área total, número de habitaciones, baños y garajes.
* **Características del Anuncio:** Zona de ubicación, antigüedad y altura (pisos). 

---

## 3. Resumen Ejecutivo
### Resumen de Hallazgos
Tras completar el ciclo de análisis con un **95% de confianza** en el método, se determinó que lo que más influye en la diferencia de precio de una vivienda es su **área construida**. Este hallazgo fue ratificado por el modelo de Random Forest. Sorprendentemente, el análisis confirmó que ni la zona, ni la antigüedad, ni la altura de la vivienda influyen de manera significativa en el precio final de venta bajo los datos actuales.

---

## 4. Análisis Detallado de Insights

### a. Dimensiones y Espacios Internos
* **Área vs. Habitaciones:** Existe una correlación positiva estadísticamente significativa del **60%**.
* **Área vs. Baños:** Se presenta una correlación aún más fuerte, alcanzando el **74%**.
* **Impacto de Garajes:** Se encontró un hallazgo inesperado con una correlación del **70%** entre el número de garajes y el precio de la vivienda.

### b. Factores Externos y de Estructura
* **Ubicación y Edad:** Se pudo confirmar estadísticamente que ni la zona ni la antigüedad de la vivienda influyen en el precio de la misma.
* **Altura:** En el análisis del precio con respecto a la altura (número de pisos) no se encontró una correlación significativa.

### c. Modelado Predictivo
* **Variable Crítica:** El modelo de **Random Forest** generado para la predicción de precios confirmó que el área es el factor de mayor peso para determinar el valor de mercado.

---

## 5. Recomendaciones
Con base en los insights y hallazgos, se recomienda al equipo de analistas e inversionistas considerar lo siguiente:
* **Priorización de Metraje:** Dado que el área es el principal predictor de precio, los esfuerzos de inversión deben centrarse en el metraje total por encima de la ubicación geográfica específica.
* **Valorización por Garajes:** Considerar el número de garajes como un factor crítico de valorización, dada su alta correlación con el precio final.
* **Revisión de Tasación:** No penalizar ni sobrevalorar inmuebles basándose únicamente en la antigüedad o la zona, ya que los datos sugieren que estos factores no son determinantes en este mercado.

---

## 6. Supuestos y Consideraciones
A lo largo del análisis, se realizaron los siguientes supuestos para manejar los datos:
* **Confianza Estadística:** Todas las conclusiones se presentan con un nivel de confianza del **95%**.
* **Origen de Datos:** Se asume que los datos capturados vía scraping de Mercadolibre son representativos de la oferta actual del mercado en Cali.
* **Relación de Variables:** Se reconoce que, aunque existe una mayor correlación entre el precio y el tamaño, correlación no implica necesariamente causalidad en todos los casos.

---

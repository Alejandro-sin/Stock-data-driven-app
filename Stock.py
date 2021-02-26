#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''


https://www.eurogamer.es/articles/2021-01-27-que-esta-pasando-con-el-valor-en-bolsa-de-gamestop

https://aroussi.com/post/python-yahoo-finance

https://docs.streamlit.io/en/stable/getting_started.html


Una idea sería dividir las cosas en módlos de trabajo, por ejemplo el trabajo de extracción de datos de la libreía yfinance

https://www.youtube.com/channel/UCbmb5IoBtHZTpYZCDBOC1CA

En este canal hay mucho más material que puedo usar para engordar este proyecto.

'''

import streamlit as st
import pandas as pd
import yfinance as yf
from googletrans import Translator



# In[5]:

st.title('Bolsa de Valores')
st.write('''

Esta aplicación web tiene como propósito mostrar un conjunto de datos históricos 
a partir de la librería **yfinance** la cual está basada en los reportes de Yahoo Finance que fueron retirados,
esta librería apunta a resolver una forma pythonica de bajar data.


### Idea principal

* Sin embargo la idea principal es realizar un análisis de lo que sucedio con gamespot y wallsstreet,
unificar la infroamción con más detalles como conexión con api de twitter para análisis de sentimientos
de los mayores inversionistas de wallstreet al respecto durante el mes de gamespot.



* Revisar si puedomodificar el markdown con el formato de github para poder ingresarle iconos y cosas así de Metah Datha.
como la imagen de un static container de wordpress.


* Puedo poner una tabla de markdown y juntarla con un format t string?
* Puedo usar la tabla  como un menú de navegación  a los gráficos.


* A Streamlit le falta un manualcito para que la gente lo vaya usar , usar un markdown 

##### Para poner cosas pequeñas, e instrucciones importantes
##### Haga doble click en al imagen para regresar al tamño normal.

''')

st.text('Esto es un texto de prueba')

# Defino el símbolo de ticker

ticker_dict = {
    'game_stop' : 'GME',
    'carrefour' : 'CA',
    'best_buy' : 'BBY'
}


context = ['longBusinessSummary', 'sector','shortName','logo_url']

gme_data = yf.Ticker(ticker_dict['game_stop'])
gme_info = gme_data.info
st.write(gme_info)



st.write(f'''

## Un acto de rebelión 

![logo](https://logo.clearbit.com/gamestop.com)

**[{gme_info['shortName']}](https://www.gamespot.com/)** es una industria de "{gme_info['industry']}" y pertenecen al sector de "{gme_info['sector']}" que define sus operaciones así:

> "{gme_info['longBusinessSummary']}"


''')




st.write(
    '''
    ## GameStop
    
    I want to write a litle comment about GameSpot

    '''
)

gme_history = gme_data.history(period='1d', start='2010-1-1', end='2021-01-30')
st.line_chart(gme_history)


# Escribo un data frame.

st.write(
    pd.DataFrame({
        'list_a':[1,2,34,5,5],
        'list_b':[3,24,534,55,55]
    })
)


# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ TRADUCCIÓN ELEMENTOS.
# translator = Translator()
# t = translator.translate('Perro', dest='es')
# st.write(t)

import streamlit as st
import requests

'''
# Welcome to TaxiFare


'''

date = st.date_input("Date du voyage")
time = st.time_input('Heure du voyage')
pickup_datetime = f'{date} {time}'

# departure = st.text_input('Adresse de départ :', 'Lille, France')
# arrival = st.text_input("Adresse d'arrivée :", 'Marseille, France')

pickup_longitude = st.number_input('Longitude de départ :', value=0.0)
pickup_latitude = st.number_input('Latitude de départ :', value=0.0)
dropoff_longitude = st.number_input('Longitude d\'arrivée :', value=0.0)
dropoff_latitude = st.number_input('Latitude d\'arrivée :', value=0.0)

passenger_count = st.slider('Nombre de passagers', 1, 8, 1)

if st.button('Combien ça coûte ?'):
    # print is visible in the server output, not in the page
    print('button clicked!')

    url = 'https://taxifare.lewagon.ai/predict'

    params = dict(
            pickup_datetime=pickup_datetime,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count
        )

    response = requests.get(url, params=params).json()

    fare = round(response["fare"], 1)
    st.write(f'${fare}')

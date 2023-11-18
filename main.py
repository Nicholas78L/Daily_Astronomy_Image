import streamlit as st
import requests

# My API NASA: R1bXD0evdXHADAEhcDMA8sCmVhCaVqq6YMef60uU

api_key = 'R1bXD0evdXHADAEhcDMA8sCmVhCaVqq6YMef60uU'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)
content = response.json()

st.title(content['title'])
st.image(content['url'])
st.text_area(content['explanation'])

import streamlit as st
import requests
import numpy as np

N = 10

st.write('Welcome to page 2')

url="https://api.giphy.com/v1/gifs/search"
params={
    "api_key": st.secrets.giphy_api_key,
    "q": "cool",
    "limit": N,
}

response = requests.get(url, params=params)
image_data = response.json()["data"]
rand_gif_url = image_data[np.random.randint(0, N-1)]["embed_url"]
st.write(
    f'<iframe src="{rand_gif_url}" width="480" height="240"',
    unsafe_allow_html=True
)

st.image(
    rand_gif_url,
    width = 400,
)
st.markdown(
    rand_gif_url,
    unsafe_allow_html=True
)
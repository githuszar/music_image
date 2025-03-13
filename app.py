# Certifique-se de instalar todas as dependências com:
# pip install streamlit requests pandas pillow numpy matplotlib

import os
import random
import requests
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# Configuração inicial
CLIENT_ID = "e983ab76967541819658cb3126d9f3df"
CLIENT_SECRET = "4f4d1a7a3697434db2a0edc2c484f80c"
REDIRECT_URI = "https://musicimage.streamlit.app/callback"
AUTH_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com/v1"

# Função para obter o token de acesso do Spotify
def get_spotify_access_token(auth_code):
    payload = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(AUTH_URL, data=payload)
    return response.json().get("access_token")

# Função para buscar os principais artistas do usuário
def get_top_artists(access_token):
    url = f"{API_BASE_URL}/me/top/artists?limit=5"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json().get("items", [])

# Função para buscar os principais gêneros musicais do usuário
def get_top_tracks_features(access_token):
    url = f"{API_BASE_URL}/me/top/tracks?limit=5"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    tracks = response.json().get("items", [])
    
    # Buscar características de áudio
    track_ids = ",".join([track["id"] for track in tracks])
    url_features = f"{API_BASE_URL}/audio-features?ids={track_ids}"
    response_features = requests.get(url_features, headers=headers)
    features = response_features.json().get("audio_features", [])
    
    return features

# Criar diretório para armazenar imagens
visualization_dir = "visualization"
os.makedirs(visualization_dir, exist_ok=True)

# Função para gerar imagem baseada nas características musicais
def generate_simple_image(user_id, features):
    width, height = 500, 500
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)
    
    if features:
        energy = features[0]["energy"] * 255
        valence = features[0]["valence"] * 255
        danceability = features[0]["danceability"] * 255
    else:
        energy, valence, danceability = 128, 128, 128  # Valores padrão

    for x in range(width):
        for y in range(height):
            draw.point((x, y), (int(energy), int(valence), int(danceability)))

    img_path = f"{visualization_dir}/{user_id}.png"
    img.save(img_path)
    return img_path

# Criar interface no Streamlit
st.title("🎨 Gerador de Imagens Musicais com Spotify")

if st.button("🎵 Gerar Imagem com Spotify"):
    st.write("🔑 Por favor, autentique-se no Spotify para continuar.")
    auth_url = f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=user-top-read"
    st.markdown(f"[Clique aqui para autenticar no Spotify]({auth_url})")
    auth_code = st.text_input("Cole aqui o código de autenticação do Spotify")
    if auth_code:
        access_token = get_spotify_access_token(auth_code)
    top_artists = get_top_artists(access_token)
    track_features = get_top_tracks_features(access_token)
    
    user_id = "spotify_user"
    img_path = generate_simple_image(user_id, track_features)
    
    st.image(img_path, caption=f"Imagem baseada no perfil musical do Spotify", use_column_width=True)
    st.success("✅ Imagem gerada com sucesso!")

# Rodar o código localmente
# Salve o código como `app.py` e execute no terminal:
# streamlit run app.py

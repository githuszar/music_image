🎵 Gerador de Imagens Musicais com Spotify

📌 Descrição

Este projeto gera imagens abstratas personalizadas baseadas nos dados musicais do Spotify de um usuário. Utiliza Streamlit para fornecer uma interface interativa e a API do Spotify para buscar as principais músicas e artistas, gerando imagens únicas baseadas nesses dados.

🚀 Funcionalidades

✅ Autenticação no Spotify para capturar os dados do usuário.
✅ Geração de imagem abstrata baseada nos atributos musicais reais (energia, valência, dançabilidade).✅ Interface interativa via Streamlit para gerar e visualizar as imagens.✅ Deploy pronto para o Streamlit Cloud com uma URL fixa.

🔧 Tecnologias Utilizadas

Python 3.8+

Streamlit (Interface interativa)

Requests (Consumo da API do Spotify)

Pandas (Manipulação de dados)

Pillow (Geração de imagens)

Numpy (Cálculos de normalização)

Matplotlib (Exibição de imagens)

🛠️ Configuração e Execução

1️⃣ Instale as dependências

pip install streamlit requests pandas pillow numpy matplotlib

2️⃣ Execute o projeto localmente

streamlit run app.py

3️⃣ Deploy no Streamlit Cloud (Opcional)

Se deseja rodar online:

Faça login no Streamlit Cloud

Conecte seu repositório do GitHub

Publique seu projeto e obtenha uma URL fixa

🔑 Configuração da API do Spotify

Para integrar o Spotify, adicione o REDIRECT_URI no painel de desenvolvedor do Spotify:

URI para configurar no Spotify:

https://seu-app.streamlit.app/callback

Após adicionar, o Streamlit solicitará autenticação e usará os dados do usuário para gerar a imagem personalizada.

📸 Exemplo de Uso

Clique no botão "🎵 Gerar Imagem com Spotify"

Faça login no Spotify

A imagem será gerada baseada nas suas músicas favoritas 🎶

📂 Estrutura do Projeto

📂 gerador-imagens-musicais/
├── 📂 api/  (Consumo da API do Spotify)
│   ├── spotify_auth.py  (Autenticação)
│   ├── get_tracks.py  (Obter músicas e artistas)
│
├── 📂 data/  (Geração de dados e insights musicais)
│   ├── process_data.py
│
├── 📂 visualization/  (Geração de imagens abstratas)
│   ├── generate_image.py
│
├── app.py  (Código principal)
├── requirements.txt  (Dependências)
├── README.md  (Documentação)

📝 Licença

Este projeto é open-source e pode ser usado livremente. 🚀🎶


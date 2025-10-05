import streamlit as st
from grafo import generar_grafo
from simulacion import simular_interacciones
from ranking import top_k_publicaciones
from pyvis.network import Network
import streamlit.components.v1 as components
import pandas as pd
import os

# config inicial
st.set_page_config(page_title="Simulación Red Social", layout="wide")
st.markdown("<h1 style='text-align: center;'> Simulación de interacción en redes sociales</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Detección de publicaciones populares</p>", unsafe_allow_html=True)

st.divider()

# parametrps
st.subheader("Parámetros de simulación")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Datos iniciales")
    num_users = st.slider("Número de usuarios", 200, 1500, 500, step=100)
    num_posts = st.slider("Número de publicaciones", 50, 500, 200, step=50)
    avg_follow = st.slider("Promedio de seguidores por usuario", 5, 200, 20, step=5)
    seed = st.number_input("Número aleatorio base (para variar la simulación)", value=42, step=1)

    if st.button("Generar grafo"):
        G, posts = generar_grafo(num_users, num_posts, avg_follow, seed)
        st.session_state['G'] = G
        st.session_state['posts'] = posts
        st.success(f"Grafo generado correctamente con {len(G.nodes())} nodos y {len(G.edges())} conexiones.")

with col2:
    st.markdown("####  Controles de simulación y ranking")

    if 'G' in st.session_state:
        if st.button(" Simular una iteración"):
            G = st.session_state['G']
            posts = st.session_state['posts']
            G = simular_interacciones(G, posts, seed=seed)
            st.session_state['G'] = G
            st.success("Simulación aplicada (1 iteración)")

        if st.button(" Simular 10 iteraciones"):
            G = st.session_state['G']
            posts = st.session_state['posts']
            for _ in range(10):
                G = simular_interacciones(G, posts)
            st.session_state['G'] = G
            st.success("Simulación aplicada (10 iteraciones)")

        if st.button(" Mostrar Top 10 publicaciones"):
            G = st.session_state['G']
            posts = st.session_state['posts']
            top = top_k_publicaciones(G, posts, k=10)
            df = pd.DataFrame(top)
            st.dataframe(df[['post', 'autor', 'score', 'likes', 'comentarios', 'compartidos', 'reach']], use_container_width=True)

        if st.checkbox(" Mostrar grafo interactivo"):
            G = st.session_state['G']
            net = Network(height="600px", width="100%", directed=True, bgcolor="#F8F9FA", font_color="#222")

            # añadir nodos
            for n, d in G.nodes(data=True):
                if d['tipo'] == 'usuario':
                    net.add_node(n, label=n, title=str(n), color="#8ecae6", size=8)
                else:
                    label = f"{n}\n❤️ {d.get('likes',0)}"
                    net.add_node(n, label=label, title=str(n), color="#ffb4a2", size=16)

            # añadir aristas
            for u, v in G.edges():
                net.add_edge(u, v)

            tmpfile = "grafo_vis.html"
            try:
                net.save_graph(tmpfile)
                with open(tmpfile, "r", encoding="utf-8") as f:
                    html = f.read()
                components.html(html, height=650, scrolling=True)
            except Exception as e:
                st.error(f"Ocurrió un error al renderizar el grafo: {e}")

st.divider()
st.caption("Desarrollado en Streamlit — Proyecto de simulación de redes sociales")

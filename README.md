Use recorridos en grafos (BFS y DFS) para simular cómo los usuarios interactúan con publicaciones dentro de una red social. 
Cada nodo puede ser un usuario o una publicación, y las conexiones representan follows o interacciones. 
A través de estas búsquedas se calcula el alcance y la popularidad de cada publicación, lo que nos permite detectar cuáles tienden a volverse más populares con el tiempo. 
La idea fue combinar simulación, visualización y algoritmos para entender mejor cómo se propaga la interacción en una red social.

Pasos:
crear un entorno virtual

python -m venv venv
venv\Scripts\activate


instalar las librerías necesarias

pip install -r requirements.txt


ejecutarlo

streamlit run app.py

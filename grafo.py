import networkx as nx
import random

def generar_grafo(num_usuarios=500, num_publicaciones=100, avg_following=20, seed=42):
    random.seed(seed)
    G = nx.DiGraph()
    users = [f'U{i}' for i in range(num_usuarios)]

    # nodos usuarios
    for u in users:
        G.add_node(u, tipo='usuario')

    # aristas follow u sigue a v
    for u in users:
        n_follow = max(1, int(random.gauss(avg_following, max(1, avg_following/3))))
        for _ in range(n_follow):
            v = random.choice(users)
            if v != u:
                G.add_edge(u, v)

    # posts
    posts = []
    for j in range(num_publicaciones):
        author = random.choice(users)
        post_id = f'P{j}'
        G.add_node(post_id, tipo='publicacion', autor=author, likes=0, comentarios=0, compartidos=0, timestamp=0, reach=0)
        G.add_edge(author, post_id)  # relación autor -> post
        posts.append(post_id)

    return G, posts

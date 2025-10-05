import random

def simular_interacciones(G, posts, p_like=0.03, p_comment=0.007, p_share=0.003, seed=None):
    if seed is not None:
        random.seed(seed)
    for post in posts:
        author = G.nodes[post]['autor']
        followers = list(G.predecessors(author))  # quienes siguen al autor
        for follower in followers:
            r = random.random()
            if r < p_like:
                G.nodes[post]['likes'] += 1
            elif r < p_like + p_comment:
                G.nodes[post]['comentarios'] += 1
            elif r < p_like + p_comment + p_share:
                G.nodes[post]['compartidos'] += 1

    # alcance (simplificado): seguidores del autor
    for post in posts:
        author = G.nodes[post]['autor']
        G.nodes[post]['reach'] = len(list(G.predecessors(author)))

    return G

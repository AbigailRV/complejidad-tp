import math

def calcular_puntaje(data, now=0, weights=(1.0, 2.0, 4.0), decay_lambda=0.01, alpha=0.001):
    likes = data.get('likes', 0)
    comentarios = data.get('comentarios', 0)
    compartidos = data.get('compartidos', 0)
    reach = data.get('reach', 0)
    age = data.get('timestamp', 0)
    raw = weights[0]*likes + weights[1]*comentarios + weights[2]*compartidos*(1 + alpha*reach)
    score = raw * math.exp(-decay_lambda * age)
    return score

def top_k_publicaciones(G, posts, k=10):
    scored = []
    for p in posts:
        score = calcular_puntaje(G.nodes[p])
        node = G.nodes[p]
        scored.append({
            'post': p,
            'score': score,
            'likes': node.get('likes',0),
            'comentarios': node.get('comentarios',0),
            'compartidos': node.get('compartidos',0),
            'reach': node.get('reach',0),
            'autor': node.get('autor','')
        })
    scored_sorted = sorted(scored, key=lambda x: x['score'], reverse=True)
    return scored_sorted[:k]

# 
"""
# **Exercícios**

  Tópicos

    Listas
    Conjuntos
    Dicionários
  

Listas

Crie uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

top_filmes = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Matrix', 'WALL·E', 'Your Name', 'Top Gun: Maverick', 'Spider-Man: Into the Spider-Verse', 'The Intouchables', 'Interstellar']
top_filmes

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.


"""

top_filmes.insert(0,'Top Gun: Maverick')
top_filmes.pop(7)
top_filmes

"""---
Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

i = 0
while i < 2:
  top_filmes.insert((9+i),'Interstellar')
  i+=1

top_filmes

"""Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado. """

set_top_filmes = list(set(top_filmes))
print(set_top_filmes)

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}`.
"""


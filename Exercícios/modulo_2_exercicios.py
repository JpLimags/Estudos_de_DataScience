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

filmes = {'filme1': {
            
              'nome': 'The Shawshank Redemption', 
              'ano': 1994, 
              'sinopse': 'Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.'
          }, 
          'filme2': {

               'nome': 'The Godfather', 
               'ano':1972, 
               'sinopse': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.'
          }, 
          'filme3': {

              'nome': 'The Dark Knight',
              'ano': 2008, 
              'sinopse': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'
          },
          'filme4':{

              'nome': 'WALL·E', 
              'ano': 2008, 
              'sinopse': 'In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.',
          },
        
          'filme5': {

             'nome': 'Your Name', 
             'ano':  2016, 
             'sinopse': 'Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?',
          },

          'filme6':{

              'nome': 'Top Gun: Maverick', 
              'ano': 2022, 
              'sinopse': 'After thirty years, Maverick is still pushing the envelope as a top naval aviator, but must confront ghosts of his past when he leads TOP GUNs elite graduates on a mission that demands the ultimate sacrifice from those chosen to fly it.',
          },
       
          'filme7': {

              'nome': 'Spider-Man: Into the Spider-Verse', 
              'ano': 2008, 
              'sinopse': 'Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.',
          },
          'filme8':{

              'nome': 'The Intouchables', 
              'ano': 2011, 
              'sinopse': 'After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.',
          },
          'filme9':{

              'nome': 'Interstellar', 
              'ano': 2014, 
              'sinopse': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.'
          },
        
          }

filmes.pop('filme1')
filmes.update({'filme_moviment': {'nome': 'The Shawshank Redemption', 
              'ano': 1994, 
              'sinopse': 'Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.'}})

print(f"Dicionário filme após a modificação:z\n{filmes}")

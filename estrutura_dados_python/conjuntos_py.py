# -*- coding: utf-8 -*-
"""conjuntos.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OigkivvQxxz7nGAH7vqFofx6FKtdv4CA

## Motivação 

- Digamos que trabalhamos como analisat de dados de mídias socas e quisessemos descobrir todas as hashtagas que alcançaram o top trending do Twitter surante uma determinada semana. Abaixo temos as hashtags por dia da semana.:
"""

hashtags_seg = ['#tiago', '#joao', "#bbb"]
hashtags_ter = ['#sarah', '#fiuk', '#bbb']
hashtags_qua = ['#giu', '#marta', '#lourdes']
hashtags_qui = ['#rafa', '#fora', '#danilo']
hashtags_sex = ['#julieta', '#matheus', '#bbb']

"""- Se fizermos uma concatenação de listas fará com que a a hashtag #bbb, e outras apareçam mais de uma vez."""

hashtag_semana = hashtags_seg + hashtags_ter + hashtags_qua  + hashtags_qui + hashtags_sex 
print(hashtag_semana)

"""### Conjuntos

- Conjuntos em python **set**, são descritas como uma estrutura de dados que implementam operações de união, intersecção e diferença assim como os conjuntos matemáticos. Os conjuntos no python não admitem repetição de elementos.
"""

frutas = {'banana', 'maca', 'uva'}

print(frutas)
print(type(frutas))

"""## Operações

- As operações da estrutura do tipo set são:
  - (diferença)

- No exemplo abaixo iremos trabalhar com alguns paises do norte da europa, vejamos: 
"""

norte_europa = {'reino unido', 'suecia', 'russia', 'noruega', 'dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}

norte_europa.difference(escandinavia)

escandinavia.difference(norte_europa)(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex)

"""## Métodos

- Os métodos aplicaveis aos conjuntos são praticamente os mesmos que são aplicaveis as listas, vejamos nos esxemplos abaixo: 
"""

cursos = {'Exatas', 'Humanas', 'Biológicas'}
print(cursos)

"""- A função `add` consegue inserir um elemento no nosso conjunto com a função.

  `set.add(val)`
"""

cursos.add('Saúde')
print(cursos)

""" - A Função `remove` remove, remove os elementos do conjunto.

  `set.remove(val)`
"""

cursos.remove()



"""## Conversão

- Conversão entre tipos de dados, abaixo iremos tranformar nosso conjunto uma lista.
"""

times_paulistas = {'São Paulo', 'Palmeiras', 'Corinthians', 'Santos'}

print(times_paulistas)
print(type(times_paulistas))

print(list(times_paulistas))
print(type(list(times_paulistas)))

"""## Revisitando a motivação



"""

print(len(hashtag_semana))

hashtags_semana = (list(set(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex)))
print(hashtags_semana)
print(len(hashtags_semana))
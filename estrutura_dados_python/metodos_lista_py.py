# -*- coding: utf-8 -*-
"""metodos_lista.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u_DX665S5UfOcgmgb4l6DrKJr5rqbIIC

### Métodos aplicaveis a listas
"""

#Criando a lista em que vamos realizar as operações

juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)

"""### Insert 

- O método insert nos permite adicionar um valor em uma posição especifica da nossa lista sem haver substituição.

  `list.insert(index,val)`
"""

juros.insert(0, 0.10)
print(juros)

"""### Append

- Sempre irá adiconar o novo valor ao final da nossa lista

  `list.append(val)`
"""

juros.append(0.09)
print(juros)

"""### Remove 

- O método `remove`, remove um item especifico pelo seu valor.

  `list.remove(value)`

"""

juros.remove(0.1)
print(juros)

"""### Pop

- Irá retirar um valor apartir do seu índice

  `list.pop(indice)`
"""

juros.pop(2)
print(juros)
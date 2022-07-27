import random
imagen = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

nombres = ['AMARANTA','ARMANDO','ESMERALDA','CAYETANO','HORTENSIA','ELEUTERIO','MAGDALENA','WILFREDO']
print('Bienvenido al juego')
print('Deberás ingresar una letra para adivinar el nombre')
seleccion = random.choice(nombres)
spaces = ["_"] * len(seleccion)
attemps = 6
while attemps > 0:
    print(imagen[attemps])
    print(' '.join(spaces))
    letra = input('Ingresa la letra: ').upper()
    if letra in seleccion:
        for i in range(len(seleccion)):
            if seleccion[i] == letra:
                spaces[i] = letra
    else:
        attemps -= 1
    if '_' not in spaces:
        print(imagen[attemps])
        print(' '.join(spaces))
        print('Ganaste')
        break
if '_' in spaces:
    print(imagen[attemps])
    print(' '.join(spaces))
    print('Perdiste')
print('Fin del juego')
print('El nombre es: ' + seleccion)
print('Gracias por jugar')
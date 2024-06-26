import random
niveles =""" Seleccione el nivel de dificultad:
            1.Fácil
            2.Media
            3.Díficil
         """
vocales= ["a","e","i","o","u"]       
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]
secret_word = random.choice(words)
max_attempts = 3
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
letters=[]
print (niveles)
nivel=int(input("Ingrese la dificultad: "))
if nivel==1:
    for letter in secret_word:
        if letter in vocales:
            guessed_letters.append(letter)
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed="".join(letters)
elif nivel==2:
    word_displayed = "_" * len(secret_word)
    word_displayed=secret_word[0:1]+word_displayed[1:]
    word_displayed=word_displayed[0:-1]+secret_word[-1]
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[-1])
elif nivel==3:
    word_displayed = "_" * len(secret_word)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")
#CODIGO
while max_attempts>0:
    letter = input("Ingresa una letra: ").lower()
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    guessed_letters.append(letter)
    if letter in secret_word and letter:
        print("¡Bien hecho! La letra está en la palabra.")
    elif letter not in secret_word and letter:
        print("Lo siento, la letra no está en la palabra.")
        max_attempts-=1
    elif not letter:
        print ("Error no ha insertardo ninguna palabra")
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
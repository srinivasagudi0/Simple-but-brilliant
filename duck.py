import random

def translate(sentence):
    if not sentence:
        return ""
    duck_sentence = ""
    for char in sentence:
        if char.isalpha():
            if random.random() < 0.5:
                duck_sentence += random.choice(["quack ", "QUACK ", "quaaaack "]) + char
            else:
                duck_sentence += char
        else:
            duck_sentence += char
    return duck_sentence.strip()

# serious mode below

def serious_translate(sentence):
    if not sentence:
        return ""
    duck_sentence = ""
    for char in sentence:
        if char.isalpha():
            duck_sentence += "QUACK! "
        else:
            duck_sentence += char
    return duck_sentence.strip()
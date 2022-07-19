def pig_it(text:str):
    finalWordList = []
    for word in text.split(" "):
        if word in ["!", "?", ",", ".", ";"]:
            finalWordList.append(word)
        else:
            wordLetters = list(word)
            wordLetters.append(wordLetters[0])
            wordLetters.remove(wordLetters[0])
            finalWordList.append("".join(wordLetters) + "ay")
    return " ".join(finalWordList)

print(pig_it('Pig latin is cool'))
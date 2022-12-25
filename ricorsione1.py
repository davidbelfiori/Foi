def downup(word):
    print(word)
    downup(word[1:])
    print(word)

downup("ciao")
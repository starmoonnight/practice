# See README.md for rules

def main():
    vowels = ['a','e','i','o','u']
    sentence=input('Translate phrase into Pig Latin:')
    sentence=sentence.split()

    for k in range(len(sentence)):
        word = sentence[k]
        if word[0] in vowels:
            sentence[k] = word + 'way'
        elif word[0] not in vowels:
            sentence[k] = word[1:] + word[0]+ 'ay'
        else:
            sentence[k] = word
    return ' '.join(sentence)
if __name__=="__main__":
    x=main()
    print(x)

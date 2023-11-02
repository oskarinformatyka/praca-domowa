def wordrand():
    from random import choice
    wordlist=['gwiazdapięcioramienna','kanapka','fortifer']
    word=choice(wordlist)
    return word

def wisielec(word):
    wordguess=len(word)*'_'
    wordguessl=list(wordguess)
    guesslist=[]
    lives=6
    while lives>0:
        if '_' not in wordguess:
            print("świetnie gratulacje")
            exit()
        print(wordguess)
        print("szanse: ",int(lives))
        guess=input('podaj jedną literę: ').lower()
        if guess not in guesslist:
            if guess in word:
                guesslist.append(guess)
                for index, i in enumerate(word):
                    if i==guess:
                        wordguessl[index]=guess
                        wordguess=''.join(wordguessl)
            elif guess not in word:
                lives-=1
                guesslist.append(guess)
        else:
            print('już to próbowałeś')

wisielec(wordrand())
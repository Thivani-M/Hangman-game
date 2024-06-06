import random
movies = ["housefull four",
          "bala"
          "chichore"
          "ujda chaman"
          "the zova factor",
          ]
name = input("Enter Name:")
print("welcome" + name)
totalturns = 7
print("So let's get started")
print("Following are the rules of the game:")
print("you will be given" + str(totalturns) + " chances to guess movie correctly")
print("if you have guessed the wrong character your turn will be deduced by 1 each time")
print("OKAY...LET'S PLAY")
print("type exit if not want to play")
q = 'y'
while True:
    choosenletters = []
    random.shuffle(movies)
    movie = orgmovie = random.choice(movies).lower()
    # choice replace with shuffle dut to repetition
    if q== "y" or q == "yes":
        turns = totalturns
        for i in movie:
            if i not in 'aeiou ':
                movie = movie.replace(i, '-')
        print('Guess movie ' + movie)
        while(turns >=1):
            guess = input('guess character:')
            guess = guess.lower()
            if(guess == 'exit'):
                exit(0)
            if guess in orgmovie:
                for x in range(0, len(movie)):
                    if orgmovie[x] == guess:
                        guessmovie = list(movie)
                        guessmovie[x] = guess
                        movie = "".join(guessmovie)
            else:
                if guess in choosenletters:
                    print("This letter already choosen. Try another one.")
                    continue
                choosenletters.append(guess)
                turns -= 1
                print("Turn chance Remains : " + str(turns))
            print(movie)
            if(movie == orgmovie):
                print('You Won!!!')
                break
        if(turns == 0):
            print('Better  Luck Next Time!!')
            print('Correct Word is : ' + orgmovie.upper())
    q = input("wanna play hangman again?")
    q = q.lower()
    if(q != 'y' and q != 'yes'):
        break
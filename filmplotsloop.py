import random
loop = True
print("Welcome to the movie plot generator! Let's put you in a movie!")
while loop == True:
    plot = str(input("First of all: Who is directing your movie? Type W for Wes Anderson, T for Tarantino, M for Michael Schur, L for Lynch.\n"))
    if plot == "W" or plot == "w":
        firstName = str(input("What's your first name? "))
        lastName = str(input("What's your family name? "))
        animal = str(input("What type of quirky pet will be your companion? "))
        favourite = str(input("Name a favourite musician. "))
        homeTown = str(input("What's your hometown? "))
        country = str(input("Name a place you haven't been to, but want to visit. "))
        sport = str(input("Name a sport. "))
        adjective = str(input("What's an adjective you wish described you? "))
        music = str(input("What's your favourite instrument? "))
        firstNameS = firstName + "s"
        lastNameS = lastName + "s"
        print("\n")
        print("Wes Anderson presents: The Wondrous Adventures of",firstName,lastName)
        print("The story of",firstName,lastName,", and the ",animal," ",favourite,".")
        print("Together they will embark on the adventure of their lifetime, travelling from",homeTown,"to the mysterious land of",country,"to uncover",firstNameS,"hidden family secret.")
        print("During their adventures, the dynamic duo will have to use ",firstNameS,sport,"skills to fight the",lastNameS,"archenemies, and learn how to be",adjective,".")
        print("The movie will release at TIFF, featuring a select score of pure",music,"covers of Simon and Garfunkel songs in Latvian.")
    elif plot == "T" or plot == "t":
        character = str(input("What's your full name? "))
        time = str(input("What's your favourite time period? (eg. the 80s, the 1900-s..) "))
        enemy = str(input("Name a person you hate. "))
        weapon = str(input("Name a weapon. "))
        country = str(input("What country are you from? "))
        wife = str(input("Name a hot actress. "))
        colour = str(input("What's your favourite colour? "))
        rebel = colour + "s"
        flower = str(input("What's your favourite flower? "))
        actor = str(input("Name one of your parents favourite actors over 50. "))
        hist = str(input("What's your favourite historical figure? "))
        print("\n")
        print("Tarantino presents: The",enemy,"Killer") 
        print("The wild almost-true story of",character,". \n A ",weapon.lower(),"wielding rebel from",time,"out for revenge against",enemy,"for murdering the leader of the rebel group, The",rebel,".")
        print("Follow this gory adventure, as",character,"has to stand ground to protect",country,"from",enemy,"with the help of the kickass",flower,"Hunter, played by",wife,".")
        print("The movie will be out in cinemas worldwide and feature",actor,"in a groundbreaking performance as",hist)
    elif plot == "M" or plot == "m":
        firstName = str(input("What's your full name? "))
        firstNameS = firstName + "s"
        friends = (input("How many close friends would you say you have? "))
        bf = str(input("What's the name of your best friend? "))
        crush = str(input("Whos your celebrity crush? "))
        workplace = str(input("Name a stereotypical workplace? (eg. school, reception, etc.) "))
        cameo = str(input("Whose your celebrity idol? "))
        prank1 = False
        prank2 = False
        prank3 = False
        prankuser1 = str(input("Would you ever clingfilm someone's car? Type Y for yes, N for no. "))
        if prankuser1 == "Y" or "y":
            prank1 = True
        elif prankuser1 == "N" or "n":
            prankuser2 = str(input("Would you ever put someone's stapler in jelly? Type Y for yes, N for no. "))
            if prankuser2 == "Y" or "y":
                prank2 = True
            else:
                prank3 = True
        boss = str(input("Write the full name of a parent/parent figure in your life. "))
        city = str(input("What's the nearest big city near you? "))
        workadj = str(input("What adjective would your boss use about you? "))
        leisadj = str(input("What adjective would your friends use about you? "))
        buzz = str(input("Name a corporate buzzword adjective. "))
        workname = str(input("Name the last name of a scientist. "))
        print("\n")
        print("Michael Schur presents: The",workplace)
        print("Meet ",firstName,". A",workadj,",",leisadj,"worker-bee at The",workname,workplace,"in downtown",city,".")
        print(firstName,"is the average person, working with their",friends,"closest friends and their crush, played by",crush,",\n while constantly negotiating with their dry and bureaucratic boss",boss,", who wants the",workplace.lower(),"to be more",buzz,".")
        if prank1 == True:
            print("Watch the pilot episode, as",bf,", ",firstNameS,"best friend, \n wakes up to see their car parked outside the",workplace.lower(),"clingfilmed, right before an important meeting!")
        elif prank2 == True:
            print("Watch the pilot episode, as",bf,", ",firstNameS,"best friend, \n comes to work, only to find their stapler suspended in jelly, right before having to hand in an importan report!")
        elif prank3 == True:
            print("Watch the pilot episode, as",bf,", ",firstNameS,"best friend, \n comes to work, only to open a letter that turns out to be a glitterbomb, right before an important meeting!")
        print("The episode will be out on Netflix next summer, and feature a cameo from",cameo,"as the substitute postman.")
    elif plot == "L" or plot == "l":
        firstName = str(input("What's your first initial? "))
        homeTown = str(input("What's your hometown? "))
        town = str(input("Describe your town in one adjective. "))
        glam = str(input("Name a glamorous job you wish you had. (eg. actor) "))
        animal = str(input("Name a group of animals. "))
        actress = str(input("Name a hot actress over 40: "))
        singer = str(input("Name your favourite singer? "))
        colour = str(input("What's your favourite colour? "))
        drink = str(input("Name a drink? "))
        drinks = drink + "s"
        electric = str(input("Name an electrical device. "))
        lullabye = str(input("Your favourite lullabye? "))
        adj = str(input("Describe your dreams in one adjective? "))
        noun = str(input("Name a noun you have dreamt about. "))
        death = str(input("Name someone annoying from your old school class. "))
        nounL = list(noun)
        random.shuffle(nounL)
        title = ""
        for x in nounL:
            title = title + x.lower()
        print("\n")
        print("David Lynch presents:",title)
        print(homeTown,"is shaken after",death,"is found dead with the note",title,"and the attention has turned towards the",town,"town and it's inhabitants.")
        print(firstName,"is simply visiting family for the weekend, not excited to go back and confront old memories.")
        print("But the",electric,"keeps making odd humming noises, and the retired",glam.lower(),", Mrs.",colour,"who is played by",actress,", who is always found in the bars at daytime, \n sipping",drinks,", seems to be watching you.")
        print("Simultaneously,", firstName,"keeps dreaming of",animal.lower(),"singing",lullabye,". The",adj.lower(),"film will premier at Cannes and feature a score composed by Lynch and performed by him and",singer)
        print("\n")
    answer = input("Run again? Type Y for yes or N for no: ")
    if answer != "Y" or "y":
        loop = False
        break
        print("\n")
    if answer == "Y" or "y":
        loop = True
        continue


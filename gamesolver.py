def gettingCards():
    print("Please put the number for the corresponding card in your deck")
    print("1: Bridge")
    print("2: River")
    print("3: Lake")
    print("4: Village")
    print("5: Mountain")
    print("6: Beach")
    print("7: Jungle")
    print("8: Reef")
    print("9: Volcano")
    print("10: Field")
    # Our default player card sets
    """player1 = [4,3,9,3,5,1,5,2,10,7]
    player2 = [2,10,5,8,7,6,6,4,8,2]
    player3 = [7,9,9,3,1,10,8,5,5,2]
    player4 = [1,6,4,3,4,8,7,9,8,9]
    player5 = [1,1,2,3,4,6,6,7,10,10]"""
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    player5 = []
    for i in range(5):
        print("For Player " + str(i+1) + ": ")
        for j in range(10):
            toAppend = input("Enter Card Number " + str(j+1) + ": ")
            if (i == 0):
                player1.append(int(toAppend))
            elif (i == 1):
                player2.append(int(toAppend))
            elif (i == 2):
                player3.append(int(toAppend))
            elif (i == 3):
                player4.append(int(toAppend))
            else:
                player5.append(int(toAppend))
    mapscore(player1, player2, player3, player4, player5)
    

def mapscore(p1, p2, p3, p4, p5):
    playerScores = [0, 0, 0, 0, 0]
    p1cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p2cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p3cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p4cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p5cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 6):
        if (i == 1):
            for elements in p1:
                p1cards[elements - 1] += 1
        elif (i == 2):
            for elements in p2:
                p2cards[elements - 1] += 1
        elif (i == 3):
            for elements in p3:
                p3cards[elements - 1] += 1
        elif (i == 4):
            for elements in p4:
                p4cards[elements - 1] += 1
        elif (i == 5):
            for elements in p5:
                p5cards[elements - 1] += 1
    playerScores[0] = calculateScore(p1cards, p2cards, p3cards, p4cards, p5cards)
    playerScores[1] = calculateScore(p2cards, p1cards, p3cards, p4cards, p5cards)
    playerScores[2] = calculateScore(p3cards, p2cards, p1cards, p4cards, p5cards)
    playerScores[3] = calculateScore(p4cards, p2cards, p3cards, p1cards, p5cards)
    playerScores[4] = calculateScore(p5cards, p2cards, p3cards, p4cards, p1cards)
    for i in range(1,6):
        print("Player " + str(i) + "'s Score is: " + str(playerScores[i-1]))
    
        

def calculateScore(cards, other1, other2, other3, other4):
    score = 0
    # Bridges
    if cards[0] != 0:
        for elements in cards:
            if elements != 0:
                score += 1

    # River
    riverpts = cards[1] - cards[2]
    if riverpts > 0:
        score -= (riverpts * 2)

    # Lake
    if (cards[2] >= 1 and cards[1] >= 1):
        lakepts = cards[2] - cards[1]
        score += (cards[2] - lakepts) * 4

    # Village
    if (cards[3] == 1):
        score += 1
    elif (cards[3] == 2):    
        score += 3
    elif (cards[3] == 3):
        score -= 6
    elif (cards[3] == 4):
        score += 10
    elif (cards[3] == 5):
        score -= 15
    # Mountain
    if (cards[4] == 3):
        score += 10
    # Beach
    if (cards[5] == 2):
        score += 6
    # Jungle
    jgCountArray = [cards[6], other1[6], other2[6], other3[6], other4[6]]
    noDupes = list(set(jgCountArray))
    noDupes.sort(reverse = True)
    try:
        if (cards[6] == noDupes[1]):
            score += 4
    except:
        score += 0
    # Reef
    score += (cards[7] * cards[3])
    # Volcano
    if (cards[8] > cards[4]):
        cards[8] = cards[4]
    score += (cards[8] * cards[9] * 3)
    score -= (cards[8] * cards[3] * 2)
    # Field
    score += (cards[9] * 3)
    return score   

gettingCards()

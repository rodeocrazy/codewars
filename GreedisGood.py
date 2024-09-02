def score(dice):
    score = 0

    if dice.count(1) == 3:
        score += 1000
    if dice.count(1) == 4:
        score += 1100
    if dice.count(1) == 5:
        score += 1200
    
    if dice.count(6) == 3:
        score += 600


    if dice.count(5) == 3:
        score += 500
    if dice.count(5) == 4:
        score += 550
    if dice.count(5) == 5:
        score += 600
    
    if dice.count(4) == 3:
        score += 400

    if dice.count(3) == 3:
        score += 300

    if dice.count(2) == 3:
        score += 200

    if dice.count(1) == 1:
        score += 100
    if dice.count(5) == 1:
        score += 50

    return score
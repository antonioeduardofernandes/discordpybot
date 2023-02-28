import random

def baseRoll(pool,difficulty, specialization=False, vontade=False, modifiers=0):
    finalResult = ""
    successes = 0 if not vontade else 1
    baseResults = []
    specializationResults = []
    modifiers = modifiers
    if not modifiers:
        modifiers = 0

    for n in range(pool):
        dice = random.randint(1,10)
        baseResults.append(dice)
        if specialization:
            while dice==10:
                dice = random.randint(1,10)
                specializationResults.append(dice)

    for d in baseResults:
       if(d>=difficulty):
           successes +=1
       if d==1:
           successes -=1

    for d in specializationResults:
       if(d>=difficulty):
           successes +=1
       if d==1:
           successes -=1

    if successes < 0:
        finalResult = "falha crítica"
    if successes == 0:
        finalResult = "falha"
    if successes > 0:
        finalResult = "sucesso"

    d = dict()

    # return pool
    return pool, difficulty, baseResults, specializationResults, successes, finalResult
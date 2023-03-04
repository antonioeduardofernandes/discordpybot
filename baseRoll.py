import random
import discord

########################################### 
# ROLAGEM
###########################################

def baseRoll(pool,difficulty, specialization, will, modifiers, type, magikal={},title="", description="", thumbnail=""):
    finalResult = ""
    successes = 0 if not will else 1
    baseResults = []
    specializationResults = []
    modifiers = modifiers if modifiers else 0
    difficulty = difficulty + modifiers

    for n in range(pool):
        dice = random.randint(1,10)
        baseResults.append(dice)
        if specialization:
            while dice==10:
                dice = random.randint(1,10)
                specializationResults.append(dice)

    for r in baseResults:
       if(r>=difficulty):
           successes +=1
       if r==1:
           successes -=1

    for r in specializationResults:
       if(r>=difficulty):
           successes +=1
       if r==1:
           successes -=1

    if successes < 0:
        finalResult = "falha crítica"
    if successes == 0:
        finalResult = "falha"
    if successes > 0:
        finalResult = "sucesso"


########################################### 
# DISPLAY NO CHAT
###########################################

    title = title or "Rolagem Simples"
    if(type=='magika'):
            title = "Rolagem para efeitos magikos"

    description = description or "Realiza uma rolagem de dados genérica"
    thumbnail = thumbnail or "https://pbs.twimg.com/profile_images/982348786465820672/gE7nG5Df_400x400.jpg"

    if(type=='magika'):
        higher_sphere = magikal['higher_sphere']
        quintessence = magikal['quintessence']
        environment = magikal['environment']
  
        paradox = 0
        if(not finalResult == "falha crítica"):
            if(environment == "vulgar" or environment == "vulgar com testemunhas"):
                paradox = 1
        if(finalResult == "falha crítica"):
            if(environment == "coincidente"):
                paradox = higher_sphere
            if(environment == "vulgar com testemunhas"):
                paradox = 1 + higher_sphere
            if(environment == "vulgar com testemunhas"):
                paradox = 2 + (higher_sphere*2)

    embed = discord.Embed(title=f"{title}", description=f"*{description}*", color=discord.Color.blurple())
    embed.set_thumbnail(url=f"{thumbnail}")
    embed.add_field(name="Parada de Dados:", value=f'{pool}d10')
    embed.add_field(name="Dificuldade:", value=difficulty)
    embed.add_field(name="Resultados:", value=f'{" - ".join(str(x) for x in baseResults)}')
    embed.add_field(name="Especialização:", value=f'{"Não possui" if not specialization else " - ".join((str(x) for x in specializationResults))}')
    if(type=='magika'):
        embed.add_field(name="Ambiente da mágika:", value=environment)
        embed.add_field(name="Paradoxo:", value=f'{paradox}')
        embed.add_field(name="Quintessêcia:", value=f'{quintessence}')
    embed.add_field(name="Gasto de Força de Vontade:", value=f'{"Sim" if will else "Não"}')
    embed.add_field(name="Sucessos Obtidos:", value=successes, inline=False)
    embed.add_field(name="A ação resultou em:", value=f'{finalResult.capitalize()}', inline=True)

    return embed

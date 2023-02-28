import discord
import os
from baseRoll import baseRoll
from utils import displayScore
from pysondb import db

database = db.getDb("database.json")

from dotenv import load_dotenv
load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} is ready and online!')

#########################
# commands
########################


# rolagem basica de dados
@bot.command(name="rolagem", description="Rolagem basica")
async def roll(ctx, dados: discord.Option(int, required=True, description="Quantidade de dados da parada:", min_value=1), 
               dificuldade:discord.Option(int,required=True, description="Dificuldade da Rolagem",max_value=10), 
               especializacao: discord.Option(bool, description="Possui especialização na rolagem?"),
               vontade:discord.Option(bool, required=False, description="Deseja gastar 1 ponto de Força de Vontade?"), 
               modificadores:discord.Option(int, required=False, description="Outros modificadores aplicáveis")):
    # realiza a rolagem base
    if not modificadores: modificadores = 0
    pool, difficulty, baseResults, specializationResults, successes, finalResult = baseRoll(dados,dificuldade,especializacao, vontade, modificadores or 0)

    # resultado a ser apresentado no chat
    embed = discord.Embed(title="Rolagem Simples", description="*Realiza uma rolagem de dados genérica*", color=discord.Color.blurple())
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/982348786465820672/gE7nG5Df_400x400.jpg")
    embed.add_field(name="Parada de Dados:", value=f'{pool}d10')
    embed.add_field(name="Dificuldade:", value=difficulty)
    embed.add_field(name="Resultados:", value=f'{" - ".join(str(x) for x in baseResults)}')
    embed.add_field(name="Especialização:", value=f'{"Não possui" if not especializacao else " - ".join((str(x) for x in specializationResults))}')
    embed.add_field(name="Sucessos Obtidos:", value=successes)
    embed.add_field(name="Gasto de Força de Vontade:", value=f'{"Sim" if vontade else "Não"}')
    embed.add_field(name="A ação resultou em:", value=f'{finalResult.capitalize()}')

    await ctx.respond("Ok", embed=embed)


# rolagem de efeitos magikos
@bot.command(name="magika", description="Rolagem para efeitos magikos")
async def magika(ctx, arete:discord.Option(int,required=True, description="Seu nível de Arete", min_value=1, max_value=10), 
                 esfera: discord.Option(int,min_value=1, max_value=5, required=True, description="Nível na esfera mais alta do efeito:"), 
                 ambiente:discord.Option(str,required=True, description="Em que condições a mágika está sendo realizada", choices=["coincidente","vulgar sem testemunhas", "vulgar com testemunhas"]),
                 especializacao: discord.Option(bool, description="Possui especialização na rolagem?"),
                 vontade:discord.Option(bool,required=False, description="Deseja gastar 1 ponto de Força de Vontade?"), 
                 quintessencia:discord.Option(int, required=False, description="Quantos pontos de quintessência deseja gastar para reduzir a dificuldade do efeito mágiko? (máx.3)", max_value=3),
                 modificadores:discord.Option(int, description="Outros modificadores aplicáveis", required=False)):
    
    if(ambiente == "coincidente"): dificuldade = 3 + esfera
    if(ambiente == "vulgar sem testemunhas"): dificuldade = 4 + esfera
    if(ambiente == "vulgar com testemunhas"): dificuldade = 5 + esfera
    if not quintessencia: quintessencia = 0
    
    # realiza a rolagem base
    pool, difficulty, baseResults, specializationResults, successes, finalResult = baseRoll(arete,dificuldade-quintessencia,especializacao, vontade, modificadores)

    paradoxo = 0
    if(not finalResult == "falha crítica"):
        if(ambiente == "vulgar" or ambiente == "vulgar com testemunhas"):
            paradoxo = 1
    if(finalResult == "falha crítica"):
        if(ambiente == "coincidente"):
            paradoxo = esfera
        if(ambiente == "vulgar com testemunhas"):
            paradoxo = 1 + esfera
        if(ambiente == "vulgar com testemunhas"):
            paradoxo = 2 + (esfera*2)
        

    # resultado a ser apresentado no chat
    embed = discord.Embed(title="Rolagem para efeitos magikos", description="", color=discord.Color.blurple())
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/982348786465820672/gE7nG5Df_400x400.jpg")
    embed.add_field(name="Parada de Dados:", value=f'{pool}d10')
    embed.add_field(name="Esfera mais alta utilizada na mágika:", value=esfera)
    embed.add_field(name="Ambiente em que a mágika é realizada:", value=ambiente)
    embed.add_field(name="Dificuldade:", value=difficulty)
    embed.add_field(name="Resultados:", value=f'{" - ".join(str(x) for x in baseResults)}')
    embed.add_field(name="Especialização:", value=f'{"Não possui" if not especializacao else " - ".join((str(x) for x in specializationResults))}')
    embed.add_field(name="Sucesssos obtidos:", value=f'{successes}')
    embed.add_field(name="Gasto de Força de Vontade:", value=f'{"Sim" if vontade else "Não"}')
    embed.add_field(name="Paradoxo recebido:", value=f'{paradoxo}')
    embed.add_field(name="A ação resultou em:", value=f'{finalResult.capitalize()}')
    
    await ctx.respond("", embed=embed)


@bot.command(name="ficha", description="Ficha de Personagem")
async def sheet(ctx):

    # caso eu seja o autor do comando, iterar pelos dados para inserir o nome dinamicamente como opcao no select
    if(ctx.author.id == 448079899056406529):
        dynamic_options = []
        for character in database.getAll():
            name = character["nome"]
            item = discord.SelectOption(label=name)
            dynamic_options.append(item)

        class MyView(discord.ui.View):
            @discord.ui.select(placeholder="Selecione", options=dynamic_options)
            async def select_callback(self, select, interaction):
                selected_character = database.getByQuery({'nome':select.values[0]})[0]
                embed = discord.Embed(title=f"nome", description="Tradicao", color=discord.Color.blurple())
                embed.set_thumbnail(url=f"{selected_character['img']}")
                await interaction.response.send_message("", embed=embed)
        await ctx.send("", view=MyView())
    else:
    # caso o autor do comando nao seja eu, capturar o personagem pelo id do autor
        selected_character = database.getByQuery({'jogador':str(ctx.author.id)})[0]
        await ctx.send("aqui ja com embed") 
        

    # embed = discord.Embed(title=f"nome", description="Tradicao", color=discord.Color.blurple())
    # embed.set_thumbnail(url=f"{selected_character['img']}")
    # embed.add_field(name="_Natureza e Comportamento_",value="", inline=False)
    # embed.add_field(name="**Atributos**",value="-----------------------------------------------------------------------", inline=False)
    # embed.add_field(name=f"Forca {displayScore(4)}", value="")
    # embed.add_field(name=f"Destreza {displayScore(2)}", value="")
    # embed.add_field(name=f"Vigor {displayScore(1)}", value="")
    # embed.add_field(name=f"Carisma {displayScore(3)}", value="")
    # embed.add_field(name=f"Manipulacao {displayScore(2)}", value="")
    # embed.add_field(name=f"Aparencia {displayScore(1)}", value="")
    # embed.add_field(name=f"Percepcao {displayScore(3)}", value="")
    # embed.add_field(name=f"Inteligencia {displayScore(2)}", value="")
    # embed.add_field(name=f"Raciocinio {displayScore(2)}", value="")
    # embed.add_field(name="Pericias",value=f"Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} \n Habilidade {displayScore(3)} ")
    
    # await ctx.respond("", embed=embed) 











# connect bot to server with token provided
bot.run(os.getenv('TOKEN'))
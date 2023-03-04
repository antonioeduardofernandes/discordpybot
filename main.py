import discord
import os
from pysondb import db

from baseRoll import baseRoll
from generateSheetEmbed import generateEmbed

from updateCharacterValues import update_character_value
from vitalityUtils import apply_damage, heal
from labels import atributos, físicos, mentais, sociais, perícias, talentos, conhecimentos


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

#########################
# UTILS
########################

# captura o personagem pelo ID do usuário ou uma lista com todos os personagens
async def get_character(ctx:discord.AutocompleteContext):
    character_list = []
    character = database.getByQuery({'jogador':str(ctx.interaction.user.id)})
    if(bool(character)):
        character_list.append(character[0]["nome"])
        return character_list
    else:
        for character in database.getAll():
            name = character["nome"]
            character_list.append(name)
        return character_list


async def get_skill(ctx:discord.AutocompleteContext):
    skill_group = ctx.options['habilidades']
    if skill_group == "perícias":
        return sorted(perícias)
    elif skill_group == "talentos":
        return sorted(talentos)
    elif skill_group == "conhecimentos":
        return sorted(conhecimentos)

#verifica se o mestre esta logado para permitir certos comandos
async def is_GM_logged():
    global bot
    guild = bot.get_guild(1077019048182829289)
    if (guild.get_member(448079899056406529)):
        return True
    else:
        return False



#########################
# FICHA
########################

@bot.command(name="ficha", description="Apresenta a ficha de personagem")
async def sheet(ctx, personagem=discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_character))):        
    character_data = database.getByQuery({'nome':personagem})[0]
    await ctx.respond("", embed=generateEmbed(character_data))

# teste de atributo + pericia
@bot.command(name="teste")
async def test(
    ctx:discord.ApplicationContext, 
    personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)), 
    atributo:discord.Option(str, choices=atributos), 
    habilidades:discord.Option(str, choices=["talentos", "perícias", "conhecimentos"]),
    habilidade:discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_skill)),
    dificuldade:discord.Option(int,required=True, description="Dificuldade da Rolagem",max_value=10), 
    especializacao: discord.Option(bool,required=False, description="Possui especialização na rolagem?"),
    vontade:discord.Option(bool, required=False, description="Deseja gastar 1 ponto de Força de Vontade?"), 
    modificadores:discord.Option(int, required=False, description="Outros modificadores aplicáveis")
    ):

 # realiza a rolagem base
    character_data = database.getByQuery({'nome':personagem})[0]

    for group in character_data["atributos"]:
        for k in character_data["atributos"][group]:
            if(k["label"] == atributo):
                attribute_value = k['valor']

    for group in character_data["habilidades"]:
        for k in character_data["habilidades"][group]:
            if(k["label"] == habilidade):
               skill_value = k['valor']

    dice_pool = attribute_value + skill_value

    # gasta vontade

    # verifica penalidade de vitalidade

    if not modificadores: modificadores = 0
    embed = baseRoll(pool = dice_pool,
                     difficulty = dificuldade,
                     specialization = especializacao, 
                     will = vontade, 
                     modifiers = modificadores, 
                     type="", 
                     title=character_data["nome"].capitalize(), 
                     description=f"{atributo.capitalize()} + {habilidade.capitalize()}",
                     thumbnail=character_data["img"]
                     )
    await ctx.respond("", embed=embed)

# rolagem de efeitos magikos
class SpheresSelectionView(discord.ui.View):
    def __init__(self, personagem, ambiente, especializacao, vontade, quintessencia, modificadores):
        super().__init__()
        self.personagem = personagem
        self.ambiente = ambiente
        self.especializacao = especializacao
        self.vontade = vontade
        self.quintessencia = quintessencia
        self.modificadores = modificadores
    @discord.ui.select(
        placeholder="Selecione as esferas do efeito",
        min_values=1,
        max_values=9,
        options = [
        discord.SelectOption(label="correspondência"),
        discord.SelectOption(label="entropia"),
        discord.SelectOption(label="forças"),
        discord.SelectOption(label="vida"),
        discord.SelectOption(label="mente"),
        discord.SelectOption(label="matéria"),
        discord.SelectOption(label="primórdio"),
        discord.SelectOption(label="espírito"),
        discord.SelectOption(label="tempo"),
        ]
    )
    async def select_callback(self, select, interaction):
        character_data = database.getByQuery({'nome':self.personagem})[0]
        valores_das_esferas = [] 

        for esfera in character_data["esferas"]:
            if(esfera['label'] in select.values):
                valores_das_esferas.append(esfera['valor'])
        
        esfera_mais_alta = max(valores_das_esferas)

        if(self.ambiente == "coincidente"): self.dificuldade = 3 + esfera_mais_alta
        elif(self.ambiente == "vulgar sem testemunhas"): self.dificuldade = 4 + esfera_mais_alta
        elif(self.ambiente == "vulgar com testemunhas"): self.dificuldade = 5 + esfera_mais_alta
        
        if not self.quintessencia: quintessencia = 0
        dificuldade = self.dificuldade - quintessencia
        arete = character_data['arete']
        embed = baseRoll(
            title = self.personagem.capitalize(),
            description=f"Esferas utilizadas: {', '.join(select.values)}",
            thumbnail=character_data["img"],
            pool = arete,
            difficulty = dificuldade,
            specialization = self.especializacao, 
            will = self.vontade, 
            modifiers = self.modificadores, 
            type="magika",
            magikal={'higher_sphere':esfera_mais_alta, 'environment':self.ambiente, 'quintessence':self.quintessencia})
        
        await interaction.response.send_message("", embed=embed)
        
        # realiza a rolagem base

@bot.command(name="magika", description="Rolagem para efeitos magikos")
async def magika(ctx,
                 personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)),  
                 ambiente:discord.Option(str,required=True, description="Em que condições a mágika está sendo realizada", choices=["coincidente","vulgar sem testemunhas", "vulgar com testemunhas"]),
                 especializacao: discord.Option(bool,required=False, description="Possui especialização na rolagem?"),
                 vontade:discord.Option(bool,required=False, description="Deseja gastar 1 ponto de Força de Vontade?"), 
                 quintessencia:discord.Option(int, required=False, description="Quantos pontos de quintessência deseja gastar para reduzir a dificuldade do efeito mágiko? (máx.3)", max_value=3),
                 modificadores:discord.Option(int, description="Outros modificadores aplicáveis", required=False)):
    view = SpheresSelectionView(personagem, ambiente, especializacao, vontade, quintessencia, modificadores)
    await ctx.send("", view=view)


#########################
# EDIÇÃO
########################

@bot.command(name="editar")
async def edit(ctx:discord.ApplicationContext, 
               personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)), 
               parametro:discord.Option(str,required=True, choices=['força de vontade', 'quintessência', 'paradoxo']), 
               valor:discord.Option(int, required=True)):
    newValue = update_character_value(character_name=personagem, parameter=parametro, value=valor)
    await ctx.respond(f"{personagem}: seu valor atual de {parametro} agora é {newValue}")


@bot.command(name="vontade")
async def will(ctx:discord.ApplicationContext, 
               personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)), 
               valor:discord.Option(int, required=True)):
    newValue, temporario = update_character_value(character_name=personagem, parameter="força de vontade", value=valor)
    
    if newValue != temporario:
        await ctx.respond(f"{personagem.capitalize()}: sua força de vontade agora é {newValue}")
    else:
        await ctx.respond(f"{personagem.capitalize()}: seu valor atual de vontade permanece {temporario}")


@bot.command(name="quintessencia")
async def quintessence(ctx:discord.ApplicationContext, 
               personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)), 
               valor:discord.Option(int, required=True)):
    newValue = update_character_value(character_name=personagem, parameter="quintessência", value=valor)
    await ctx.respond(f"{personagem}: seu valor atual de quintessência agora é {newValue}")


@bot.command(name="paradoxo")
async def paradox(ctx:discord.ApplicationContext, 
               personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)), 
               valor:discord.Option(int, required=True)):
    newValue = update_character_value(character_name=personagem, parameter="paradoxo", value=valor)
    await ctx.respond(f"{personagem}: seu valor atual de paradoxo agora é {newValue}")


@bot.command(name="dano", description="Aplica dano ao personagem selecionado")
async def damage(ctx,
                 personagem:discord.Option(str,required=True, autocomplete=discord.utils.basic_autocomplete(get_character)),  
                 tipo:discord.Option(str, description="Tipo de dano",choices=['agravado', 'letal', 'contusão'], required=True),
                 dano:discord.Option(int, description="Valor do dano", required=True)):
    
    character_data = database.getByQuery({'nome':personagem})[0]
    dead = apply_damage(character=character_data, type=tipo, amount=dano)
    if not dead:
        await ctx.respond(f"{personagem.capitalize()} sofreu {dano} de dano {tipo}")
    else:
        await ctx.respond(f"{personagem.capitalize()} sofreu {dano} de dano {tipo}. Dano suficiente para morrer...")


@bot.command(name="cura", description="Cura ferimentos do personagem")
async def healing(ctx, personagem:discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_character)), valor:discord.Option(int, description="Pontos de vitalidade a serem curados", required=True) ):
    character_data = database.getByQuery({'nome':personagem})[0]
    healed = heal(character=character_data, amount=valor)
    if healed:
        await ctx.respond(f"{personagem.capitalize()} curou {valor} pontos de vitalidade")
    else:
        await ctx.respond(f"{personagem.capitalize()} não possui dano para curar")
        

#########################
# GERAIS
########################

@bot.command(name="xp", description="Atribui pontos de experiência")
async def experience(ctx:discord.ApplicationContext, 
               valor:discord.Option(int,min_value=1, required=True)):
    if ctx.author.id != 448079899056406529:
        await ctx.respond(f"Você não tem permissão para rodar este comando")
        return
    else:
        character_list = []
        for character in database.getAll():
            current_xp = character['experiência']
            new_xp = valor + current_xp
            database.updateByQuery({"nome": character['nome']}, {"experiência":new_xp})
            character_list.append(character['nome'].capitalize())
        await ctx.respond(f" {', '.join(character_list)} receberam {valor} de experiência")
        

@bot.command(name="ajuda", description="Exibe os comandos possíveis para o bot")
async def help(ctx):
    embed = discord.Embed(title=f"Comandos de ajuda", color=discord.Color.blurple())
    embed.set_thumbnail(url="https://rb.gy/vg9hre")
    embed.add_field(name=f"Personagem:", value="**`/ficha`:** Exibe a ficha do personagem.\n **`/teste`:** Realiza um teste de perícia + atributo.\n **`/magika`:** Realiza uma rolagem de magika a partir da ficha do personagem. \n **`/quintessencia`:** Edita os valores de quintessencia na ficha.\n **`/vontade`:** Edita os valores de força de vontade na ficha.\n **`/paradoxo`:** Edita os valores de paradoxo na ficha.", inline=False)
    embed.add_field(name=f"Vitalidade:", value="**`/dano`:** Aplica dano à vitalidade do personagem.\n **`/cura`:** Cura pontos de vitalidade perdidos.\n\n", inline=False)
    embed.add_field(name=f"Gerais:", value="**`/rolagem`:** Realiza uma rolagem genérica.\n **`/efeito`:** Realiza uma rolagem magika genérica.\n ", inline=False)
    await ctx.respond("", embed=embed)



# TODO - aplicar gasto de quintessencia, paradoxo e vontade na rolagem mágika direto na ficha do personagem
# TODO - alterar no comando de teste de perícia para aplicar penalidade por dano recebido e poder anular com gasto de força de vontade





# connect bot to server with token provided
bot.run(os.getenv('TOKEN'))
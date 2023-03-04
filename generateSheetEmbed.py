import discord
from vitalityUtils import display_vitality

displayScore = lambda score:"●"*score

def generateEmbed(selected_character):
    fisicos = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor'])) + " " + (a['especializacao']),selected_character['atributos']['físicos']))) 
    sociais = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['atributos']['sociais']))) 
    mentais = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['atributos']['mentais']))) 
    talentos = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['habilidades']['talentos']))) 
    pericias = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['habilidades']['perícias']))) 
    conhecimentos = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['habilidades']['conhecimentos']))) 
    esferas = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor']))+ " " + (a['especializacao']),selected_character['esferas']))) 
    antecedentes = "\n".join(list(map(lambda a:a['label'].capitalize() + " " + str(displayScore(a['valor'])),selected_character['antecedentes'])))
    vontade_permanente = selected_character['vontade']['permanente']
    vontade_temporaria = selected_character['vontade']['temporario']

    embed = discord.Embed(title=f"{selected_character['nome']}", color=discord.Color.blurple())
    embed.set_thumbnail(url=f"{selected_character['img']}")
    embed.add_field(name=f"_Tradição: {selected_character['tradicao']}\t Essência: {selected_character['essencia']}_",value="", inline=False)
    embed.add_field(name=f"_Natureza: {selected_character['natureza']} \t Comportamento: {selected_character['comportamento']}_",value="", inline=False)
    embed.add_field(name="**Atributos**",value="-----------------------------------------------------------------------", inline=False)
    embed.add_field(name=f"{fisicos}", value="")
    embed.add_field(name=f"{sociais}", value="")
    embed.add_field(name=f"{mentais}", value="")
    embed.add_field(name="**Habilidades**",value="-----------------------------------------------------------------------", inline=False)
    embed.add_field(name=f"{talentos}", value="")
    embed.add_field(name=f"{pericias}", value="")
    embed.add_field(name=f"{conhecimentos}", value="")
    embed.add_field(name="**Vantagens**",value="-----------------------------------------------------------------------", inline=False)
    embed.add_field(name=f"{antecedentes}", value="")
    embed.add_field(name="**Esferas**",value="-----------------------------------------------------------------------", inline=False)
    embed.add_field(name=f"{esferas}", value="")
    embed.add_field(name=f"Arete: {selected_character['arete']}",value="", inline=False)
    embed.add_field(name=f"Força de Vontade: {vontade_permanente}/{vontade_temporaria}",value="", inline=False)
    embed.add_field(name=f"Quintessência: {selected_character['quintessencia']}",value="", inline=False)
    embed.add_field(name=f"Paradoxo: {selected_character['paradoxo']}",value="", inline=False)
    embed.add_field(name="Vitalidade:",value=display_vitality(selected_character), inline=False)

    return embed
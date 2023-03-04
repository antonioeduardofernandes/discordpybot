from pysondb import db
database = db.getDb("database.json")


def update_character_value(character_name, parameter, value):
	character_data = database.getByQuery({'nome':character_name})[0]

	if parameter == "força de vontade":
		permanente = character_data['vontade']['permanente']
		temporario = character_data['vontade']['temporario']
		if((temporario + value) >= permanente):
			newValue = permanente
		elif(temporario + value < 0):
			newValue = 0
		else:
			newValue = temporario + value
		database.updateByQuery({"nome": character_name}, {"vontade":{'permanente':permanente, 'temporario':newValue}})
		return newValue, temporario
	
	elif parameter in ["quintessência", "paradoxo"]:
		quintessencia_atual = character_data['quintessencia']
		paradoxo_atual = character_data['paradoxo']
		
		if parameter == "quintessência":
			max_increment = 20-(quintessencia_atual + paradoxo_atual)
			newValue = max(min(value,max_increment) + quintessencia_atual,0)
			database.updateByQuery({"nome": character_name}, {"quintessencia":newValue})
		elif parameter == "paradoxo":
			newValue = min((value+paradoxo_atual),20)
			quintessencia_atual = min(quintessencia_atual, 20-newValue)
			database.updateByQuery({"nome": character_name}, {"quintessencia":quintessencia_atual})
			database.updateByQuery({"nome": character_name}, {"paradoxo":newValue})
		return newValue
	

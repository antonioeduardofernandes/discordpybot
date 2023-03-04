from pysondb import db
database = db.getDb("database.json")

def display_vitality(character):
	symbols = []
	labels = ['escoriado', 'machucado (-1)', 'ferido (-1)', 'ferido gravemente (-2)', 'espancado (-2)', 'aleijado (-5)', 'incapacitado']
	vitality_display = []
	for n in range(character['vitalidade']['agravado']):
		# print('◆')
		symbols.append('◆')
	for n in range(character['vitalidade']['letal']):
		# print('■')
		symbols.append('■')
	for n in range(character['vitalidade']['contusão']):
		# print('▣')
		symbols.append('▣')
	for n in range(7 - sum(character['vitalidade'].values())):
		# print('□')
		symbols.append('□')

	for n in range(7):
		vitality_display.append(symbols[n] + " " + labels[n].capitalize())

	return "\n".join(vitality_display)

def heal(character,amount):
	agravado = character['vitalidade']["agravado"]
	letal = character['vitalidade']["letal"]
	contusao = character['vitalidade']["contusão"]
	healed = True

	if amount <= 0 or (agravado == 0 and letal == 0 and contusao == 0):
		healed = False
		return healed
	else:
			while amount > 0:
				if contusao > 0:
					contusao -= 1
					amount -= 1
				elif letal > 0:
					letal -= 1
					amount -= 1
				elif agravado > 0:
					agravado -= 1
					amount -= 1
				elif contusao == 0 and letal == 0 and agravado == 0:
					amount = 0
	database.updateByQuery({"nome": character['nome']}, {"vitalidade":{'agravado':agravado,'letal':letal, 'contusão':contusao}})
	return healed


def apply_damage(character,type, amount):
	agravado = character['vitalidade']["agravado"]
	letal = character['vitalidade']["letal"]
	contusao = character['vitalidade']["contusão"]
	dead = False

	for n in range(amount):
		if(letal + agravado == 7):
			dead = True
			return dead 
		if not type == 'contusão':
			if type== 'letal': letal +=1
			if type== 'agravado': agravado +=1
			database.updateByQuery({"nome": character['nome']}, {"vitalidade":{'agravado':agravado,'letal':letal, 'contusão':contusao}})
		else:
			if(letal + agravado +  contusao < 7):
				contusao +=1
				database.updateByQuery({"nome": character['nome']}, {"vitalidade":{'agravado':agravado,'letal':letal, 'contusão':contusao}})
			else:
				contusao -=1
				letal +=1
				database.updateByQuery({"nome": character['nome']}, {"vitalidade":{'agravado':agravado,'letal':letal, 'contusão':contusao}})

	return dead
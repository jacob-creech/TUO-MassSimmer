import TUOSettings, re, os

def playerDict():
	playerDict = {}
	file = open(TUOSettings.filename, "r")
	for line in file:
		player = line.split(': ')[0]
		deck = line.split(': ')[1]
		playerDict[player] = deck
	return playerDict

def simOpponent(OpSys, deck, iterations):
	#./tuo "Arkadios, Dreamhaunter, Demi Constrictor, Scorched Hellwing, The Adversary, Bolt Crag, Gorrus Rav, Ezamit Tranq, Deserted Baughe, Erebus City Sector, Savant Ascendant, Hex Arrival-5, Gehenna Cursed" "Serapherus Mutant" pvp ordered endgame 0 climb 1000000
	#line = ' "Serapherus Mutant" pvp ordered endgame 0 climb '
	print OpSys + deck + line + str(iterations)
	result = os.system(OpSys + deck + line + str(iterations))
	
def main():
	
	iniVariables()
	
	decks = playerDict()

	file = open(TUOSettings.result, "w")

	for line in decks:
		print decks[line]
		#result = simOpponent(os, decks[line], iterations)
		#file.write(line + str(result))




main()
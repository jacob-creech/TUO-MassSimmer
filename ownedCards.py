import urllib2
import json
import Queue
import time
import random
import sys
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup

cardIds = []
ownedCards = []
cardList = []

def getIDs(user_id, password, syncode):
	summaries = json.loads(urllib2.urlopen('https://mobile.tyrantonline.com/api.php?message=init&user_id=' + user_id + '&password=' + password + '&syncode=' + syncode, timeout = 10).read().encode('utf-8'))
	for line in summaries["user_cards"]:
		if int(summaries["user_cards"][line]['num_owned']) > 0:
			cardIds.append(str(line))

def getOwnedCards(cardIds):
	tree = ET.parse('cards.xml')
	root = tree.getroot()
	for unit in root.iter('unit'):
		if unit.find('upgrade') is not None:
			for id in unit.findall('upgrade'):
				if id.find('card_id').text in cardIds:
					ownedCards.append(unit.find('name').text)

def main():
	user_id = ''
	password = ''
	syncode = ''
	getIDs(user_id, password, syncode)
	getOwnedCards(cardIds)
	
	f = open('ownedcards.txt', 'w')
	for card in ownedCards:
		f.write(card + '\n')
	
main()
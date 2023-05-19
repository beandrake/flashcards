import random
import os

class flashcards:

	def __init__(self, filename):		
		self.cardList = self.readCardFile(filename)


	def _clearScreen(self):
		#print('\033c', end='') # this doesn't work for me
		os.system('cls') # Windows only
	

	def readCardFile(self, filename):
		
		with open (filename, 'r') as cardFile:
			linesFromFile = cardFile.readlines()

		blockList = []	# a block is a collection of text that represents the front or back of a flashcard
		currentBlockContents = ''
		# first, separate file into blocks; each block is a series of consecutive non-whitespace lines
		for thisLine in linesFromFile:
			# If we've detected the block delimiter and we have content for this block...			
			lineIsJustWhiteSpace = thisLine.isspace()
			if lineIsJustWhiteSpace and currentBlockContents != '':
				# This block is done, add it to the list and start a new block
				blockList.append(currentBlockContents)
				currentBlockContents = ''
			# Otherwise the line isn't the delimiter, so add it to the current block
			else:
				currentBlockContents += thisLine

		# If we reached the end and have content in our current block, add it to the list
		if currentBlockContents != '':
			blockList.append(currentBlockContents)

		if len(blockList) % 2 != 0:
			raise RuntimeError(f"Input file {filename} does not contain an even number of text blocks that represent card faces.  Each flashcard needs two sides!")

		# Make cards, each card consisting of two consecutive blocks
		cardsToMake = len(blockList) / 2
		cardsMade = 0
		cardList = []
		while cardsMade < cardsToMake:
			term = blockList[cardsMade*2]
			definition = blockList[cardsMade*2 + 1]
			cardList.append( [term, definition] )
			cardsMade += 1
		
		return cardList

		
	def askCard(self, cardIndex=None):
		# if a card wasn't specified, choose one at random
		if cardIndex is None:
			cardIndex = random.randrange(0, len(self.cardList))
		
		ourCard = self.cardList[cardIndex]
		self._clearScreen()
		print()
		print( ourCard[0] )
		print()
		input(r"...")
		print()
		print( ourCard[1] )
		print()
		input(r"...")
		# wait for input

	
	def askAllCards(self):
		# get a list of all card indices and then shuffle it so the order is random
		cardOrder = []
		for i in range(0, len(self.cardList)):
			cardOrder.append(i)		
		random.shuffle(cardOrder)

		# ask all the cards
		for cardIndex in cardOrder:
			self.askCard(cardIndex)


if __name__ == '__main__':
	ourCards = flashcards(r'cards.txt')
	ourCards.askAllCards()
	print()
	print("Congratulations, you finished!")
	input()


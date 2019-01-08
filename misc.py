import pandas as pd
import numpy as np
import copy
import tests

def memory_address(in_var):
	return hex(id(in_var))

class Position(object):
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
	
	def trans(self, translation):
		#translate position by translate(Position)
		newX = self.x + translation.x
		newY = self.y + translation.y
		return Position(newX, newY)
		
class OccupiedArea(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		arr = [[{'occupants':[]} for h in range(height)] for w in range(width)]	
		self.is_occupied = arr
		
	def getBorderingCells(self, position, arr):
		cells = []
		x = position.x
		y = position.y
		for j in [y - 1, y, y + 1]:
			for i in [x - 1, x, x + 1]:
				if i == x and j == y:
					continue
				cells.append(arr[i][j])
		return cells
				
	def isOccupied(self, positions):
		#check whether multiple or only one position has been supplied
		if type(positions) == type([]):
			#checks whether any of the given postions are occupied
			for position in positions:
				x = position.x
				y = position.y
				occupants = self.is_occupied[x][y]['occupants']
				if occupants:
					#return True as soon as a true value is found
					return True
			#return false if all positions are unoccupied
			return False                              
		elif type(positions) == type(Position(0,0)):
			#positions contains only one value
			position = positions
			x = position.x
			y = position.y
			occupants = self.is_occupied[x][y]['occupants']
			if occupants:
				return True
			else:
				return False                                                                                                 
		else:
			print "something unexpected has been passed to isOccupied"                                         
		
	def changeCell(self, being, position, operation):
		if operation == 'occupy':
			function = self.occupy
		elif operation == 'vacate':
			function = self.vacate
		else:
			print "Don't know about that function yet."
			quit()
		
		before = self.getBorderingCells(position, self.is_occupied)
		function(being, position)
		after = self.getBorderingCells(position, self.is_occupied)
		if not tests.verifySame(before, after):
			print "Changing the cell has changed its surroundings."
			quit()
			
	def occupy(self, being, position):                                                                                    
		x = position.x
		y = position.y       
		self.is_occupied[x][y]['occupants'].append(being)
	
	def vacate(self, being, position):
		x = position.x
		y = position.y
		old = copy.deepcopy(self.is_occupied[x][y]['occupants'])
		if being in old:
			new = []
			for oldBeing in old:
				if oldBeing == being:
					continue
				else:
					new.append(oldBeing)
		self.is_occupied[x][y]['occupants'] = new
		
import pandas as pd
import numpy as np
import copy

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
		                                                                                                                  
	def occupy(self, being, position):                                                                                    
		x = position.x
		y = position.y       
		
		#print "               ", x - 1, "                              ", x, "                              ", x + 1
		#print y-1, self.is_occupied[x - 1][y - 1], self.is_occupied[x][y-1], self.is_occupied[x + 1][y-1]
		#print y, self.is_occupied[x - 1][y], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		#print y + 1,self.is_occupied[x - 1][y + 1], self.is_occupied[x][y+1], self.is_occupied[x + 1][y+1]  		
		#
		#print memory_address(self.is_occupied[y-1][x])
		#print memory_address(self.is_occupied[y][x])
		#print memory_address(self.is_occupied[y+1][x])
		#
		#print self.is_occupied[x][y]
		self.is_occupied[x][y]['occupants'].append(being)
		#print self.is_occupied[x][y]
		#                                
		#print "               ", x - 1, "                              ", x, "                              ", x + 1
		#print y-1, self.is_occupied[x - 1][y - 1], self.is_occupied[x][y-1], self.is_occupied[x + 1][y-1]
		#print y, self.is_occupied[x - 1][y], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		#print y + 1,self.is_occupied[x - 1][y + 1], self.is_occupied[x][y+1], self.is_occupied[x + 1][y+1]   
		#print y-1, self.is_occupied[x][y-1]
		#print y+1, self.is_occupied[x][y+1]
		#
		#
		#print memory_address(self.is_occupied[y-1][x])
		#print memory_address(self.is_occupied[y][x])
		#print memory_address(self.is_occupied[y+1][x])
	
	def vacate(self, position):
		x = position.x
		y = position.y
		self.is_occupied[x][y]['state'] = False
		
import pandas as pd
import numpy as np
import copy

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
		
		col = [{'state':False, 'by':[]} for i in range(height)]
		arr = [col for j in range(width)]
		self.is_occupied = arr
		
		
		
		#col = [{'state': False, 'by': []} for i in range(height)]
		#d = {key : value for (key,value) in [(j, col) for j in range(width)]}
		#self.is_occupied = pd.DataFrame(data=d)
		
	def isOccupied(self, positions):
		#check whether multiple or only one position has been supplied
		if type(positions) == type([]):
			#checks whether any of the given postions are occupied
			for position in positions:
				x = position.x
				y = position.y
				result = self.is_occupied[x][y]['state']
				if result == True:
					#return True as soon as a true value is found
					return result
			#return false if all positions are unoccupied
			return result
		elif type(positions) == type(Position(0,0)):
			#positions contains only one value
			position = positions
			x = position.x
			y = position.y
			result = self.is_occupied[x][y]['state']
			print x, y, result
			return result                                                                                                        
		else:
			print "something unexpected has been passed to isOccupied"                                         
		                                                                                                                  
	def occupy(self, position):                                                                                    
		x = position.x
		y = position.y       
		
		print "               ", x - 1, "                              ", x, "                              ", x + 1
		print y-1, self.is_occupied[x - 1][y - 1], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		print y, self.is_occupied[x - 1][y], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		print y + 1,self.is_occupied[x - 1][y + 1], self.is_occupied[x][y], self.is_occupied[x + 1][y]   
				         	                   
		print self.is_occupied[x][y]
		self.is_occupied[x][y]['state'] = True
		print self.is_occupied[x][y]
		
		print "               ", x - 1, "                              ", x, "                              ", x + 1
		print y-1, self.is_occupied[x - 1][y - 1], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		print y, self.is_occupied[x - 1][y], self.is_occupied[x][y], self.is_occupied[x + 1][y]
		print y + 1,self.is_occupied[x - 1][y + 1], self.is_occupied[x][y], self.is_occupied[x + 1][y]   
	
	def vacate(self, position):
		x = position.x
		y = position.y
		self.is_occupied[x][y]['state'] = False
		
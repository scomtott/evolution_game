import pandas as pd

class Position(object):
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		
class OccupiedArea(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		col = [False for i in range(height)]
		d = {key : value for (key,value) in [(i, col) for i in range(width)]}
		self.is_occupied = pd.DataFrame(data=d)
		
	def isOccupied(self, position):
		x = position.x
		y = position.y
		result = self.is_occupied[x][y]
		return result
		
	def occupy(self, position):
		x = position.x
		y = position.y
		self.is_occupied[x][y] = True
	
	def vacate(self, position):
		x = position.x
		y = position.y
		self.is_occupied[x][y] = False
		
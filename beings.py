import pygame
import random as rnd
import pandas as pd

from misc import Position
from misc import OccupiedArea
import world_parameters

wp = world_parameters.Params()
occupied = OccupiedArea(wp.width, wp.height)




class Being(object):
	def __init__(self, *args, **kwargs):
		pass
	
	def determineSpawnLoc(self):
		pass
	
	def checkPositionOK(self):
		pass
	
	def setBeingParameters(self, alive, position):
		pass
	
	def checkIfOccupied(self, position):
		pass
	
	def drawSelf(self, surface):
		pass
	
	def died(self):
		return None
		
class PointBeing(Being):
	
	def checkIfOccupied(self, position):
		return occupied.isOccupied(position)
		
	def drawSelf(self, surface):
		x = self.position.x
		y = self.position.y
		pygame.draw.rect(surface, self.colour, 
							pygame.Rect(x, y, self.size, self.size))
		
	def reportAreaOccupied(self):
		return self.position
	
class Fungus(PointBeing):
	def __init__(self, *args, **kwargs):
		position = self.determineSpawnLoc(kwargs)
		alive = self.checkPositionOK(position)
		self.setBeingParameters(alive, position)
		
	def determineSpawnLoc(self, kwargs):
		if kwargs.get('position', None) == None:
			#Fungus created by pressing space bar, position determined randomly
			x = rnd.randint(0,wp.width)
			y = rnd.randint(0,wp.height)
			position = Position(x,y)
		elif kwargs.get('position', None) != None:
			#Fungus created by multiplying - position based on existing fungus
			position = kwargs.get('position', None)
		else:
			print "something has gone wrong"
			position = Position(-1,-1)
		return position
		
	def checkPositionOK(self, position):
		if position == None:
			#this shouldn't happen but is included to makes sure beings with no
			#defined position end up dead.
			return False
		elif position.x < 0 or position.x > wp.width - 1:
			#position outside of the allowable x position range
			return False
		elif position.y < 0 or position.y > wp.height - 1:
			#position outside the allowable y position range
			return False
		else:
			#position is a valid position
			pass
		
		if self.checkIfOccupied(position) == True:
			#if position is already occupied, the being dies
			return False
		elif self.checkIfOccupied(position) == False:
			#if position is unoccupied, the being lives.
			return True
			
	def setBeingParameters(self, alive, position):
		if alive:
			self.position = position
			self.alive = alive
			occupied.occupy(position)
			self.colour = (255, 255, 255)
			
		elif not alive:
			self.position = Position(0,0)
			self.alive = False
			self.colour = (255, 0, 0)
			
		else:
			print "hmm"
			
		self.spawnPosition = position
		self.size = 1
		self.multiplyProb = 0.02
		self.isColony = False
	
	def attemptToMultiply(self):
		prob = self.multiplyProb
		rand = rnd.uniform(0.0, 1.0)
		if rand < prob:
			offspring = self.multiply()
		else:
			offspring = self.died()
			
		return offspring
		
	def died(self):
		return None
		

	def multiply(self):
		newPos = Position(self.position.x + rnd.randint(-3,3),
						  self.position.y + rnd.randint(-3,3))
		newFungus = Fungus(position=newPos)
		return newFungus
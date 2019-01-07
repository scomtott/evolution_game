import pygame
import random as rnd
import pandas as pd

from misc import Position
from misc import OccupiedArea
import world_parameters

wp = world_parameters.Params()
occupied = OccupiedArea(wp.width, wp.height)

class Fungus(object):
	def __init__(self, *args, **kwargs):
		if kwargs.get('position', None) == None:
			#Fungus created by pressing space bar, position determined randomly
			position = self.determineSpawnLoc()
			self.alive = True
		elif kwargs.get('position', None) != None:
			#Fungus created by multiplying - position based on existing fungus
			position = kwargs.get('position', None)
			self.alive = True
		else:
			print "something has gone wrong..."
			self.alive = False

		
		if position == None:
			self.alive = False
		elif position.x < 0 or position.x > wp.width - 1:
			self.alive = False
		elif position.y < 0 or position.y > wp.height - 1:
			self.alive = False
		else:
			self.alive = True
			self.position = self.checkIfOccupied(position)
	
		if self.alive == True:
			self.spawnX = self.position.x
			self.spawnY = self.position.y
			occupied.occupy(self.position)
			self.colour = (255, 255, 255)
			self.size = 1
			self.isColony = False
		elif self.alive == False:
			self.position = Position(0,0)
			self.spawnX = self.position.x
			self.spawnY = self.position.y
			self.colour = (255, 0, 0)
			self.size = 1
			self.isColony = False	
		else:
			print "uh oh"
	
	
		self.spawnX = self.position.x
		self.spawnY = self.position.y
		occupied.occupy(self.position)
		self.colour = (255, 255, 255)
		self.size = 1
		self.isColony = False
		
	def checkIfOccupied(self, position):
		if occupied.isOccupied(position) == False:
			return position
		elif occupied.isOccupied(position) == True:
			print "occupied"
			self.alive = False
			return Position(0,0)
		
	def determineSpawnLoc(self): 
		x = rnd.randint(0,wp.width)
		y = rnd.randint(0,wp.height)
		position = Position(x,y)
			
		return position
		
	def drawSelf(self, surface):
		x = self.position.x
		y = self.position.y
		pygame.draw.rect(surface, self.colour, pygame.Rect(x, y, 2, 2))
	
	def reportPosition(self):
		return self.position
	
	def attemptToMultiply(self, prob):
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
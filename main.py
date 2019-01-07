import pygame
import os
import random as rnd
import copy
import pandas as pd

from misc import Position
from misc import OccupiedArea
import world_parameters
wp = world_parameters.Params()

import beings

class SceneBase(object):
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)
        
        
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.active_beings = {'fungi': []}
        self.occupied = OccupiedArea(wp.width, wp.height)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
        	if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        		fungus = beings.Fungus()
        		if fungus.alive == True:
        			self.active_beings['fungi'].append(fungus)
        	
        	if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        		print self.occupied.is_occupied
        
    def Update(self):
    	active_beings_copy = copy.deepcopy(self.active_beings)
        for being in active_beings_copy['fungi']:
        	newBeing = being.attemptToMultiply(0.02)
        	if newBeing == None:
        		continue
        	elif newBeing.alive == True:
        		self.active_beings['fungi'].append(newBeing)
        	else:
        		pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        for being in self.active_beings['fungi']:
        	being.drawSelf(screen)

run_game(wp.width, wp.height, wp.fps, TitleScene())


"""
activeBeings = {'fungi':[]}

while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_SPACE]:
			fungus = beings.Fungus()
			activeBeings['fungi'].append(fungus)
			screen.blit(background, (0,0))
			for being in activeBeings['fungi']:
				being.drawSelf(screen)
			
	
			
	pygame.display.flip()
	clock.tick(60)
"""	                
	    
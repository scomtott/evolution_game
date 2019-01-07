Evolution game.

Not exactly sure where this project is going - it will probably *evolve* as I code it.
General idea is to have a world populated by creatures whose behaviour is algorithmic
and in some way mimics real life creatures - desire to reproduce, find food, conflict
etc. Players will be able to influence the environment (but not directly the behaviour
of the creatures). Currently unsure what the player's goal should be.

Info:

Written in Python 2.7 for Windows with PyGame.

Required non-standard modules:
pygame
pandas

Current functionality:

Window opens with red "title screen" - will be made a bit more exciting at some later 
point. 
Press Enter to start the game.
Pressing Space "innoculates" the world with fungi (one for each press).
Fungi will randomly multiply indefinitely. Probably a good idea to not leave this program 
running too long as there is no limit on how much memory it will use.
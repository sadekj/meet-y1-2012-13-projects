import pygame
from pygame import *
import stair
from stair import Stair

pygame.init()
var = 1
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def filecheck():
    print "Called from main.py"

stair = Stair()

class Game:
    def __init__(self):
        print "The game has been launched"
        
    def mainloop(self):
        while True:
            terminate = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate = True
            if terminate:
                print "Terminating application.."
                break

            screen.fill([200, 200, 200])

            # Update and draw all objects...

            pygame.display.flip()
            clock.tick(60)

def main():
    game = Game()
    game.mainloop()
    
if __name__ == "__main__":
    main()
    
quit()

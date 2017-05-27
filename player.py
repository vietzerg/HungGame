import pygame
from point import *
from  renderer import *
from inputmanager import *

class Player:
    def __init__(self):
        self.position = Point()
        self.renderer = SpriteRenderer(pygame.image.load("resources/player.png"))
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = 500

    def run(self):
        self.move()

    def move(self):
        if input_manager.right_pressed:
            self.position.add_up(5, 0)
        if input_manager.left_pressed:
            self.position.add_up(-5, 0)
        if input_manager.down_pressed:
            self.position.add_up(0, 5)
        if input_manager.up_pressed:
            self.position.add_up(0, -5)

        if self.constraints is not None:
            self.constraints.make(self.position)
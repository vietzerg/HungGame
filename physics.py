import math
from settings import *
from gamemanager import *


class Physics:
    def __init__(self):
        self.game_objects = []
        self.fruits = []
        self.traps = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def add_fruits(self, game_object):
        self.fruits.append(game_object)
        self.game_objects.append(game_object)

    #  Why need this ??
    def add_traps(self, game_object):
        self.game_objects.append(game_object)

    def check_contact(self, box_collider):
        for game_object in self.game_objects:
            if game_object.active:
                box_collider1 = box_collider
                box_collider2 = game_object.box_collider
                if box_collider1.check_collide(box_collider2):
                    return game_object

    def check_hit_wall(self):
        for fruit in self.fruits:
            if fruit.position.x <= 0 or fruit.position.x >= WIDTH:
                fruit.vel.x *= -1

    def check_hit_ground(self):
        for fruit in self.fruits:
            if fruit.ground_hit == 0 and fruit.position.y >= GROUND_y -32 :
                fruit.ground_hit += 1
                fruit.vel.x *= 1
                fruit.vel.y *= -0.7
            # if fruit.ground_hit == 0 and fruit.position.y >= GROUND_y - 32:
            #     fruit.vel.y *= -1
            #     fruit.acc.y = 3
            #     fruit.vel.add_up(0, fruit.acc.y)
            #     fruit.position.add_up(fruit.vel.x, fruit.vel.y + 0.5 * fruit.acc.y)

            if fruit.ground_hit == 1 and fruit.position.y <= GROUND_y - 50 -32 :
                fruit.ground_hit += 1
                fruit.vel.x *= 1
                fruit.vel.y *= -0.7

            if fruit.ground_hit == 2 and fruit.position.y >= GROUND_y -32:
                fruit.ground_hit += 1
                fruit.vel.x *= 0.8
                fruit.vel.y *= -1

            if fruit.ground_hit == 3 and fruit.position.y <= GROUND_y - 30 -32 :
                fruit.ground_hit += 1
                fruit.vel.x *= 0.8
                fruit.vel.y *= -1

            if fruit.ground_hit == 4 and fruit.position.y >= GROUND_y -32:
                fruit.vel.x = 0
                fruit.vel.y = 0
                fruit.active = False

physics = Physics()


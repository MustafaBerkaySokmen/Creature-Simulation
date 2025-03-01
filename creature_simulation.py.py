import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
from random import choice

class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.food_count = 0
        self.eat_times = deque(maxlen=2)  # Use a deque to efficiently keep track of the last 2 eating times

    def move(self, game_map):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        valid_moves = [d for d in directions if self.is_valid_move(game_map, d)]
        if valid_moves:
            move = choice(valid_moves)
            self.x += move[0]
            self.y += move[1]

    def is_valid_move(self, game_map, move):
        new_x = self.x + move[0]
        new_y = self.y + move[1]
        return 0 <= new_x < game_map.shape[0] and 0 <= new_y < game_map.shape[1]

    def eat(self, food_spots, current_time):
        if (self.x, self.y) in food_spots:
            food_spots.remove((self.x, self.y))
            self.food_count += 1
            self.eat_times.append(current_time)

    def can_survive(self, current_time):
        if len(self.eat_times) == 0:
            return False
        return current_time - self.eat_times[0] <= 10

    def can_reproduce(self, current_time):
        return len(self.eat_times) == 2 and self.eat_times[1] - self.eat_times[0] <= 10


def game_step(game_map, creatures, food_spots, current_time):
    new_creatures = []
    for creature in creatures:
        creature.move(game_map)
        creature.eat(food_spots, current_time)
        if creature.can_survive(current_time):
            new_creatures.append(creature)
        if creature.can_reproduce(current_time):
            new_creatures.append(Creature(creature.x, creature.y))
    creatures = new_creatures
    spawn_food(game_map, food_spots)
    return creatures, food_spots


def spawn_food(game_map, food_spots, num_food=1):
    for _ in range(num_food):
        while True:
            x = np.random.randint(game_map.shape[0])
            y = np.random.randint(game_map.shape[1])
            if (x, y) not in food_spots:
                food_spots.append((x, y))
                break


def update(num, img, game_map, creatures, food_spots):
    game_map.fill(0)

    for spot in food_spots:
        game_map[spot[0], spot[1]] = 1

    for creature in creatures:
        game_map[creature.x, creature.y] = 2

    img.set_array(game_map)

    creatures, food_spots = game_step(game_map, creatures, food_spots, num)

    return img,


map_size = 10
num_steps = 20
game_map = np.zeros((map_size, map_size))
creatures = [Creature(np.random.randint(map_size), np.random.randint(map_size))]
food_spots = []

fig, ax = plt.subplots()
img = ax.imshow(game_map, cmap='viridis')

ani = FuncAnimation(fig, update, frames=num_steps, fargs=(img, game_map, creatures, food_spots), interval=200, blit=True)

plt.show()

import random
from nc_server_utils import Communicator
MAP_WIDTH = 60
MAP_HEIGHT = 40
ENCOUNTER_CHANCE = 0.5
BASE_LEVEL_EXP = 1000
LEVEL_INCREASE_BASE = 1.3

NAMES = ['Foo', 'Bar', 'Fiz', 'Baz']
io = Communicator(DEBUG=False)


class Pythomon:

    def __init__(self):
        self.level = 1
        self.max_hp = 20
        self.cur_hp = 20
        self.powers = [
            ('Basic power 1', 0.3, 5),
        ]
        self.exp_current = 0
        self.name = random.choice(NAMES)

    def check_next_level(self, level):
        return BASE_LEVEL_EXP * LEVEL_INCREASE_BASE ** self.level

    def __str__(self):
        return "{}: Level: {} HP {}/{}".format(
            self.name, self.level, self.cur_hp, self.max_hp)

    def fight(self, monster):
        while monster.hp > 0 and self.hp > 0:
            monster_attack = random.choice(monster.powers)
            io.print("Monster uses {}", monster_attack[0])
            if monster_attack[1] > random.random():
                self.get_hit(monster_attack[2])
                io.print("Monster deals {} damage".format(monster_attack[2]))
                if not self.cur_hp:
                    io.print("You lost!")


class Player:
    def __init__(self):
        self.coords = [MAP_WIDTH//2, MAP_HEIGHT//2]
        self.pythomons = [Pythomon(), Pythomon()]

    def move(self, vector):
        self.coords[0] += vector[0]
        self.coords[1] += vector[1]
        if random.random() < ENCOUNTER_CHANCE:
            monster = Pythomon()
            io.print("Encountered wild monster... growl!!!!")
            io.print(monster)
            self.list_pythomons(True)
            pythomon_index = io.input('Select a pythomon: ')
            pythomon = self.pythomons[int(pythomon_index)]
            pythomon.fight(monster)

    def list_pythomons(self, show_indices=False):
        io.print('Available pythomons:')
        for i, pythomon in enumerate(self.pythomons):
            if show_indices:
                io.print('{}: {}'.format(i, pythomon))
            else:
                io.print(pythomon)


if __name__ == '__main__':

    player = Player()
    io.print(player.coords)

    while True:
        command = io.input()

        if command == 'exit' or command == 'quit' or command == 'q':
            break
        elif command == 'right':
            player.move([1, 0])
        elif command == 'left':
            player.move([-1, 0])
        elif command == 'up':
            player.move([0, 1])
        elif command == 'down':
            player.move([0, -1])
        elif command == 'list pythomons':
            player.list_pythomons()

        else:
            io.print('Command was not recognized')

        io.print(player.coords)

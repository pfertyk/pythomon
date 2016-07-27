import random
import argparse
from nc_server_utils import Communicator
parser = argparse.ArgumentParser(
    description='Pythomon game coded during PyRa #25')
parser.add_argument('--debug', dest='debug', action='store_true')
parser.add_argument('--no-debug', dest='debug', action='store_false')
parser.set_defaults(debug=True)
args = parser.parse_args()
MAP_WIDTH = 60
MAP_HEIGHT = 40
ENCOUNTER_CHANCE = 0.5
BASE_LEVEL_EXP = 1000
LEVEL_INCREASE_BASE = 1.3

NAMES = ['Foo', 'Bar', 'Fiz', 'Baz']


class Pythomon:

    def __init__(self,io):
        self.level = 1
        self.max_hp = 20
        self.cur_hp = 20
        self.powers = [
            ('Basic power 1', 0.7, 5),
        ]
        self.exp_current = 0
        self.name = random.choice(NAMES)
        self.io=io

    def check_next_level(self, level):
        return BASE_LEVEL_EXP * LEVEL_INCREASE_BASE ** self.level

    def __str__(self):
        return "{}: Level: {} HP {}/{}".format(
            self.name, self.level, self.cur_hp, self.max_hp)

    def fight(self, monster):
        while monster.cur_hp > 0 and self.cur_hp > 0:
            monster_attack = random.choice(monster.powers)
            self.io.print("Monster uses {}".format(monster_attack[0]))
            if monster_attack[1] > random.random():
                self.get_hit(monster_attack[2])
                self.io.print("Monster deals {} damage".format(monster_attack[2]))
                if not self.cur_hp:
                    self.io.print("You lost!")
                    break
            else:
                self.io.print('Monster missed!')
            self.io.print('Available attacks:')
            for i, attack in enumerate(self.powers):
                self.io.print('{}: {}'.format(i, attack[0]))
            attack_index = self.io.input('Choose an attack: ')
            pythomon_attack = self.powers[int(attack_index)]
            if pythomon_attack[1] > random.random():
                self.io.print('Pythomon deals {} damage'.format(pythomon_attack[2]))
                monster.get_hit(pythomon_attack[2])
                if not monster.cur_hp:
                    self.io.print('You won!')
                    break

    def get_hit(self, damage):
        self.cur_hp -= damage
        if self.cur_hp < 0:
            self.cur_hp = 0


class Player:
    def __init__(self,io):
        self.coords = [MAP_WIDTH//2, MAP_HEIGHT//2]
        self.pythomons = [Pythomon(io), Pythomon(io)]
        self.io=io
    def move(self, vector):
        self.coords[0] += vector[0]
        self.coords[1] += vector[1]
        if random.random() < ENCOUNTER_CHANCE:
            monster = Pythomon(self.io)
            self.io.print("Encountered wild monster... growl!!!!")
            self.io.print(monster)
            self.list_pythomons(True)
            pythomon_index = self.io.input('Select a pythomon: ')
            pythomon = self.pythomons[int(pythomon_index)]
            pythomon.fight(monster)
            if not monster.cur_hp:
                self.pythomons.append(monster)

    def list_pythomons(self, show_indices=False):
        self.io.print('Available pythomons:')
        for i, pythomon in enumerate(self.pythomons):
            if show_indices:
                self.io.print('{}: {}'.format(i, pythomon))
            else:
                self.io.print(pythomon)

def main(self):
    player = Player(self)
    self.print(player.coords)

    while True:
        command = self.input()

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
            self.print('Command was not recognized')

        self.print(player.coords)
if __name__ == '__main__':
    Communicator.main=main
    while True:
        io = Communicator(DEBUG=args.debug)

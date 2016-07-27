MAP_WIDTH = 60
MAP_HEIGHT = 40


class Player:
    def __init__(self):
        self.coords = [MAP_WIDTH//2, MAP_HEIGHT//2]

    def move(self, vector):
        self.coords[0] += vector[0]
        self.coords[1] += vector[1]

if __name__ == '__main__':
    player = Player()
    print(player.coords)

    while True:
        command = input()

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
        else:
            print('Command was not recognized')

        print(player.coords)

MAP_WIDTH = 60
MAP_HEIGHT = 40


class Player:
    def __init__(self):
        self.coords = [MAP_WIDTH//2, MAP_HEIGHT//2]

if __name__ == '__main__':
    player = Player()
    print(player.coords)

    while True:
        command = input()
        print(command)

        if command == 'exit':
            break

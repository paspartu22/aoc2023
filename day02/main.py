class Game:
    def __init__(self, id):
        self.id = int(id)
        self.red = 0
        self.green = 0
        self.blue = 0
    def __str__(self) -> str:
        return f"game #{self.id} has {self.red} red, {self.green} green, {self.blue} blue"
    
with open("data.txt", 'r') as file:
    result = 0
    for line in file:
        line = line.split(':')
        #print(line)
        game = Game(line[0].split(" ")[1])
        line = line[1].strip().split(';')
        for item in line:
            item = item.split(',')
            for hand in item:
                hand = hand.strip().split(" ")
                if hand[1] == "blue" and int(hand[0]) > game.blue:
                    game.blue = int(hand[0])
                elif hand[1] == "red" and int(hand[0]) > game.red:
                    game.red = int(hand[0])
                elif hand[1] == "green" and int(hand[0]) > game.green:
                    game.green = int(hand[0])
        print(game)
        #part one
        '''
        if game.red <= 12 and game.green <= 13 and game.blue <= 14:
            print (f"game {game.id} is valid")
            result += game.id
        '''
        #part two
        print (f"power of game {game.id} = {game.red*game.blue*game.green}")
        result += (game.red*game.blue*game.green)
    print (result)    
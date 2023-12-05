class Game:
    def __init__(self, id) -> None:
        self.id = int(id)
        self.wins = 0
        self.numbers = 0 
    def __str__(self) -> str:
        return f"game {self.id}, wins {self.wins}, numbers{self.numbers}"

list_of_wins = {}
    
with open("data.txt", "r") as file:      
    part1_result = 0
    for line in file:
        while "  " in line:
            line = line.replace("  ", " ", -1) #remove double spaces
        #data parsing
        line = line.strip().split(":")
        game = Game(line[0].split(" ")[1])
        line = line[1].strip().split("|")
        game.wins = line[0].strip().split(" ")
        game.numbers = line[1].strip().split(" ")
        
        #part_one
        part1_game_result = 0       
        part2_game_result = 0
        for number in game.numbers:
            #part 1 game result calc
            if number in game.wins:
                if part1_game_result == 0:
                    part1_game_result = 1
                else:
                    part1_game_result *= 2
            #part 2 game result calc
                part2_game_result +=1
                        
        part1_result += part1_game_result
        #add original one
        if game.id in list_of_wins:
            list_of_wins[game.id] += 1
        else:
            list_of_wins[game.id] = 1
        #add wins
        for i in range(part2_game_result):
            if game.id+i+1 in list_of_wins:
                list_of_wins[game.id+i+1] += list_of_wins[game.id]
            else:
                list_of_wins[game.id+i+1] = list_of_wins[game.id]
                
        print (f"part 1 game {game.id} worth {part1_game_result} ")
        print (f"part 2 game {game.id} worth {part2_game_result}")
  
    print (f"part 1 {part1_result}")
    print (f"part 2 {sum(list_of_wins.values())}")
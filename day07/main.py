hand_names = {1: "high",
              2: "one p",
              3: "two p",
              4: "three",
              5: "full house",
              6: "four",
              7: "five"}
class Hand:
    def __init__(self, input) -> None:
        input = input.split()
        self.bid = int(input[1])
        self.hand_str = input[0]
        self.hand_str = self.hand_str.replace("A", "e")
        self.hand_str = self.hand_str.replace("K", "d")
        self.hand_str = self.hand_str.replace("Q", "c")
        self.hand_str = self.hand_str.replace("J", "1")
        self.hand_str = self.hand_str.replace("T", "a")        
        self.hand_int = int(self.hand_str, 16)
        self.hand_strength = 0
        
    def __str__(self):
        return f"{hand_names[self.hand_strength]} | {self.hand_str} | {self.hand_int:x} | {self.bid}"
    
    def parse_hand(self):
        print(self.hand_str)
        hand_values = {"1" : 0}
        for card in self.hand_str:
            if card in hand_values:
                hand_values[card] += 1
            else:
                hand_values[card] = 1
        max_value = [0, 0]
        for card in hand_values.items():
            if card[0] != "1" and card[1] > int(max_value[1]):
                max_value = card
        if max_value[1] != 0:
            hand_values[max_value[0]] += hand_values["1"]
            hand_values["1"] = 0
        else:
            hand_values["1"] = 5
            
                
        if 5 in hand_values.values():
            self.hand_strength = 7
        elif 4 in hand_values.values():
            self.hand_strength = 6
        elif 3 in hand_values.values() and 2 in hand_values.values():
            self.hand_strength = 5
        elif 3 in hand_values.values():
            self.hand_strength = 4
        elif 2 in hand_values.values():
            amount_of_pair = 0
            for item in hand_values.values():
                if item == 2:
                    amount_of_pair += 1
            if amount_of_pair == 2:
                self.hand_strength = 3
            else:
                self.hand_strength = 2
        elif 1 in hand_values.values():
            self.hand_strength = 1
        else:
            print("Error")
            input()
        
        #self.hand_int = int(self.hand_str, 16)
        return self.hand_strength
    
    
    
def parse(file):
    with open(file, "r") as file:
        hands = []
        for line in file:
            hands.append(Hand(line))
        
        return hands

def main():
    hands = parse("data.txt")
    hands_in_groups = {7:[], 6:[], 5:[], 4:[], 3:[], 2:[], 1:[]}
    for hand in hands:
        strength = hand.parse_hand()
        hands_in_groups[strength].append(hand)
        #print(hand)
    result = 0
    rank = 0
    for item in hands_in_groups.values():
        print(len(item))
    for hand_strength in range(1, 8):
        print(hand_strength)
        for hand_value in range(0x11111, 0xf0000):
            for hand in hands_in_groups[hand_strength]:
                if hand_value == hand.hand_int:
                    rank += 1
                    result += rank*hand.bid
                    print(f"{rank} | {hand}")    
    print("=== result ===")
    print(result)
    
if __name__ == "__main__":
    main()
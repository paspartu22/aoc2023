hand_names = {1: "high card",
              2: "one pair",
              3: "two pairs",
              4: "three of a kind",
              5: "full house",
              6: "four of a kind",
              7: "five of a kind"}
class Hand:
    def __init__(self, input) -> None:
        input = input.split()
        self.bid = int(input[1])
        self.hand_str = input[0]
        self.hand_str = self.hand_str.replace("A", "e")
        self.hand_str = self.hand_str.replace("K", "d")
        self.hand_str = self.hand_str.replace("Q", "c")
        #self.hand_str = self.hand_str.replace("J", "b") part 1
        self.hand_str = self.hand_str.replace("J", "1")
        self.hand_str = self.hand_str.replace("T", "a")        
        self.hand_int = int(self.hand_str, 16)
        self.hand_strength = 0
        
    def __str__(self):
        return f"{hand_names[self.hand_strength]} \t| {self.hand_str} \t| {self.hand_int:x} \t| {self.bid}"

    def __lt__(self, other):
        return self.hand_int < other.hand_int
    
    def parse_hand(self):
        #map amount of cards
        print(self.hand_str)
        hand_values = {"1" : 0}
        for card in self.hand_str:
            if card in hand_values:
                hand_values[card] += 1
            else:
                hand_values[card] = 1
        #process jokers (remove for part 1)
        max_value = [0, 0]
        for card in hand_values.items():
            if card[0] != "1" and card[1] > int(max_value[1]):
                max_value = card
        if max_value[1] != 0:
            hand_values[max_value[0]] += hand_values["1"]
            hand_values["1"] = 0
        else:
            hand_values["1"] = 5
        #process strength of hand
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
        else:
            self.hand_strength = 1
        return self.hand_strength
    
def parse_input(file):
    with open(file, "r") as file:
        hands = []
        for line in file:
            hands.append(Hand(line))
        return hands

def main():
    hands = parse_input("data.txt")
    hands_in_groups = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    for hand in hands:
        strength = hand.parse_hand()
        hands_in_groups[strength].append(hand)

    result = 0
    rank = 0
    for hand_group in hands_in_groups.values():
        hand_group.sort()
        for hand in hand_group:
            rank += 1
            result += rank*hand.bid
            print(f"{rank} \t| {hand}")    
    print("=== result ===")
    print(result)

if __name__ == "__main__":
    main()
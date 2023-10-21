import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0

    def roll_die(self):
        roll = random.randint(1, 6)
        if roll == 1:
            self.turn_total = 0
        else:
            self.turn_total += roll
        return roll

    def hold(self):
        self.score += self.turn_total
        self.turn_total = 0

    def get_decision(self):
        decision = input(f"{self.name}, enter 'r' to roll or 'h' to hold: ").strip().lower()
        return decision

def play_game():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    current_player = random.choice(players)

    while True:
        print(f"{current_player.name}'s turn:")
        decision = current_player.get_decision()
        
        if decision == 'r':
            roll = current_player.roll_die()
            print(f"{current_player.name} rolled a {roll}.")
            print(f"Turn total: {current_player.turn_total}, Total score: {current_player.score}")
            
            if current_player.turn_total == 0:
                current_player = player1 if current_player == player2 else player2
        elif decision == 'h':
            current_player.hold()
            print(f"{current_player.name} decided to hold.")
            print(f"Turn total: {current_player.turn_total}, Total score: {current_player.score}")
            
            if current_player.score >= 100:
                print(f"{current_player.name} wins!")
                break
            else:
                current_player = player1 if current_player == player2 else player2
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

if __name__ == "__main__":
    random.seed(0)
    play_game()

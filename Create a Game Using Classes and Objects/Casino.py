import random

class Player:
  
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
    def __repr__(self):
        return "Player {name} has {money} money.".format(name=self.name, money=self.money)
  
    def place_bet(self, amount, game):
        if amount < game.minBet or amount > game.maxBet:
            return "Bet amount must be between {} and {}.".format(game.minBet, game.maxBet)
        if self.money < amount:
            return "Insufficient funds to place this bet."
        self.money -= amount
        return "Bet of {} placed successfully.".format(amount)

    def win(self, amount):
        self.money += amount * 1.5 
        return "You have won {}".format(amount * 1.5)

    def lose(self):
        return "You have lost :("
  
    def check_balance(self):
        return "You have {} in the bank.".format(self.money)

    def join_game(self, game):
        return "Joined the {} table".format(game.name)

class Games:
  
    def __init__(self, name, minBet, maxBet):
        self.name = name
        self.minBet = minBet
        self.maxBet = maxBet
    
    def __repr__(self):
        return "Game {name} with min bet {minBet} and max bet {maxBet}.".format(name=self.name, minBet=self.minBet, maxBet=self.maxBet)
class Blackjack(Games):
  
    def __init__(self, minBet, maxBet):
        super().__init__("Blackjack", minBet, maxBet)
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    
    def __repr__(self):
        return "Blackjack game with min bet {minBet} and max bet {maxBet}.".format(minBet=self.minBet, maxBet=self.maxBet)

    def deal_card(self):
        return random.choice(self.deck)

    def play(self, player):
        stand = False
        player_hand = [self.deal_card(), self.deal_card()]
        dealer_hand = [self.deal_card(), self.deal_card()]
        print("Player's hand:", player_hand)
        print("Dealer's hand:", dealer_hand[0], "?")
        
        while not stand:
            choice = input("Hit or stand? (h/s): ").lower()
            if choice == 'h':
                player_hand.append(self.deal_card())
                print("Player's hand:", player_hand)
                if sum(player_hand) > 21:
                    print("Bust! You lose.")
                    player.lose()
                    return
            elif choice == 's':
                stand = True
            else:
                print("Invalid choice. Please enter 'h' to hit or 's'")
        
        print("Dealer's hand:", dealer_hand)
        while sum(dealer_hand) < 17:
            dealer_hand.append(self.deal_card())
            print("Dealer's hand:", dealer_hand)
        
        if sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
            print("You win!")
            player.win(sum(player_hand))
        else:
            print("Dealer wins.")
            player.lose()



player = Player("Alice", 500)
blackjack = Blackjack(10, 100)
print(player.join_game(blackjack))

try:
    choice1 = input("How much do you want to bet: ")
except EOFError:
    print("EOFError, bet = 50")
print(player.place_bet(int(choice1), blackjack))

blackjack.play(player)

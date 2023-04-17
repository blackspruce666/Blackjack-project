import random
import db


class not_enough_chips_exception(Exception):
    "Raised when you do not have enough chips to play" 
    pass


print("BLACKJACK!")
print("Blackjack payout is 3:2")


def make_deck():
    #use this line if the unicode characters don't work nicely on your system.
    #suits = ["of hearts", "of diamonds", "of spades", "of clubs"]
    suits = ["\u2665", "\u2666", "\u2660", "\u2663"]
    deck = []

    for suit in suits:
        i = 1
        while i < 14:
            if i == 1:
                deck.append(["A", suit, 11])
            elif i == 11:
                deck.append(["J", suit, 10])
            elif i == 12:
                deck.append(["Q", suit, 10])
            elif i == 13:
                deck.append(["K", suit, 10])
            else:
                deck.append([i, suit, i])
            i += 1

    return deck


def draw_card(deck):
    card = deck.pop(0)
    return card


def score_hand(hand):
    score = []
    a = 11
    for card in hand:
        score.append(card[2])

    while sum(score) > 21 and a in score:
        for i in score:
            if i == 11 and (sum(score) > 21):
                score.remove(i)
                score.append(1)

    return sum(score)


def display_1_dealer(hand):
    print()
    print(f"DEALER'S SHOWN CARD:")
    print(f"{hand[0][0]} {hand[0][1]}")
    return hand


def display_hand_dealer(hand):
    print()
    print("DEALER'S CARDS:")
    for x in hand:
        print(f"{x[0]} {x[1]}")
    return hand


def display_cards_player(hand):
    print()
    print(f'YOUR CARDS:')
    for x in hand:
        print(f"{x[0]} {x[1]}")
    return hand


def set_bet(money):
    while True:
        try:
            bet = float(input("Bet: "))
            if bet > money:
                raise not_enough_chips_exception
            if bet < 5 or bet > 1000:
                raise ValueError("Bet must be between 5 and 1000")
            return bet
        except ValueError:
            print("Please enter a number of chips between 5 and 1000")
        except not_enough_chips_exception:
            print("You can't bet more money than you have.")


def initialize_money():
    while True:
        try:
            money = float(db.read_file())
            return money
        except (TypeError, UnboundLocalError, FileNotFoundError, IndexError, ValueError):
            db.write_file([100.00])


def main():
    while True:
        print()
        #get money from the file
        money = initialize_money()

    
        print(f"Money: {money}")

        while money < 5:
            print()
            reset = input("Would you like some more chips? (y/n)")
            if reset.lower() == "y":
                db.reset_account()
                money = initialize_money()
                print("Your account has been topped up to 100.")
                print()
            elif reset.lower() == "n":
                print("Come back soon!")
                print("Bye!")
                quit()
            else:
                print("Please choose y or n")
                print()

        #set bet
        bet = set_bet(money)

        #make and shuffle deck
        deck1 = make_deck()
        random.shuffle(deck1)

        #initialize hands as empty lists
        hand = []
        dealer_hand = []

        #deal cards to player and dealer
        hand.append(draw_card(deck1))
        dealer_hand.append(draw_card(deck1))
        hand.append(draw_card(deck1))
        dealer_hand.append(draw_card(deck1))

        #show dealer's first card
        display_1_dealer(dealer_hand)

        #show player's cards
        display_cards_player(hand)

        #get player score. Checking here prevents the player hitting when they already have 21.
        player_score = score_hand(hand)

        #give the player the option to hit (starts a loop) or stand. Breaks automatically on 21 or higher.
        while player_score < 21:
            print()
            hos = input("Hit or stand? (hit/stand): ")
            if hos.lower() == "hit":
                hand.append(draw_card(deck1)) #add card
                display_cards_player(hand)  #show card
                player_score = score_hand(hand) #score hand to check for 21 or bust
            elif hos.lower() == "stand":
                break
            else:
                print("Error. Please enter hit or stand.")


        #dealer hits if dealer score is below 16
        player_score = score_hand(hand)
        dealer_score = score_hand(dealer_hand)
        while dealer_score < 17 and dealer_score <21:
            dealer_hand.append(draw_card(deck1))
            dealer_score = score_hand(dealer_hand)

        #player wins immediately on 21
        if player_score == 21:
            print()
            db.add_money(money, bet)
            print(f"YOUR POINTS:    {player_score}")
            print("WINNER WINNER CHICKEN DINNER!!!")
            print(f"Money:  {float(db.read_file())}")

        #player loses immediately if they go over 21/bust
        elif player_score > 21:
            print()
            db.lose_money(money, bet)
            print(f"YOUR POINTS:    {player_score}")
            print("BUST! You lose.")
            print(f"Money:  {float(db.read_file())}")


        #If player score is less than 21, program compares player hand to dealer hand
        elif player_score < 21:
            display_hand_dealer(dealer_hand)
            dealer_score = score_hand(dealer_hand)
            print()
            print(f"YOUR POINTS:    {player_score}")
            print(f"DEALER'S POINTS:    {dealer_score}")

            #Dealer wins
            if dealer_score < 22 and dealer_score > player_score:
                print()
                db.lose_money(money, bet)
                print("Sorry, you lose.")
                print(f"Money:  {float(db.read_file())}")

            #Player wins
            elif dealer_score < player_score:
                print()
                db.add_money(money, bet)
                print("You win!!!")
                print(f"Money:  {float(db.read_file())}")

            #Tie/push
            elif dealer_score > 21 or dealer_score == player_score:
                print()
                db.add_money(money, 0)
                print("Push. It's a tie. :/")
                print(f"Money:  {float(db.read_file())}")

        #play again/loop
        print()
        y = input("Play again? (y/n)")
        if y.lower() == "n":
            print("Come back soon!")
            print("Bye!")
            break
        elif y.lower() == "y":
            continue
        else:
            print("Please enter y or n")

#Dunder
if __name__ == "__main__":
    main()

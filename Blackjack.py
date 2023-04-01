import random
import money


print("BLACKJACK!")
print("Blackjack payout is 3:2")


def make_deck():
    suits = ["of hearts", "of diamonds", "of spades", "of clubs"]
    deck = []

    for suit in suits:
        i = 1
        while (i < 14):
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


def shuffle(deck):
    random.shuffle(deck)
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


def hit_or_stand(hand, deck):
    while True:
        print()
        hos = input("Hit or stand? (hit/stand):    ")
        if hos.lower() == "hit":
            hand.append(draw_card(deck))
            display_cards_player(hand)

        elif hos.lower() == "stand":
            return hand
        else:
            print("Error. Please enter hit or stand.")


def main():
    while True:
        #make and shuffle deck
        deck1 = make_deck()
        shuffle(deck1)

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

        #give the player the option to hit (starts a loop) or stand
        hand = hit_or_stand(hand, deck1)

        #dealer hits if dealer score is below 16
        player_score = score_hand(hand)
        dealer_score = score_hand(dealer_hand)
        while dealer_score < 17:
            dealer_hand.append(draw_card(deck1))
            dealer_score = score_hand(dealer_hand)

        if player_score == 21:
            print()
            print(f"YOUR POINTS:    {player_score}")
            print("WINNER WINNER CHICKEN DINNER!!!")
            print()
            #give money

        elif player_score > 21:
            print()
            print(f"YOUR POINTS:    {player_score}")
            print("BUST! You lose.")
            #lose money

        elif player_score < 21:
            display_hand_dealer(dealer_hand)
            dealer_score = score_hand(dealer_hand)
            print(f"YOUR POINTS:    {player_score}")
            print(f"DEALER'S POINTS:    {dealer_score}")

            if dealer_score > player_score:
                print("Sorry, you lose.")


            elif dealer_score < player_score:
                print("You win!!!")

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









if __name__ == "__main__":
    main()
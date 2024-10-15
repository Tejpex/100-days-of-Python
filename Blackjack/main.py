import random
from art import logo

playing = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealers_cards = []
players_cards = []


def dealers_score():
    return sum(dealers_cards)


def players_score():
    return sum(players_cards)


while playing:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if want_to_play == "y":
        # Deal two cards each to player and dealer
        for n in range(2):
            players_cards.append(cards[random.randint(0, len(cards) - 1)])
            dealers_cards.append(cards[random.randint(0, len(cards) - 1)])

        print(logo)

        round_ended = False
        while not round_ended:
            # Check if player has 21 or more
            if players_score() == 21:
                round_ended = True
            elif players_score() > 21:
                # Change ace from 11 to 1
                if 11 in players_cards:
                    ace = players_cards.index(11)
                    players_cards[ace] = 1
                # More than 21 and no ace - player lose
                else:
                    round_ended = True
            # Let player see their hand and ask for more cards
            else:
                print(f"Your cards: {players_cards}. Current score: {players_score()}")
                print(f"Computer's first card: {dealers_cards[0]}")
                more_cards = input("Type 'y' to get another card. Type 'n' to pass. ")
                if more_cards == "y":
                    players_cards.append(cards[random.randint(0, len(cards) - 1)])
                else:
                    round_ended = True

        # Check to see if user is over 21
        if players_score() > 21:
            print(f"Your final hand: {players_cards}. Final score: {players_score()}")
            print("Sorry, you lose. 😥")
        else:
            # Fill dealer's hand with cards
            while dealers_score() < 17:
                dealers_cards.append(cards[random.randint(0, len(cards) - 1)])
                if dealers_score() > 21:
                    if 11 in dealers_cards:
                        ace = dealers_cards.index(11)
                        dealers_cards[ace] = 1

            # Print final hands
            print(f"Your final hand: {players_cards}. Final score: {players_score()}")
            print(f"Computer's final hand: {dealers_cards}. Final score: {dealers_score()}")

            # Check who wins
            if players_score() == dealers_score():
                print("It's a tie. Computer wins.")
            elif players_score() == 21:
                print("Blackjack! You win! 😎")
            elif dealers_score() > 21:
                print("Computer lost. You win! 😁")
            elif players_score() > dealers_score():
                print("Higher score. You win! 😃")
            else:
                print("Computer wins. You lose. 🙁")

        # Clear hands
        dealers_cards = []
        players_cards = []

    else:
        playing = False

print("Goodbye")

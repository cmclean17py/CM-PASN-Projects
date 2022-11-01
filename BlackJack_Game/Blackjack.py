import random
import time
import os

#Create deck of cards (4 cards of each suit)
card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4


#check if deck is empty and if so, reshuffle (inititlaize new deck) (working on feature)
def check_deck_for_shuffle(card_deck):
    if len(card_deck) == 0:
        print("The deck has run out. One moment while we shuffle your deck . . .")
        time.sleep(2)
        return card_deck


#Deal hand to both the user and CPU
def game_hand(card_deck):
    hand = []
    for i in range(2):
        random.shuffle(card_deck)
        card = card_deck.pop()
        hand.append(card)
    return hand

#Hit action will add card from deck to users hand
def hit(hand):
    card = card_deck.pop()
    hand.append(card)
    return hand

#Ask the user if they want to continue playing or leave game
def play_again():
    user_choice = input("Do you want to play again? Y/N: ").lower()
    if user_choice == "y":
        card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
        player_hand = []
        dealer_hand = []
        game()
    else:
        print("Thank you for playing, bye now!")
        exit()

# def print_status(player_hand, dealer_hand):
#     print(f"The dealer is showing{dealer_hand} for a total of {card_total(dealer_hand)}" )

#Determine if player has blackjack
def black_jack(dealer_hand, player_hand):
    if card_total(dealer_hand) == 21:
        print("The dealer has 21 BLACKJACK, you LOSE!")
        play_again()
    elif card_total(player_hand) == 21:
        print ("You have 21 BLACKJACK, you WIN")
        play_again()

#Return card total for player/dealer hand
def card_total(hand):
    total = 0
    for card in hand:
        if card == 11:
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total

#Determine the card total for player and dealer to decide who wins
def score(player_hand, dealer_hand):
    if card_total(player_hand) == 21:
        print("Congratulations you have blackjack! You Win ")
    elif card_total(dealer_hand) == 21:
        print("The Dealer has 21 BLACKJACK, You lose! Better luck next time")
    elif card_total(player_hand) > 21:
        print("You BUST, you lose!")
    elif card_total(dealer_hand) > 21:
        print("The Dealer BUST, you WIN!")
    elif card_total(player_hand) > card_total(dealer_hand):
        print("You scored higher than the Dealer, you WIN")
    elif card_total(dealer_hand) > card_total(player_hand):
        print("The Dealer has more than you, You LOSE! Better luck next time")

#Clear terminal when starting a new game
def clear():
    if os.name == "nt":
        os.system("cls")
    if os.name == "posix":
        os.system("clear")
    if os.name == "java":
        os.system("clear")

def print_results_of_hand(dealer_hand, player_hand):
    print_results = print(f"The dealer has {dealer_hand} with a total of {card_total(dealer_hand)} "
                          f"\n and you have {player_hand} with a total of {card_total(player_hand)}")
    return print_results



#Functionality of Blackjack game
def game():
    clear()
    choice = 0
    print("Welcome to Blackjack! Are you feeling lucky? ")
    if len(card_deck) == 0:

    dealer_hand = game_hand(card_deck)
    player_hand = game_hand(card_deck)
    while choice != "q":
        print(f"You currently have {player_hand} which totals to {card_total(player_hand)}")
        print(f"The dealer is showing a {dealer_hand}")
        black_jack(dealer_hand, player_hand)
        choice = input("Do you want to [S]tay [H]it or [Q}uit? ").lower()
        if choice == "h":
            hit(player_hand)
            while card_total(dealer_hand) < 17:
                hit(dealer_hand)
                print_results_of_hand(dealer_hand, player_hand)
                score(player_hand, dealer_hand)
                play_again()
        elif choice == "s":
            if card_total(dealer_hand) >= 17:
                print_results_of_hand(dealer_hand, player_hand)
                score(player_hand, dealer_hand)
                play_again()
            elif card_total(dealer_hand) < 17:
                hit(dealer_hand)
                print_results_of_hand(dealer_hand, player_hand)
                score(player_hand, dealer_hand)
                play_again()

game()








import random

def user_hand():
    hand = []
    for i in range(2):
        random_user = random.randint(2, 11)
        hand.append(random_user)
    return hand

def hit():
    card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    hit = random.choice(card_deck)
    return hit

def dealer():
    dealer_hand = []
    for i in range(2):
        random_dealer = random.randint(2,11)
        dealer_hand.append(random_dealer)
    return dealer_hand

user_choice = input('Do you want to hit or stay? ').lower()
#while user_choice == 'hit':
new_hand = sum(user_hand().append(hit()))
print(new_hand)



#Start Game and Greet User
#name = input('Enter your name if you are ready to play: ')
#print(f"Hello {name}, Welcome to Black Jack")



import time

#testing shuffling cards when list == 0
list = [1,2]
hand = []
for i in range(20):
    card = list.pop()
    print(list)
    hand.append(card)
    print(f"your hand {hand}")
    if len(list) == 0:
        print("One moment while we shuffle your deck")
        time.sleep(2)
        print("We are shuffling")
        list = [1,2] * 4
        print(list)


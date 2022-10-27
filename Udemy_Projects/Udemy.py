# st = ' Print words that start with s in this sentence'
# sword = st.split()
#for word in sword:
#   if word.startswith('s'):
#       print(word)
#for num in range(0,100):
#    if num % 2 == 0:
#        print(num)

#mylist = [*range(1, 101)]
#for num in mylist:
   # if num % 3 == 0 and num % 5 == 0:
       # print(f'FizzBuzz {num}')
  #  elif num % 5 == 0:
         #print(f'Buzz {num}')
    #elif num % 3 == 0:
       #  print(f'Fizz {num}')
   # else:
      #  print(num)



#st = 'Create a list of the first letters of every word in this string'

#mylist = st.split()
#newlist = [fletter[0] for fletter in mylist]
#print (newlist)
#for fletter in mylist:
#     print(fletter[0])

# st = 'Print every word in this sentence that has an even number of letters'
#newlist = st.split()
#for wordcount in newlist:
    # if len(wordcount) % 2 == 0:
       # print('EVEN')
   #  else:
       #  print(f'your word is NOT even it has {len(wordcount)} characters')



    #elif num % 5 == 0:
     #   print('Buzz')
    #elif num % 3 == 0 and num % 5 == 0:
      #  print('FizzBuzz')
    #else:
     #   break




#def myfunc(x):
#    mylist = []
#    for i in range(len(x)):
#        if i % 2 == 0:
#            mylist.append(x[i].upper())
#        else:
#            mylist.append(x[i].lower())
#    return ''.join(mylist)

#print(myfunc('Thisgameistoolong'))

# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a,b)
#    else:
#        return max(a,b)

#print(lesser_of_two_evens(2,4 ))

#Check if the first letter of two words are the same
#def animal_crackers(text):
#    new = text.split()
#    return new[0][0].lower() == new[1][0].lower()

#print(animal_crackers("LevelHeaded DLama"))

# Given 2 integers retun True if the sum of the integers is 20 or if one of the integers is 20. if not return false
#def makes_twenty(a,b):
#    return (a + b) == 20 or a == 20 or b == 20
#print(makes_twenty(3,2))

# Capitalize the first and fourth letter of a word

#def capital_func(word):
#    first = word[:3]
#    second = word[3:]
#    return first.capitalize() + second.capitalize()
#print(capital_func("macbutterfield"))

#reverse a sentence
#def reverse_word(text):
#    word = text.split()
#    reverse = word[::-1]
#    return ' '.join(reverse)

#print(reverse_word('We are ready'))

# Given an integer n, return True if n is within 10 of either 100 or 200

#def almost_there(n):


# Given a list of ints return true if the array contains a 3 next to a 3 somowhere

#def find_33(list):
#    for i in range(0,len(list)-1):
#        if list[i] == 3 and list[i+1] == 3:
#            return True
#    else:
#        return False

#print(find_33([1,3,4,6,4,3,5]))


# given a string, return a string where for every character in the original there are 3 characters
#def paper_doll(text):
#    result = ''
#    for char in text:
#        result += char*3
#    return result

#print(paper_doll('Christopher'))


#BLACK JACK: given 3 integers between 1 and 11, if there sum is less than or equal to 21 return there sum
#if their sum exceeds 21 and there's an eleven reduce the total sum by 1o
#finally, if the sum (even after adjustment exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:
            return sum([a,b,c]) - 10
    else:
        return "BUST"


print(blackjack(5,9,10))










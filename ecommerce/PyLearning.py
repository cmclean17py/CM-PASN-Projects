# course = 'Python for beginners'
# print ('Python' in course)

# print (10 + 3)

# x = 10
# x = x + 3
# x +=3 #same as above

#x = 3 != 2
#print (x)


#price = 25
#print (price > 10 and price < 30)

#temperature = 25

#if temperature > 30:
 #   print ("it's a hot day")
  #  print ("Drink plenty of water")
# elif temperature > 20:
  #  print ("it's a nice day")
# elif temperature > 10:
  #  print ("it's a bit cold")
# print ('Done')

#print ("Hello User")
#weight = float ( input ("Enter your weight? "))
#unit = (input ("(K)g or (L)bs?: "))

#if unit.upper() == "K":
#  converted = weight / 0.45
# print ("Your weight in Lbs is: " + str(converted))
#else:
#   converted = weight * 0.45
#   print ("Your weight in Kg is: " + str(converted))

#elif
    #print ("Done"):




#i = 1
#while i <=10:
 #   print (i * '* ')
  #  i=i+1

# def checkSpeed(speed):
    # if speed <= 70:
#     return "OK"

    # else:
#    speed1 = (speed-70)//5

#  if speed1 <= 12:
#      print(f"Point: {speed1}")

     #    else:
#         print("License suspended")


# checkSpeed(int(input("Enter speed: ")))


#weight = input ("Hello user what is your weight? ")
#conversion = float (weight) * 0.45
#msg = f'Your weight is {conversion} in Lbs'
#print (msg)

#course = "Python for Beginners"
#print (len(course)) finding the legnth of a string
#print (course.upper())
#print (course.replace ("Beginners", "Suckers"))
# #print ("Python" in course)


# n = [5, 2, 5, 2, 2]
#for x in n:
# output = ''
#   for count in range(x):
#      output += 'x'
#  print (output)



# secret_num = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
#    guess = int(input("Guess: "))
#   guess_count += 1
#   if guess == secret_num:
#        print ("You win! ")
#        break
#else:
#   print ("You failed ")


#for i in range(1, 8):
#    for j in range(1, 8):
#        print(i*j, end = '   ')
#    print(' ')





class Person:
    def __init__(self, name):
        self.name = name

    def  __init__(self, sentenace):
        self.sentance = sentenace
        print("What do you want me to say")

john = Person("John Smith")
words = Person("What did you say?  ")
print(john.name)
print(words.sentance)





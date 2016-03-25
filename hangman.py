
##The objective of what I wanted to do was to create a list which
##takes in users word and stores the word in a list
#The if statment checks if the letter entered by the player is in the list

print"Welcome to hang man"
input = raw_input("Enter a word  to be guessed by player 2")
alist=[input]

print len(input)
##loop to display the players words in dashes
print "guess the word player 2 the dashes represent the number of letters in the word \n"
for i in range(len(input)):
    print "-"

input = raw_input("Guess Letter:")
incorrect=[]

if(input in alist):
    print "yes correct "
##add letter to the dash board
else:
    incorrect.append(input)
    print ("incorrect answer")
    input = raw_input("player two your turn :")
if(input in alist):
    print"yes"
    incorrect.append(input)


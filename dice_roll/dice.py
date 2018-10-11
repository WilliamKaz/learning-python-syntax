# make sure random is available
import random
# define the roll variable
player1_roll =  random.randint(1,6)
player2_roll =  random.randint(1,6)
# return the result in the form of a string
print " Player 1: Your roll is " +  str(player1_roll) +  "!"
print " Player 2: Your roll is " +  str(player2_roll) +  "!"

if player1_roll > player2_roll :
  print "Winner is: Player 1"
elif player1_roll < player2_roll :
  print "Winner is: Player 2"
else :
  print "Winner is: No one. Please roll again"
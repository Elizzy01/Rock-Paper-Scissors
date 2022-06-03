import random

# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
choices = ["r", "p", "s"]  

# Computer's random choice
computer = random.choice(choices)
print ("computer: ",computer)
player = None

# Asking for user's input
# verifying user's input

while player not in choices:
   player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n" ).lower()
   print ("player: ",player)
   
if (player == computer):
   print("Wow, it's a tie; try again!") 

elif (player == "r" and computer == "s") or (player =="s" and computer =="p") or (player == "p" and computer == "r"):
      print ("Hurray, you won; computer lost!")
else: 
   print ("Computer won; you lost.")
      

print("\nThanks for playing")

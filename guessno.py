import random
target=random.randint(1,5)

while True:
  userchoice= (input("guess the target:"))
  if(userchoice=="Q"):
    print("quit the game")
    break
  userchoice= int(userchoice)
  if(userchoice==target):
    print("you have guessed right")
    break
  elif(userchoice<target):
    print("you have to guess some greater no")
  else:
    print("you have to guess some smaller no")

print("gameover")

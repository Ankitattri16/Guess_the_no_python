import random
target=random.randint(1,5)

while True:
  userchoice= (input("guess the target:"))
  if(userchoice=="Q"):
    print("quit the game")
    break
  userchoice= int(userchoice)
  if(userchoice==target):
    print("you have guess right")
    break
  elif(userchoice<target):
    print("you have to guess some bigger no")
  else:
    print("you have to guess some smaller no")

print("gameover")
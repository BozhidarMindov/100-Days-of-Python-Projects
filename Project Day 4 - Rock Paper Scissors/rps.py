import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

itemList = [rock, paper, scissors]
userImput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if(userImput > 2 or userImput < 0):
  print("You entered an invalid number")
  
else:
  pickName1 = ""
  if(userImput == 0):
    pickName1 = "rock"
  elif(userImput == 1):
    pickName1 = "paper"
  elif(userImput == 2):
    pickName1 = "scissors"
    
  print(f"\nYou chose {userImput} ({pickName1})")
  print(itemList[userImput])
  
  computerPick = random.randint(0, 2)
  
  pickName2 = ""
  if(computerPick == 0):
    pickName2 = "rock"
  elif(computerPick == 1):
    pickName2 = "paper"
  elif(computerPick == 2):
    pickName2 = "scissors"
    
  print(f"Computer chose {computerPick} ({pickName2})")
  print(itemList[computerPick])

  if(userImput == computerPick):
    print("It\'s a Draw!")
  elif(userImput == 0 and computerPick == 2):
    print("You win!")
  elif(userImput == 2 and computerPick == 0):
    print("You lose!")
  elif(userImput > computerPick):
    print("You win!")
  elif(computerPick > userImput):
    print("You lose!")




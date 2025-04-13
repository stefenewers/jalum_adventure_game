print("************************************************")
print("Welcome to the JALUM Adventure Game!")
print("Developed by S. Ewers Gaming Studios")
print("************************************************")
print("Your mission is to find the treasure.")
print("You will be asked a series of questions to guide you through the game.")
print("You will have 10 health points to start with.")
print("If you reach 0 health, you lose the game.")
print("If you make it through the game and find the treasure, you win!")
print("Let's start the adventure!")
print("************************************************")

# Game starts here
name = input("What name do you go by, explorer? ")
age = int(input("How old are you? "))
health = 10
print(f"Welcome to the game {name}!")

if age >= 18:
  print("You are old enough to play for sure.")
  
  wants_to_explore = input("Do you want to explore? Enter (yes or no) ").lower()
  if wants_to_explore == "yes":
    print("You are starting with", health, "health points.")
    print("Let's play!")

    left_or_right = input("You just exited a dark cave with two paths infront of you. Would you like to go Left or Right? - Enter (left or right) ").lower()
    if left_or_right == "left":
      ans = input("Nice, you followed the path and found a lake... Do you want to swim across the lake or try to run around it? - Enter (swim or run) ").lower()

      if ans == "run":
          print("You ran around the lake and reached the other side safely.")
      else:
          print("You managed to swim across, but were bit by a crocodile and lost 5 health points.")
          health -= 5

      ans = input("You notice an old battered house across the grass priarie. You also noticed a Land Rover that seems functional and can get you home. Which do you choose? Enter (Walk to house or Enter Land Rover) ").lower()
      if ans == "walk to house":
          print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health.")
          health -= 5
    
          if health <= 0:
              print("You now have 0 health and you lost the game...")
          else:
              print("You have survived and found the treasure... You win!")

      else:
          print("The Land Rover was rigged with a trap. It exploded. You have lost...")

    else:
      print("You fell off a cliff. The game is Game Over!")
  else:
      print("Sorry - Your loss. We hope to see you soon!...")
else:
  print("You are not old enough to play - Sorry future explorer.")

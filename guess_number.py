import random

def guess(number):
 
  random_number = random.randint(1, number)
  print(random_number)
  guess = 0;
  attempts = 1;
  while guess is not random_number:
    try:  
      guess = int(input(f"Guess a number between 1 and {number}: "))
      if (guess) is random_number:
        print(f"Yaayy!!! you guessed the number {random_number} correctly.")
      else:
        print("Sorry, guess again")  
      if attempts == 3 and guess != random_number:
        print("Oops!!! you've made 3 attempts")
        return

      attempts += 1
    #quit program with "ctrl + c"
    except KeyboardInterrupt:
      return
    except:       
      print("Please make sure to enter a number. Try again.")

guess(10)     

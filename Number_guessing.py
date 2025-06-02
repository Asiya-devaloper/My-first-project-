import random #random number generate cheyyadam ki 
Secret_number =random.randint(1,100)#computer oka number ni pick chestundhi
while true:
      guess =int(input ("guess a number between 1 and 100:"))# user guess 
      if guess <secret _number :
           print ("Too low!try again.")
      elif guess > secret _number:
           print ("Too high!try again.")
      else:
           print ("Congratulations!you guessed it right.")
          break # correct guess ayithe loop stop 
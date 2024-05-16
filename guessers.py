import random;
print("THE RANDOM NUMBERS GIVEN FOR YOU TO GUESS ARE NUMBERS LESS THAN OR EQUAL TO THE CEILING NUMBER YOU PROVIDE!!!");
ceilNo= input("Please enter your ceiling number ");

if ceilNo.isdigit():
    ceilNo = int(ceilNo)
    if ceilNo <= 0 :
        print("Please Enter a number greater than 0 next time");
        quit()
else :
    print("Please enter a number next time")
    
randomNo = random.randint(0,ceilNo);

guesses = 0
    
while guesses < 3 :
    guesses +=1
    user_guess = input("Please enter your guess ");

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == randomNo :
            print("You got it right!👍")
            quit()
    else :
        print("Please Enter a number")
        continue
   
    if user_guess <  randomNo :
        print ("Sorry your guess is below the correct answer")
        continue

    else  : 
        print ("Sorry your guess is higher than the correct answer")
        continue




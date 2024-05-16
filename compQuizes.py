prompt = input("Let's test your computer knowledge!(yes/no)? ").lower()

if prompt != "yes":
    print("Okay, maybe next time! 😒 ")
    quit()


score =0
answer = input("Quiz 1:  What does CPU stand for? " ).lower()

if answer == "central processing unit" :
    print ("Correct!😁👍")
    score+= 1
else :
    print("Incorrect! 😒")
    print("The correct answer is 'Central Processing Unit' ")


answer = input("Quiz 2:  What does GPU stand for? " ).lower()

if answer == "general processing unit" :
    print ("Correct!😁👍")
    score+= 1
else :
    print("Incorrect! 😒")
    print("The correct answer is 'general Processing Unit' ")


answer = input("Quiz 3:  What does RAM stand for? " ).lower()

if answer == "random access memory" :
    print ("Correct!😁👍")
    score+= 1
else :
    print("Incorrect! 😒")
    print("The correct answer is 'random access memory' ")


answer = input("Quiz 4:  What does UPS stand for? " ).lower()

if answer == "uninterruptible power supply" :
    print ("Correct!😁👍")
    score+= 1
else :
    print("Incorrect! 😒")
    print("The correct answer is 'Uninterruptible power supply' ")


total = score

print (f"You got {total} quizes corect out of the total 4")

avg = total/4 *100

print (f"Your average is{avg}")

print("Thanks for playing! 😁😎")
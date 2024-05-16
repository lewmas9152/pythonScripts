import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = random.randint(1, 10)
MAX_OPERAND = random.randint(10, 20)

def generate_question():
    operator = random.choice(OPERATORS)
    operand1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    question = str(operand1) + " " + operator + " " + str(operand2)
    answer = eval(question)
    return question, answer


wrong = 0
correct = 0

print("Press enter to start the quiz")
start = time.time()

print("---------------------------")
for i in range(10):
    question, answer = generate_question()
    while True:
        guess = input("question" +" #" +str(i+1) +": " + question +": ")
        if guess == str(answer):
            correct +=1
            break
        wrong += 1

end = time.time()
total_time = round(end - start,2)     
print("---------------------------")
print("You got", correct, "correct answers")
print("You got", wrong, "wrong answers")
print("Total time taken", total_time)
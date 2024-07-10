with open("story.txt", "r") as f:
    story = f.read()

start_char = "<"
end_char = ">"
start_point = -1

words =set()

for i, char in enumerate(story):
    if char == start_char:
        start_point = i
    
    if char == end_char and start_point != -1:
        words.add(story[start_point:i+1])
        start_point = -1

answers = {}

for word in words:
    user_input = input("Enter a word for "+word+": ")
    answers[word] = user_input

for word in words:
    story = story.replace(word, answers[word])

print(story)   
        
    
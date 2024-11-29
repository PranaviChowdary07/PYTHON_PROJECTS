import random 
def set_difficulty(level_chosen):
    if level_chosen == 'Easy':
        attempts = 10
    else:
        attempts = 5
print("Let me think of a number between 1 to 100.")
answer = random.randint(1,100)
print(answer)
level = input("Choose level of dificulty .... Type 'Easy' or 'Hard': ")
set_difficulty(level)


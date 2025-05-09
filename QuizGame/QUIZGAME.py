questions=("9&10",
           "1&2?",
           "2&3?",
           "4&5?")

options=(("A.9.5","B.5","C.6"),
         ("A.2","B.3","C.1.5"),
         ("A.1","B.2.5","C.4"),
         ("A.3","B.4.5","C.2"))
answers=("A","C","B","B")
guesses=[]
score=0
question_num=0

print("ENTER RIGHT NUMBER B/W NUMBERS!\n")
for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("ENTER (A,B,C,D):  ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        print('CORRECT')
        score+=1
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is correct answer")
    question_num=question_num+1


print("-----------")
print("- RESULTS -")
print("-----------")

print("answers:\n",end="")
print('CORRECT ANSWERS:')
print("YOUR ANSWERS:")


for guess in guesses:
    print(guess, end=" ")
print()


for answer in answers:

    print(answer,end=" ")
print(" ")

score=int(score/len(questions)*100)
print(f"YOUR SCORE IS {score}%")
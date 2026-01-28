import random
stages=["""
   ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|___

""", """
 _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___
        ""","""
     _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |     
     |
 ____|___""","""
  ____________
     |/      |
     |      (_)
     |      \|/
     |      
     |      
     |
 ____|___""","""
  ____________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___
 ""","""
  ____________
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___
 """
        ]

word_list=["camel","computer","baboon","papaya","car","rhino"]
lives=6

chosen_word=random.choice(word_list)
#print(chosen_word)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
game_over=False
correct_word=[]

while not game_over :
    guess = input("enter a letter ".lower())
    display = ""

    #print(guess)

    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter

        else:
            display+="_"
    print(display)
    if guess not in  chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")

    if "_" not in display:
        game_over=True
        print("You win")
    print(stages[lives-1])




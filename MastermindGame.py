# -*- coding: utf-8 -*-
## MASTERMIND GAME by Birce 

import random 

Code_length = 4 
Game_turncount=0 

Set_of_colors = ['red','green', 'blue', 'magenta', 'yellow', 'purple', 'brown', 'orange']
Key_pegs= ['black', 'white']
DoubleRight_peg = Key_pegs[0]
ColorRight_peg= Key_pegs[1]

Color_code = random.sample(Set_of_colors, k = Code_length)

print(Set_of_colors)
print(Color_code)

Feedback = []
guess_code = []  



def Master_Feedback():
     
    for slot in range(len(Color_code)):
       
        if  guess_code[slot] == Color_code[slot]:
            print(Key_pegs[0])
            Feedback.append(Key_pegs[0]) 
        
        
        elif guess_code[slot] in  Color_code:
            print(Key_pegs[1])
            Feedback.append(Key_pegs[1])
        
            
    return Feedback 

def Guess_code():    
    
    for slot in range(len(Color_code)):
        guess_code = []
        new_guess = input('please Guess Color: ')
        
        guess_code.append(new_guess)
        
    
    print(guess_code)
    return guess_code
    

terminal_result =  [Key_pegs[0], Key_pegs[0], Key_pegs[0], Key_pegs[0]]
Guess_code()
Master_Feedback()

        
while Game_turncount<8: 
    
    
    if Feedback != terminal_result:
         
        Guess_code()
        Feedback = []
        Master_Feedback()
        Game_turncount += 1
    elif  Feedback == terminal_result:
        print('Congrats. You did it!')
        break
else:
    print('Game Over. Please try again.')
     

        





import random as rd  

comput_choice = rd.choice([0, -1, 1])
youstr = input("Enter you choice S / G / W  : ")
youdict = {'s' : 1 , 'w': -1, 'g': 0}

reversedict = {1: 's', -1: 'w', 0: 'g'} 
you = youdict[youstr]

print("\n\nComputer's choice: ", reversedict[comput_choice], "\nYour Choice : ", reversedict[you] )

print("\n")
if (comput_choice == you):
    print("It's a tie!")
else:
    if (comput_choice == -1 and you == 1):
        print("You wins!")
    elif (comput_choice == -1 and you == 0):
        print( "Computer Wins!")
    elif (comput_choice == 1 and you == -1):
        print("Computer wins!")
    elif (comput_choice == 1 and you == 0):
        print("You wins!")
    elif (comput_choice == 0 and you == 1):
        print("Computer wins!")
    elif (comput_choice == 0 and you == -1):
        print("Computer wins!")
    else:
        print("Something is wrong!")


'''
    if(comput_choice - you == -1) and (computer_choice - you == 2):
        print("Computer wins!")
    else:
        print("You wins!")
'''
    






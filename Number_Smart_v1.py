import easygui
from random import randint
USER_NAME = 0
user_total = 20
user_prog = 0
question = 0
while USER_NAME == 0:
    USER_NAME = easygui.enterbox("What is your name?")
    easygui.msgbox("Hello " + USER_NAME)
    easygui.msgbox("This is a game to test and improve your knowledge of numbers from 0-100, this is level one")
    user_prog = 1
    break

while user_total != 20:
    if user_total == 10:
        easygui.msgbox("Congrats! You have passed the first level! Level 2 will be harder since the numbers are now between 0-1000. GET READY!")
        user_prog = 2
        
    while user_total != 20:
        number_A = 0
        number_B = 0
        question = 0
        while user_prog == 1 or user_prog == 2:
            if user_prog == 1:
                number_A = str(randint(1,100))
                number_B = str(randint(1,100))

            elif user_prog == 2:
                number_A = str(randint(1,1000))
                number_B = str(randint(1,1000))

            #Random question with values 1 and 2, which ask the biggest/smallest number questions
            question = randint(1,2)
            user_answer = 1
            break

        if question == 1:
            while user_answer != 0:
                user_answer = 0
                user_answer = easygui.enterbox("Which number is bigger?: {} or {} :Type the answer using your keyboard" .format(number_A, number_B))
                if number_A > number_B:
                    if user_answer == number_A:
                        easygui.msgbox("CORRECT!, You got it right on the spot!")
                        user_total += 1
                        break
                        
                    elif user_answer == number_B:
                        easygui.msgbox("You were so close!, it was number {} ".format (number_A))
                        break
                    else:
                        easygui.msgbox("You didn't type any of the numbers, try again")
                        
                elif number_B > number_A:
                    if user_answer == number_B:
                        easygui.msgbox("Good Job!, you were 100% Correct, KEEP GOING!")
                        user_total += 1
                        break
                    
                    elif user_answer == number_A:
                        easygui.msgbox("Man you had it so close!, the correct answer was " + number_B)
                        break
                    else:
                        easygui.msgbox("You didn't type any of the numbers, try again")
                else:
                    if user_answer == number_A or user_answer == number_B:
                        easygui.msgbox("They were the same numbers!, so none of them was bigger")
                    break
                        
        elif question == 2:
            while user_answer != 0:
                user_answer = 0
                user_answer = easygui.enterbox("Which number is smaller?: {} or {} :Type the answer using your keyboard" .format(number_A, number_B))
                if number_A < number_B:
                    if user_answer == number_A:
                        easygui.msgbox("THATS RIGHT!, You're very smart indeed!")
                        user_total += 1
                        break
                    
                    elif user_answer == number_B:
                        easygui.msgbox("So clooooooose!!, the right answer was " + number_A)
                        break
                    else:
                        easygui.msgbox("You didn't type any of the numbers try again")
                        
                elif number_B < number_A:
                    if user_answer == number_B:
                        easygui.msgbox("100% Correct, you’re rampaging through the questions!”)")
                        user_total += 1
                        break
                    
                    elif user_answer == number_A:
                        easygui.msgbox("Oh man! At least you tried, the correct answer was " + number_B)
                        break
                    else:
                        easygui.msgbox("You didn't type any of the numbers try again")
                else:
                    if user_answer == number_A or user_answer == number_B:
                        easygui.msgbox("They were the same numbers!, so none of them were smaller")
                    break
        # user_answer is set to 0 to end both loops, break is also a half measure in case user_answer does not end the loop.
        user_answer = 0
        break
    
#END OF GAME SCREEN, AUTOMATICALLY TERMINATES GAME
easygui.msgbox("GOOD JOB {}! You finished both level 1 and 2 of this game, feel free to try again if you want to improve your skills even more!".format(USER_NAME))






                        
                                               

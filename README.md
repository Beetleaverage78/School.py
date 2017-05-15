# Number_SMart_GAme.V1
###### This is just a game to improve your knowledge of numbers, starting at 1-100.
## Import Features
- Encourage users to continue playing the game
- Has Two levels, each with different difficulty settings.
- Has a flexible and robust feedback system... i think

This program is open sourced, and easily customizable to your preferences.
just need a bit of python knowledge. The easygui module is already installed.
But if that doesn't work, an installer is provided just in case.

**[Additional Info]** Modifying this will provide another level to the program, for the users to beat.

**EXAMPLE TEMPLATE**
Only this part of the code should be edited, but you don't need this tutorial if your good at python. Heres an example of adding a third level to the program
```py
#Change the user_total of all while loops to 30 if you add another level.
#Then to 40 if you have another level etc.
while user_total != 20:
    if user_total == 10:
        easygui.msgbox("Congrats! You have passed the first level! Level 2 will be harder since the numbers are now between 0-1000. GET READY!")
        user_prog = 2

    elif user_total == 20:
        easygui.msgbox("Yooo lit you made it passed level 2, now its gonna be harder at level 3!")
        user_prog = 3
    #Under here make another elif setting user_prog to 3 or 4 depending on levels.
    #Also add another congrats message :D
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
            #You can add another line of code to make more levels.
            elif user_prog == 3:
                number_A = str(randint(1,10000))
                number_B = str(randint(1,10000))
            #Random question with values 1 and 2, which ask the biggest/smallest number questions
            question = randint(1,2)
            user_answer = 1
            break
```
## Good luck! - edit the program to your own use!
= btw I just made this cus i had to hahah, it will probs be outdated soon.
~~suppose to be done at school~~

*BUT WHO CARES*

A Great Coder Once Said
> Who Gives a f*** <

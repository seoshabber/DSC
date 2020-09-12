import random
import easygui

name=easygui.enterbox("What is your name?")
easygui.msgbox("Ok, "+name+"!\nLet's play 21 game.")
answer= random.randint(1,21)
card1=random.randint(1,13)
more=easygui.buttonbox("Your first card is "+str(card1)+"\nDo you want more?", choices=['yes','no'])
if more == 'yes':
    card2=random.randint(1,13)
    easygui.msgbox("Your second card is "+str(card2)+"\nCheck your result")
    result=card1+card2
else:
    easygui.msgbox("Ok, check your result")
    result=card1
if result<=21:
    if result>answer:
        easygui.msgbox("Your final result is "+str(result)+"\nComputer's card was "+str(answer)+".\nYou win!")   
    else:
        easygui.msgbox("Your final result is "+str(result)+"\nComputer's card was "+str(answer)+".\nYou lose!")
else:
    easygui.msgbox("Your final result is "+str(result)+". It is over 21, so you lose.\nComputer's card was "+str(answer))

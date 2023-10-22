#Make rock paper sissor game using
import random 

def user():
    choice= input('what is your choice (reck , paper , sissor [wrire (r,p,s )])').upper()
    if choice not in ["R", "P", "S"]:
        return user()

    return choice
def isWin(user, com ):

    if user== com:
        isTie( user, com)
        return

        
    
    elif com == 'R' and user=="P" or com =='P'and user== "S" or com== "S" and user== "R" :
        play_again=input( f"you win!, you choosed :{user} and computer choosed {com},wanna play again(y/N)?: ") 
    else :
        play_again=input(f"You loose! you choosed :{user} and computer choosed {com}, try again (y/n): ")
    if play_again.upper()=="Y":
        return True
    else:
        return False
def isTie(user, com) :
    if com == user:
        play_again=input( f"This is tie computer also choosed {com} wanna play aginn( Y/N ): ")
    if play_again.upper()== "Y" :
        main()
    else:
        print("Thanks for playing see you soon ")
    


def main():
    user_choice= user()
    com= random.choice(["R", "P", "S"])
    playagain=isWin(user_choice, com)
    if playagain:
        main()
    else:
        print("thanks for playing see you soon!!!")

main()
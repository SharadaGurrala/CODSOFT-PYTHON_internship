import random

def get_user_choice():
    choice = input("Enter your choice (rock,paper,scissor)\n").lower()

    while choice not in (['rock','paper','scissor']):
        print("invalid choice! try again")
        choice = input("Enter your choice (rock,paper,scissor)\n").lower()
        return choice

    return choice


def get_computer_choice():
    return random.choice(['rock','paper','scissor'])
    

def get_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif(user_choice=='rock' and computer_choice=='scissor') or \
        (user_choice=='paper' and computer_choice=='rock') or \
        (user_choice=='scissor' and computer_choice=='paper'):
        return "user"
    else:
        return "computer"


def get_result(user_choice,computer_choice,winner):
    print(f"your choice is {user_choice} and computer choice is {computer_choice}\n")
    if(winner== "tie"):
        print("game tie!")
    elif (winner == "user"):
        print("you win")
    else:
        print("you lose")
    
def main():

    user_score=0
    computer_score=0
    while True:

        user_choice =  get_user_choice()
        computer_choice = get_computer_choice()
        winner = get_winner(user_choice,computer_choice)
       
        get_result(user_choice,computer_choice,winner)
        
        if(winner == 'user'):
            user_score +=1
        elif (winner == 'computer'):
            computer_score +=1
        

        print(f"score :- you :{user_score}  &  computer :{computer_score}\n")
        
        player=input("want to continue game? (yes/no): ").lower()
        if player !='yes':
           break

    print("thanks for playing\n")
if __name__=="__main__":
    main()






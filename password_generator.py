import random
import string



def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
        
    return password    
    


def main():
    length = int(input("Enter the length that you want to generate password: \n"))

    password = generate_password(length)

    print(f"The generated password {password}")
if __name__ == "__main__" :
    main()   
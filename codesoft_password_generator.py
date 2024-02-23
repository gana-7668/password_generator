import random
import string

while True:
    def generate_password(length=15):
        characters= string.ascii_letters + string.digits + string.punctuation

        password="".join(random.choice(characters) for _ in range(length))

        return password

    if __name__=="__main__":
        password_length=15

        try:
            password_length=int(input("enter desired password length (defalt password length is 15)::"))

        except ValueError:
            print("invalid input. using default password length:")

        if password_length<=0:
            print("password length should be greater than 0. using default password length: ")
            password_length=15

        generate_password=generate_password(password_length)
        print(generate_password)

        

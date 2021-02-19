#Write a program which accept one number for user and check whether number is prime or not.
# taking input from user

def Chkprime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
    
        
def main():
       
        num = int(input("Enter any number: "))
       
        (Chkprime(num))

if __name__ == "__main__":
    main()       
       
       
       
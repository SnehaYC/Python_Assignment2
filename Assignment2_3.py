#Write a program which accept one number from user and return its factorial.
 
def factorial(no):
    fact = 1
    for i in range (1,no+1):
        fact = fact * i
    return fact
  
def main():
    num = int(input("Enter the number: "))

    facto =(factorial(num))
    print("Factorial of number is :",facto)
    
if __name__ == "__main__":
    main()     

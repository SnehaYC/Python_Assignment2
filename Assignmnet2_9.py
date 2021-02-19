#Write a program which accept number from user and return number of digit in that number.
def nodigit(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count
def main():
    value = int(input("Enter number :"))
    
    ret = nodigit(value)
    print("The number of digits in the number are:",ret)    

if __name__ == "__main__":
    main() 
    
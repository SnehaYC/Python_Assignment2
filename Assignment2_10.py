#Write a program which accept number from user and return addition of digits in that number.
def getSum(n):  
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum

def main():
    value = int(input("Enter number :"))
    
    ret=getSum(value)
    
    print("Addition :",ret)
    
if __name__ == "__main__":
    main()

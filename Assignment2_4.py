#Write a program which accept one number for user and return addition of its factors.


def factor(num):
    
    factor = []
    for i in range(1,num+1):
        if num%i==0:
           factor.append(i)
    print ("Factors are:",(factor))     
    return sum(factor)
     
    
def main():  
    num = int(input("Enter the number: "))

    facto =(factor(num))
    print("Addition of Factors is :",facto)
    
    
if __name__ == "__main__":
    main()    


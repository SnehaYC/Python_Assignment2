#Write a program which accept one number and display below pattern.
#Input :5 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
def display(n):
    for i in range(0, n):  
        for j in range(0, n):  
            print("* ", end="")       
        print()
def main():
    value = int(input("Enter number :"))
    
    display(value)
    
if __name__ == "__main__":
    main()     
        
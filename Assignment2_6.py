#Write a program which accept one number and display below pattern.
#Input:5
#* * * * *
#* * * * 
#* * * 
#* * 
#* 

def display(cnt):
    for i in range(cnt + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
def main():
    value = int(input("Enter number :"))
    
    display(value)
    
if __name__ == "__main__":
    main() 


    

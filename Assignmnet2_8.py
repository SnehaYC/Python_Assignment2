#Write a program which accept one number and display below pattern.
#Input:5
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

def display(cnt):
    for i in range(1, cnt + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')
    
def main():
    value = int(input("Enter number :"))
    
    display(value)
    
if __name__ == "__main__":
    main()         
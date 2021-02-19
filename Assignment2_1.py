#Create a module named as Arithematic which contains 4 functions as Add()for addition,Sub()for substraction,Mult() for multiplication and Div() for division.
#All functions accepts two parameters as number and perform the operation.
#Write a python program which call all the functions from Arithematic module by accepting the parameters from user.
import arithematic
def main():
    print("Enter first number:")
    value1 = int(input())
    
    print("Enter second number:")
    value2 = int(input())
    
    ret1 = arithematic.Addition(value1,value2)
    ret2 = arithematic.Substraction(value1,value2)
    ret3 = arithematic.Multiplication(value1,value2)
    ret4 = arithematic.Division(value1,value2)
    
    print("Addition is:",ret1)
    print("Substraction is:",ret2)
    print("Multiplication is:",ret3)
    print("Division is:",ret4)
    
if __name__ == "__main__":
    main()     
    
    
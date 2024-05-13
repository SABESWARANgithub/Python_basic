'''
Also known as "Errror handling"
try block & expect block & finally block;by using these blocks,we can acheive exceptional handling
major types of error in python- 3 types :  i)Compile-time/Syntax error
                                          ii)Run-time error - error b^n the run time(b^n --- & output page)
                                         iii)Logical error
try block - use to find the errors & to handle before the execution itself to avoid the error
if we give like this ..... as e;in that e the reason of error will store.can give any instead of e
'''

'''
#ZeroDivision Error
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))     #if any no is used to divide by zero:it shows ZeroDivisionError
    result=a/b
    print(result)
except ZeroDivisionError as e:
    print("the natural no's are not able to divide by zero",e)
'''

'''
try:
    a=int(input())
    b=int(input())
    c=a+b
    print(d)
except ValueError as strE:        #if we give str instead of int,shows ValueError
    print("ValueError,",strE)
except NameError:              #when we call/process one var,but the var is not even declared,shows NameError
    print("nameError")
except Exception:
    print("Some Error had accoured")
finally:
    print("Done")


#type error
try:
    a=int(input("enter number"))
    b=input("Enter str/no:")
    c=b/a
    print(c)
except TypeError as e:              #when the integer is try to do divide or any mathematical operation bwith str,it shows TypeError
    print("TypeError,",e)
except Exception as  e:
    print("Some error had occured",e)
finally:
    print("Done")
'''

#by giving the print func in the try block is not efficient,give it in last is best
try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))  # if any no is used to divide by zero:it shows ZeroDivisionError
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("the natural no's are not able to divide by zero", e)
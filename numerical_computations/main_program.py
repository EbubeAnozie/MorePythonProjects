import project_module.compute_error as ce
import project_module.compute_differentiation as cd



"""This is the main program that integrates all the numerical functions."""


def choose_operation():
    not_valid = True
    while not_valid:
        try:
            user_input = int(input("""Enter the number corresponds to the operation you want to perform; e.g. 1 or 2 or 3 ...
                               1. Numerical Errors
                               2. Numerical Differentitation
                               3. Numerical Integration
                               \nEnter: """))
            return user_input
        except:
            print("Invalid input")
            not_valid == True
            

def numerical_error():
    not_valid = True
    while not_valid:
        try:
            n = float(input("Enter the exact value: "))
            m = float(input("Enter the approximation: "))
            print(f"Absolute error: {ce.abs_err(n,m)}")
            print(f"Relative error: {ce.rel_err(n,m)}")
            return None
        except:
            print("invalid input")
            # check if user wants to perform another operation
            continue
        #finally:
            #pass # check if the user wants to perform another operation
        



def numerical_differentiation():

    user_input = -1
    while user_input not in operation_number_list: # modify this line
        user_input = int(input("""Enter the number corresponds to the numerical differentiation you want to perform; e.g. 1 or 2 or 3 ...
                           1. Taylor differentiation
                           2.
                           3.
                           """))
    return user_input



def perform_operation(number):
    not_found = True
    while not_found:
        if number == 1:
            numerical_error()
        else:
            print("Operation number not found")
            number = choose_operation()
            continue
                
        
        



operation_number_list = [i for i in range(1, 4)]

if __name__ == "__main__":
    number = choose_operation()
    perform_operation(number)
    


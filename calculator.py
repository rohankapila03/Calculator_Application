# calculator.py
# Rohan Kapila, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
num_1 = int(input('Enter First Number:'))  #assign an input value for the first number that must be a integer
operator_1 = input('Enter First Operator:')  #assign first operator that can be input by user
num_2 = int(input('Enter Second Number:')) #assign integer input value for second number
operator_2 = input('Enter Second Operator:') #assign a input value for the second operator
num_3 = int(input('Enter Third Number:')) #assign a integer value as input for third integer

if operator_1 == '*':                               #determines if the first operator is a * if not move to next operator choice
    if operator_2 == '*' or operator_2 == '/':      #if first operator * this line will occur and determine the second operator as either * or /
        if operator_2 == '*': 
            result = (num_1 * num_2 * num_3)        #if operator 1 and operator 2 is * this line will occur which becomes the equation for result
        else:
            operator_2 == '/' 
            result = (num_1 * num_2 // num_3)        #if first operator is * and second operator is / this line will occur and be the equation for result
    else:
        operator_2 == '+' or operator_2 == '-'      # determines second operator isnt * or / so must be + or -
        if operator_2 == '+':
            result = ((num_1 * num_2) + num_3)      #if first operator * and second operator + this line will run and be the equation that determines result
        else:
            operator_2 == '-'                       #if operator 2 isnt + then it will be -
            result = ((num_1 * num_2) - num_3)      #if operator 1 * and operator 2 - this will be the new value for result
elif operator_1 == '/':                             #if first operator not * check if /
    if operator_2 == '*' or operator_2 == '/':      #check if operator 2 is * or /
        if operator_2 == '*':
            result = (num_1 // num_2 * num_3)        #run this line as new result value if operator 1 is / and operator 2 is *
        else:
            operator_2 == '/'                       #if operator 2 not * test if /
            result =  (num_1 // num_2 // num_3)       #store this as result value if all operator /
    else:
        operator_2 == '+' or operator_2 == '-'      # if opeartor 2 not * or / check if + or -
        if operator_2 == '+':
            result = ((num_1 // num_2) + num_3)      #if operator 1 / and operator 2 + store as result value used to ensure order of operation done
        else:
            operator_2 == '-'                       #if operator 2 not + must be - because all other operation already tested
            result = ((num_1 // num_2) - num_3)      #store as result if operator 1 / and operator 2 -
elif operator_1 == '+':                             #check if first operator +
    if operator_2 == '*' or  operator_2 == '/':     #check if second operator is * or / only if first operator +
        if operator_2 == '*':
            result = (num_1 + (num_2 * num_3))      #if first operator + and second operator * store as result, this ensures order of operations done
        else:
            operator_2 == '/'                       #second operator not * so must be / only if line 42 holds true
            result = (num_1 + (num_2 // num_3))
    else:
         operator_2 == '+' or operator_2 == '-'     #if second operator not * or /, must be + or -
         if operator_2 =='+':
            result = (num_1 + num_2 + num_3)        #store this line as result if operator 1 is + and operator 2 is +
         else:                                      #if line 49 true and operator 2 isnt +, second operator must be -
             operator_2 == '-'
             result = (num_1 + num_2 - num_3)       #store this line as result if operator 1 is + and operator 2 is -
elif operator_1 == '-':                             #check if operator 1 is -
    if operator_2 == '*' or operator_2 == '/':      #check if operator 2 is * or /
        if operator_2 == '*': 
            result = (num_1 - (num_2 * num_3))      #store as result if operator 1 is - and operator 2 is *, this ensures order of operations are accounted for
        else:                                       #if line 56 holds true and operator 2 isnt * this else statement will occur and operator 2 will be /
            operator_2 == '/' 
            result = (num_1 - (num_2 // num_3))        #store this as result if operator 1 is - and operator 2 is /, ensure order operation is done
    else:                                           #if line 56 false, then operator 2 will either be + or -
        operator_2 == "+" or operator_2 == '-'
        if operator_2 == '+':                       #check if input operator 2 is +
            result = (num_1 - num_2 + num_3)        #if input operator 2 is + and operator 1 is -, store this as result
        else:                                       #if line 63 true but 64 false then operator 2 must be -
            operator_2 == '-'
            result = (num_1 - num_2 - num_3)        #if operator 1 is - and operator 2 is - store this expression as result
 
print(f'Entered Expression:: {num_1} {operator_1} {num_2} {operator_2} {num_3}')    #print expression by displaying all of users inputted values
print(f'your final answer = {result}')              #print users final results by printing stored value of result


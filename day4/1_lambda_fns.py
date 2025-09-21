# lambda function is a small anonymous function( no name needed) , no return statement needed
# automatically returns the result of the expression
# can take any number of arguments, but only one expression
# need the lambda keyword to define it

# syntax: lambda parameters: expression

#ex 1 ✅
add = lambda x, y: x + y
print(add(10, 20))  

#ex 2 ✅
answer = lambda a, b: a * b
print(answer(5, 4))



#often used with higher-order functions like map(), filter(), and reduce()

# python day4/1_lambda_fns.py
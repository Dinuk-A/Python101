# 1. basic pattern ✅
'''
*
**
***
****
*****
'''

print("basic stars")
for x in range (1,6):
    print('*'*x)
    
# 2. reverse pattern ✅
'''
*****
****
***
**
*
'''

print("reverse stars")
count = 5
while count > 0:
    print('*' * count)
    count -= 1

#3. pyramid pattern ✅
'''
   *
  ***
 *****
******* 
'''

print("basic pyramid")
row_count = 4
for n in range(1,row_count+1):
    print(' '*(row_count-n) + '*'*(2*n-1))
   
#with while ✅
print("basic pyramid with while") 
#use a custom counter because while doesn't have a built-in index counter like for
y=1
while y<= row_count:
    print(' '*(row_count-y) + '*'*(2*y-1))
    y+=1
    

#4. left aligned basic pattern
'''
    *
   **
  ***
 ****
*****
'''

print("right aligned basic pattern")

rows = 5
counter = 0
while counter < rows:
    spaces= ' ' * (rows-counter-1)
    stars = '*'*(counter+1)
    print(spaces + stars )
    counter+=1
    
#right aligned upside down pattern ❌
#upside down pyramid ❌

# python day2/8_star_patterns.py
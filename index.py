#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max(a,b,c)

print(max_num(3,4,5)) #5

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(nums):
    result = 1
    for num in nums:
        result *= num
    return result   

print(mult_list([1,2,3,4])) #24
   

#Write a Python function called rev_string() to reverse a string.

def rev_string(my_string):
    return my_string[::-1]

print(rev_string("hello")) #olleh
    

#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(x,y,z):
    return x in range(y,z+1)


print(num_within(3,2,4)) #True


##Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.

def pascal(n):
    triangle = [[1], [1,1]]
    if n < 1:
        print("invalid input")
    elif n == 1:
        print(triangle[0])
    else:
        row_num = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_num - 2]  
            length = len(row_prev)+1
            for i in range(length):
                if i == 0 or i == length-1:
                    row.append(1)
                else:
                    row.append(triangle[row_num-2][i-1] + triangle[row_num-2][i])
            triangle.append(row)
            row_num += 1

        for row in triangle:
            print(row)

pascal(5)

                                         

'''
Note: This exercise should be done using only the statements and other features we have learned so far.

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the
next line.

Write a function that draws a similar grid with four rows and four columns.

'''


def draw_grid():
    hor_line = "+ - - - - + - - - - +"
    ver_line = "|         |         |"
    for i in range(2):
        print(hor_line)
        for j in range(4):
            print(ver_line)
    print(hor_line)


def draw_four_row_column_grid():
    hor_line = "+ - - - - + - - - - + - - - - + - - - - +"
    ver_line = "|         |         |         |         |"
    for i in range(4):
        print(hor_line)
        for j in range(4):
            print(ver_line)
    print(hor_line)


#draw_grid()
draw_four_row_column_grid()

num_rows = int(input("Enter the number of rows : "))
num_columns = int(input("Enter the number of columns : "))

row = 1
column = 1

while row <= num_rows:
    if row == 1 or row == num_rows:
        print('*' * num_rows)
    
    elif column == 1 or column == num_columns:
        print('*' + ' ' * (num_columns - 2) + '*')
    else:
        ...
    row += 1


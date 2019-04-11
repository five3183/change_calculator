'''
    Simple function go get optimal change
'''

CURRENCY = [('Hundreds', 100), ('Fifties', 50), ('Twenties', 20), ('Tens', 10), ('Fives', 5), ('Ones', 1), ('Quaters', .25), ('Dimes', .10), ('Knickles', .05), ('Pennies', .01)]

def get_change(cost, paid):
    '''
        input = cost of item amount paid
        output = The optimal change
    '''
    # Get the difference
    difference = paid - cost
    if difference == 0:
        return 'Exact amount'
    elif difference < 0:
        return 'Not enough currency'
    else:
        # loop through curency object
        for money in CURRENCY:
            # Check to see if the difference is greater or equal to zero
            if difference - money[1] >= 0:
                # Get the number of each
                num = int(difference / money[1])
                difference = difference - (num * money[1])
                print(f'Number of {money[0]} : {num}')
               

get_change(77.33, 100)

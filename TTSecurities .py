#
#
# TT Securities    
#
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

# choice 0
def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

# choice 1
def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

# choice 2
def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]


# choice 3   
def avg_price(prices):
    '''Finds the average price of the given list of prices
    '''
    sum=0
    for i in prices:
        sum+=i
    result=sum/len(prices)
    return result
    
# choice 4
def std_dev(prices):
    '''Finds the standard deviation of the given list of prices
    '''
    sum=0
    for i in range(len(prices)):
        a=prices[i]-avg_price(prices)
        b=a**2
        sum+=b
        
    std_dev=math.sqrt(sum/len(prices))
    return std_dev

# choice 5
def max_day(prices):
    '''Finds the day in which prices are maximum
    '''
    day_number=0
    for i in range(len(prices)):
        if prices[i]>prices[0]:
            day_number=i
    return day_number

# choice 6
def any_below(prices, threshold):
    '''Finds if any of the prices are above the threshold
    '''
    for i in prices:
        if i<threshold:
            print('there is atleast one price below',threshold)
            return True
        
    print('there is no prices below', threshold)            
    return False
        

# choice 7
def find_plan(prices):
    """Finds the best day to sell, buy and the maximum profit obtained
    """
    
    maxdiff=0
    day = 0
    for x in range(len(prices)):
        for y in range(x+1, len(prices)):
            diff=abs(prices[y]-prices[x])
            if diff>maxdiff and prices[x]<prices[y]:
                maxdiff=diff
                sell_day = x
                buy_day = y
            
    return [sell_day, buy_day, maxdiff]

        

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice ==3:
            avgerage=avg_price(prices)
            print('The average price is ', avg_price(prices))
        elif choice==4:
            standard_dev=std_dev(prices)
            print('the standard deviation is ', std_dev(prices))
        elif choice==5:
            maxd=max_day(prices)
            print('The max price is',prices[maxd],'on day', maxd)
        elif choice==6:
            threshold=int(input('Enter the threshold value:'))
            anybelow=any_below(prices, threshold)
        elif choice==7:
            bestplan = find_plan(prices)
            print('Buy on day',bestplan[0],'at price',prices[bestplan[0]])
            print('Sell on day',bestplan[1],'at price',prices[bestplan[1]])
            print('Total profit:',bestplan[2])
       
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

# part1 psudocode 
# get input of number of years
# for x in those number of years
# for y in 1 thorugh 13 
# get rainfall from user
#  add rainfall to total rainfall
# print the total rainfall divided by 12

#part2 psudocode 
# create if statmetn block for findoing number of points per purchased book 
# get number of books per user 
# run number of books through if statment block to get the points 
# print number of points 





import random

random_rain =random.uniform(1, 5) 

def get_rainfall(too_lazy): 
    while True:
        try: 
            if too_lazy == True:
                return random.uniform(1, 5) 
            rain = float(input("enter rainfall: "))
            return rain 
        except:
            print("enter a number")


def find_rainfall(too_lazy): 
    while True: 
        try:   
            years = int(input("enter number of years: "))
            break 
        except: 
            print("a number, not difficult")
    total_rain = 0 

    for year in range (1, years+ 1):
        print("year "+ str(year))
        for month in range (1, 13):
            rain = get_rainfall(too_lazy)
            total_rain = total_rain + rain 
            print("month " + str(month) + ": " + str(rain))
    average_rain = total_rain / (12 * years) 

    print("the total rain is: " + str(total_rain))
    print("the average rain is: " + str(average_rain))
    
# this is what the code would look like if following the prompt strictly 
def get_points(books_purchased):
    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0
    return points
#this would make more sense but not what was stricketly asked for 
def get_points_other(books_purchased):
    if books_purchased == 0:
        points = 0
    elif books_purchased <= 2:
        points = 5
    elif books_purchased <= 4:
        points = 15
    elif books_purchased <= 6:
        points = 30
    elif books_purchased >= 7:
        points = 60
    else:
        points = 0
    return points


def get_books():
    while True:
        try: 
            books = int(input("enter the number of books you purchased: "))
            return books 
        except:
            print("enter a number")

def part2(): 
    books = get_books()
    print("you have earned: " + str(get_points(books)) + " points")


def main():
    #part1 
    too_lazy = True if input(" are you too lazy: ").lower() == 'yes' else False
    find_rainfall(too_lazy)
    #part2 
    part2()




if __name__=="__main__":
    main()
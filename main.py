#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    month = month.capitalize()
    if month == "January":
        month_num = "01"
    elif month == "February":
        month_num = "02"
    elif month == "March":
        month_num = "03"
    elif month == "April":
        month_num = "04"
    elif month == "May":
        month_num = "05"
    elif month == "June":
        month_num = "06"
    elif month == "July":
        month_num = "07"
    elif month == "August":
        month_num = "08"
    elif month == "September":
        month_num = "09"
    elif month == "October":
        month_num = "10"
    elif month == "November":
        month_num = "11"
    elif month == "December":
        month_num = "12"
    else:
        month_num = 0
    return(month_num)


#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    list = []
    
    user_string = user_string.replace(",","")
    
    for x in user_string.split(" "):
        list.append(x)
    
    new_month = parse_month(list[0])
    day = int(list[1])
    if day < 10:
        return (f'{new_month}/0{list[1]}/{list[2]}')
    elif day > 9:
        return (f'{new_month}/{list[1]}/{list[2]}')
    else:
        return
        
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    user_string = input()
    while user_string != "-1":
        print(parse_date(user_string))
        user_string = input()
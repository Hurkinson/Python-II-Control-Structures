#Write a function called get_todays_date that returns
#today's date as a string, in the form year/month/day.
#For example, if today is January 15th, 2017, then it
#would return 2017/1/15.
#
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.
#
#Note that the line below will let you access today's date
#using date.today() anywhere in your code.
from datetime import date


#Write your function here!
def get_todays_date():
    today = date.today()
    today_y = str(today.year)
    today_m = str(today.month)
    today_d = str(today.day)
    string = ("{0}/{1}/{2}".format(today_y, today_m, today_d))
    return string
    


#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.

print(get_todays_date())


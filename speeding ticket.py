driver_speed = 57
speed_limit = 55
school_zone = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a conditional that decides the price of a speed ticket
#depending on the driver's speed, the speed limit, and
#whether or not they were in a school zone.
#
#The reasoning that determines the price of the ticket is:
#
# - $100 for speeding at all (any instance where driver_speed
#   is greater than speed limit).
# - $10 dollars per mile over the speed limit the driver was
#   going.
# - 2x the value otherwise if the violation occurred in a
#   school zone, as represented by the value of school_zone.
#
#Print the cost of the speeding ticket. If the driver was not
#speeding, print $0.
#
#Under the original values above, this should print $240:
#$100 for speeding, $20 for going 2mph above the speed limit,
#and x2 for it occurring in a school zone.


#Add your code here! Make sure to print the dollar sign, too.

def speedticket(drv_sp,sp_lmt,sch_z):
    bill = 0
    
    
    if drv_sp > sp_lmt:
        bill += 100 + ((drv_sp - sp_lmt)*10)
        if sch_z :
            bill *= 2
        result = "${0}".format(bill)
    else:
        result = "${0}".format(bill)
    return result


print(speedticket(driver_speed,speed_limit,school_zone))
    





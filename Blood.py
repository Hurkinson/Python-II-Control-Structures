#Consult this blood pressures chart: http://bit.ly/2CloACs
#
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).
#
#HINT: Don't overcomplicate this! Think carefully about in
#what order you should check the different categories. This
#problem could be easy or extremely hard depending on the
#order you change and whether you use returns or elifs wisely.


#Add your code here!
def check_blood_pressure(Syst_bp, Diast_bp):
    Sys_status = 0
    Dia_status = 0
    status_L= ["Low","Ideal","Pre-high","High"]
        
    if Syst_bp >= 70 and Syst_bp <= 90:
        Sys_status = 0
        
    elif Syst_bp >90 and Syst_bp <= 120:
        Sys_status = 1
        
    elif Syst_bp >120 and Syst_bp <= 140:
        Sys_status = 2
        
    elif Syst_bp >140 and Syst_bp <= 190:
        Sys_status = 3
                
                
    if Diast_bp >= 40 and Diast_bp <= 60:
        Dia_status = 0
        
    elif Diast_bp >60 and Diast_bp <= 80:
        Dia_status = 1
        
    elif Diast_bp >80 and Diast_bp <= 90:
        Dia_status = 2
        
    elif Diast_bp >90 and Diast_bp <= 100:
        Dia_status = 3
        
    print(Sys_status)
    print(Dia_status)
    
    if Sys_status > Dia_status:
            
        return status_L[Sys_status]
    else:
        return status_L[Dia_status]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Ideal
test_systolic = 80
test_diastolic = 90

print(check_blood_pressure(test_systolic, test_diastolic))



import math
def calculate_time(enter, exit):
    enter_h, enter_m = map(int, enter.split(':'))
    exit_h, exit_m = map(int, exit.split(':'))
    enter = enter_h * 60 + enter_m
    exit = exit_h * 60 + exit_m
    total = exit - enter
    return  convert_to_hours_mins(total),calculate_parking_fee(total)

def calculate_parking_fee(total_mins):
    if total_mins <= 15:
        return 0
    elif total_mins <= 60*2:
        return 50
    else:
        if total_mins>= 60*15:
            return 300
        return 50 + math.ceil(total_mins/60 -2) * 10


def convert_to_hours_mins(total_mins):
    hours = total_mins // 60
    mins = total_mins % 60
    return hours, mins

def print_time(time,text):
    h, m = map(int, time.split(':'))
    print(f"{text} : {h:02d}:{m:02d}")

enter_t=  input()
exit_t = input()

print_time(enter_t,"Enter time")
print_time(exit_t,"Out time")

(h,m),parking_fee = calculate_time(enter_t, exit_t)
print("Total time : {} hour {} min".format(h,m))

if parking_fee ==0:
    print("Charge : FREE.")
else:
    print("Charge : {} Baht.".format(parking_fee))
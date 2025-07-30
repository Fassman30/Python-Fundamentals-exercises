def add_day():
    week=["Monday","Tuesday","Wednesday","Thursday","Friday",]
    print(f"My first list is {week}")
    week.append("Saturday")
    week.append("Sunday") 
    print(f"My new list is {week}")
    print(f"The Day is {week[0]}")
    print(f"The Day is {week[-2]}")
    return week
add_day()
import calendar, time

if __name__ == '__main__':
    count = 1
    year = 1995 # Change to your year of birth 
    while count <= 12:
        bm = calendar.month(year, count)
        count += 1
        print(bm)
        time.sleep(1)

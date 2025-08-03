
import calendar

def isNoErrorInput(cei):
    try:
        int(cei)
        if int(cei) < 0:
            return False
        return True 
    except:
        return False 
        
if __name__ == '__main__':
    yr = input('Enter the year or -1 to quit: ')
    while yr != '-1':
        if isNoErrorInput(yr):
            count = 1
            while count <= 12:
                print(calendar.month(int(yr), count))
                count += 1
        else: 
            print("Invalid input. try again!")
        yr = input('Enter the year or -1 to quit: ')
        
        

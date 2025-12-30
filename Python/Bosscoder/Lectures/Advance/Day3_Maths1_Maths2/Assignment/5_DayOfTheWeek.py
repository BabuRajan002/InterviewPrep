class DayOfTheWeek:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def isLeapYear(self, y):
        if y % 4 == 0:
            if y % 100 == 0:
                return y % 400 == 0
            return True
        return False
    
    def solve(self):
        
        weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = 0
        year = self. year
        month = self.month
        day = self.day
        
        #to calculate target Year before year
        for y in range(1971, year):
            if self.isLeapYear(y) == True:
                days += 366
            else:
                days += 365
        
        #to calculate target Months before months
        for m in range(1, month):
            if m == 2 and self.isLeapYear(year) == True:
                days += 29
            else:
                days += months[m-1]
        
        #Remaining days in that month 
        days += day - 1

        idx = (5 + days) % 7
        return weeks[idx]

if __name__ == "__main__":
    daysofweek = DayOfTheWeek(18, 7, 1999)
    print(daysofweek.solve())



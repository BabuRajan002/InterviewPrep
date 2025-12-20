class Week:
    def __init__(self, week, days):
        self.week = week
        self.days = days
    
    def print_week(self):
        for i in range(1,self.week):
            print(f"Week {i}")
            for j in range(1,self.days):
                print(f"Days {j}",end=" ")
            print(" ")

if __name__ == "__main__":
    week = Week(4,6)
    week.print_week()

        
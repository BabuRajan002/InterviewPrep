class MultipleOfFive:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        times = self.n // 5 + 1
        num_list = []
        for i in range(1, times):
            num_list.append(i * 5)
        return num_list

if __name__ == "__main__":
    mul_of_five = MultipleOfFive(25)
    print(mul_of_five.solve())
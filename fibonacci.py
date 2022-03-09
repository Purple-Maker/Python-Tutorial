#Using Recursion
class Fibonacci():
    def __init__(self, num):
        self.n = num

    def fiboRecur(self):
        if self.n == 2: return self.n - 1
        elif self.n == 1: return self.n - 1
        #else: return fiboRecur(self.n - 1) + fiboRecur(self.n - 2)
        else: return Fibonacci(self.n - 1).fiboRecur() + Fibonacci(self.n - 2).fiboRecur()


if __name__ == "__main__":
    print('斐波那契数列的第n个数是:')
    n = int(input('n = '))
    FString = Fibonacci(n)
    print(FString.fiboRecur())
    fiboList = []
    for i in range(1,n+1):
        F = Fibonacci(i)
        fiboList.append(F.fiboRecur())
    print('斐波那契数列的前n个数为:{}'.format(fiboList))
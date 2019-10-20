# Runtime: 48 ms, faster than 89.09% of Python3 online submissions for Fizz Buzz Multithreaded.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Fizz Buzz Multithreaded.
import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n + 1
        self.f = threading.Semaphore(0)
        self.b = threading.Semaphore(0)
        self.fb = threading.Semaphore(0)
        self.nn = threading.Semaphore(1)
        self.cur = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5:
                self.f.acquire()
                printFizz()
                self.cur += 1
                if self.cur % 5 == 0:
                    self.b.release()
                else:
                    self.nn.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 5 == 0 and i % 3:
                self.b.acquire()
                printBuzz()
                self.cur += 1
                if self.cur % 3 == 0:
                    self.f.release()
                else:
                    self.nn.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 5 == 0 and i % 3 == 0:
                self.fb.acquire()
                printFizzBuzz()
                self.cur += 1
                self.nn.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            if i % 5 and i % 3:
                self.nn.acquire()
                printNumber(i)
                self.cur += 1
                if self.cur % 3 == 0 and self.cur % 5 == 0:
                    self.fb.release()  # fb add 1
                elif self.cur % 3 == 0:
                    self.f.release()  # f add 1
                elif self.cur % 5 == 0:
                    self.b.release()  # b add 1
                else:
                    self.nn.release()

################################################################################
# event
################################################################################
# Runtime: 72 ms, faster than 50.14% of Python3 online submissions for Print in Order.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Print in Order.
from threading import Event


class Foo:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.done[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.done[0].wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.done[1].set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done[1].wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


################################################################################
# barrier
################################################################################
# Runtime: 40 ms, faster than 82.14% of Python3 online submissions for Print in Order.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Print in Order.
from threading import Barrier


class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)
            
    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()
            
    def third(self, printThird):
        self.second_barrier.wait()
        printThird()


################################################################################
# lock
################################################################################
# Runtime: 44 ms, faster than 75.28% of Python3 online submissions for Print in Order.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Print in Order.
from threading import Lock


class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst):
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        with self.lock1:
            printSecond()
            self.lock2.release()

    def third(self, printThird):
        with self.lock2:
            printThird()


################################################################################
# semaphore
################################################################################
# Runtime: 40 ms, faster than 82.14% of Python3 online submissions for Print in Order.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Print in Order.
from threading import Semaphore


class Foo:
    def __init__(self):
        self.sem1 = Semaphore(0)
        self.sem2 = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.sem1.release()

    def second(self, printSecond):
        with self.sem1:
            printSecond()
            self.sem2.release()

    def third(self, printThird):
        with self.sem2:
            printThird()


################################################################################
# condition variable
################################################################################
# Runtime: 40 ms, faster than 82.14% of Python3 online submissions for Print in Order.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Print in Order.
from threading import Condition


class Foo:
    def __init__(self):
        self.exec_cond = Condition()
        self.order = 0

    def first(self, printFirst):
        with self.exec_cond:
            printFirst()
            self.order = 1
            self.exec_cond.notify(2)

    def second(self, printSecond):
        with self.exec_cond:
            self.exec_cond.wait_for(lambda: self.order == 1)
            printSecond()
            self.order = 2
            self.exec_cond.notify()

    def third(self, printThird):
        with self.exec_cond:
            self.exec_cond.wait_for(lambda: self.order == 2)
            printThird()

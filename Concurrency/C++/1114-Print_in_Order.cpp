// TODO: all method


////////////////////////////////////////////////////////////////////////////////
// mutex + condition_variable + lock
////////////////////////////////////////////////////////////////////////////////
// Runtime: 168 ms, faster than 41.96% of C++ online submissions for Print in Order.
// Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Print in Order.
#include <mutex>
#include <condition_variable>
#include <thread>
#include <functional>
using namespace std;


class Foo {
public:
    Foo() {
        count = 1;
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex> lck(mtx);
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        count = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lck(mtx);
        while (count != 2)
            cv.wait(lck);
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        count = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lck(mtx);
        while (count != 3)
            cv.wait(lck);        
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        cv.notify_all();
    }

private:
    int count = 0;
    mutex mtx;
    condition_variable cv;
};


////////////////////////////////////////////////////////////////////////////////
// mutex + lock
////////////////////////////////////////////////////////////////////////////////
// Runtime: 204 ms, faster than 32.04% of C++ online submissions for Print in Order.
// Memory Usage: 9.2 MB, less than 100.00% of C++ online submissions for Print in Order.
class Foo {
public:
    mutex m1, m2;
    Foo() {
        m1.lock();
        m2.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.   
        printFirst();
        m1.unlock();
    }

    void second(function<void()> printSecond) {
        // printSecond() outputs "second". Do not change or remove this line.
        m1.lock();
        printSecond();
        m2.unlock();
    }

    void third(function<void()> printThird) {
        // printThird() outputs "third". Do not change or remove this line.
        m2.lock();        
        printThird();
    }
};


////////////////////////////////////////////////////////////////////////////////
// atomic + sleep
////////////////////////////////////////////////////////////////////////////////
// Runtime: 1664 ms, faster than 6.85% of C++ online submissions for Print in Order.
// Memory Usage: 9.2 MB, less than 100.00% of C++ online submissions for Print in Order.
class Foo {
public:
    Foo() : i(0) {}
    


    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        i=1;
    }

    void second(function<void()> printSecond) {
        while(i!=1){}
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        i=2;
    }

    void third(function<void()> printThird) {
        while(i!=2){}
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
private:
    atomic_int i;
};


////////////////////////////////////////////////////////////////////////////////
// chrono
////////////////////////////////////////////////////////////////////////////////
// Runtime: 156 ms, faster than 60.70% of C++ online submissions for Print in Order.
// Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Print in Order.
#include <chrono>
#include <thread>


class Foo {
public:
    Foo() {
        times_called = 0;
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        times_called += 1;
    }

    void second(function<void()> printSecond) {
        
        // printSecond() outputs "second". Do not change or remove this line.
        while (times_called != 1)
        {
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
        printSecond();
        times_called += 1;
    }

    void third(function<void()> printThird) {
        
        // printThird() outputs "third". Do not change or remove this line.
        while (times_called != 2)
        {
            std::this_thread::sleep_for(std::chrono::milliseconds(10));
        }
        printThird();
    }
private:
    int times_called;
};

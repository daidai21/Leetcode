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

// TODO: all method


////////////////////////////////////////////////////////////////////////////////
// usleep + while True
////////////////////////////////////////////////////////////////////////////////
// Runtime: 164 ms, faster than 47.04% of C online submissions for Print in Order.
// Memory Usage: 7.5 MB, less than 100.00% of C online submissions for Print in Order.
typedef struct {
    // User defined data may be declared here.
    bool first_finish;
    bool second_finish;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    obj->first_finish = false;
    obj->second_finish = false;
    
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj->first_finish = true;
}

void second(Foo* obj) {
    while (obj->first_finish == false)
        usleep(5);
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj->second_finish = true;
}

void third(Foo* obj) {
    while (obj->first_finish == false || obj->second_finish == false)
        usleep(5);    
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    
}


////////////////////////////////////////////////////////////////////////////////
// sched_yield()
////////////////////////////////////////////////////////////////////////////////
// Runtime: 312 ms, faster than 21.43% of C online submissions for Print in Order.
// Memory Usage: 7.8 MB, less than 100.00% of C online submissions for Print in Order.
#include <sched.h>

typedef struct {
    // User defined data may be declared here.
    int val;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    obj->val = 0;
    
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj->val++;
}

void second(Foo* obj) {
    while (obj->val < 1)
        sched_yield();
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj->val++;
}

void third(Foo* obj) {
    while (obj->val < 2)
        sched_yield();
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    
}



////////////////////////////////////////////////////////////////////////////////
// while True
////////////////////////////////////////////////////////////////////////////////
// FIXME: The theory is not rigorous
// Runtime: 1500 ms, faster than 7.14% of C online submissions for Print in Order.
// Memory Usage: 7.8 MB, less than 100.00% of C online submissions for Print in Order.
typedef struct {
    // User defined data may be declared here.
    int * i; 
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    // Initialize user defined data here. 
    obj->i = malloc(sizeof(int));
    *(obj->i) = 1; 
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    *(obj->i) += 1; 
}

void second(Foo* obj) {
    while (1){
        if (*(obj->i) == 2)
            break; 
    }
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    *(obj->i) += 1; 
}

void third(Foo* obj) {
    while (1){
        if (*(obj->i) == 3)
            break; 
    }
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    free(obj->i);
    free(obj); 
}


////////////////////////////////////////////////////////////////////////////////
// condition variable + lock
////////////////////////////////////////////////////////////////////////////////
// Runtime: 152 ms, faster than 62.81% of C online submissions for Print in Order.
// Memory Usage: 7.6 MB, less than 100.00% of C online submissions for Print in Order.
#include <pthread.h>


typedef struct {
    pthread_mutex_t mx;
    pthread_cond_t cv;
    int val;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    pthread_mutex_init(&obj->mx, NULL);
    pthread_cond_init(&obj->cv, NULL);
    obj->val = 0;
    return obj;
}

void first(Foo* obj) {
    pthread_mutex_lock(&obj->mx);
    printFirst();
    obj->val = 1;
    pthread_cond_signal(&obj->cv);
    pthread_mutex_unlock(&obj->mx);
}

void second(Foo* obj) {
    pthread_mutex_lock(&obj->mx);
    while(obj->val<1){
        pthread_cond_signal(&obj->cv);
        pthread_cond_wait(&obj->cv, &obj->mx);
    }
    printSecond();
    obj->val = 2;
    pthread_cond_signal(&obj->cv);
    pthread_mutex_unlock(&obj->mx);
}

void third(Foo* obj) {
    pthread_mutex_lock(&obj->mx);
    while(obj->val<2){
        pthread_cond_signal(&obj->cv);
        pthread_cond_wait(&obj->cv, &obj->mx);
    }
    printThird();
    obj->val = 0;
    pthread_cond_signal(&obj->cv);
    pthread_mutex_unlock(&obj->mx);
}

void fooFree(Foo* obj) {
    pthread_mutex_destroy(&obj->mx);
    pthread_cond_destroy(&obj->cv);
    free(obj);
}

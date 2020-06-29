// greedy
// Runtime: 0 ms, faster than 100.00% of C online submissions for Valid Parenthesis String.
// Memory Usage: 5.1 MB, less than 70.69% of C online submissions for Valid Parenthesis String.
bool checkValidString(char * s){
    int low  = 0;
    int high = 0;
    for (char* t = s; *t != '\0'; ++t) {
        if (*t == '(')
            low++;
        else
            low--;
        if (*t != ')')
            high++;
        else
            high--;
        if (high < 0)
            break;
        low = low > 0 ? low : 0;
    }
    return low == 0;
}

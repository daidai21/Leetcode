// Runtime: 5 ms, faster than 23.26% of Java online submissions for Decode String.
// Memory Usage: 37.6 MB, less than 29.90% of Java online submissions for Decode String.
class Solution {
    public String decodeString(String s) {
        String res = "";
        Stack<Integer> stk1 = new Stack<>();
        Stack<String> stk2 = new Stack<>();
        Integer tmp = 0; // stk1
        for (char ch : s.toCharArray()) {
            System.out.println(stk1 + " " + stk2 + " " + tmp + " " + res);
            if (ch == '[') {
                stk1.push(tmp);
                stk2.push(res);
                res = "";
                tmp = 0;
            } else if (ch == ']') {
                String t = res;
                int repeatTimes = stk1.pop() - 1;
                for (int i = 0; i < repeatTimes; ++i) {
                    res += t;
                }
                res = stk2.pop() + res;
            } else if (Character.isDigit(ch)) {
                tmp = tmp * 10 + ch - '0';
            } else {
                res += ch;
            }
        }
        return res;
    }
}

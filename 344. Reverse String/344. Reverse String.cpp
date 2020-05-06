//Recursive solution


class Solution {
public:
    void reverseString(vector<char>& s) {
        if (s.size() == 0)
            return;
        char t = s[0];
        auto begin = s.begin();
        s.erase(begin);
        reverseString(s);
        s.push_back(t);
        
    }
};

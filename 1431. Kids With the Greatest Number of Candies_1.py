class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> answer;
        int max_cnt = 0;
        for (int i = 0; i < candies.size(); ++i) {
            max_cnt = max(candies[i], max_cnt);
        }
        for (int i = 0; i < candies.size(); ++i) {            
            answer.push_back((candies[i] + extraCandies) >= max_cnt); 
        }
        return answer;
    }
};

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& c, int ec) {
        
        //variable maximum is to store the maximum of the given array
        int maximum = INT_MIN;
        int n = c.size();
        
        for(int i = 0; i<n; i++)
            maximum = max(maximum,c[i]);
        
        //to store the final answer vector
        vector<bool> answer;
        
        // the logic is simple : if adding ec with the current allotted candies makes it >= the current maximum then the answer should be true for that index, otherwise 0
        for(int i =0;i<n;i++){
            if(c[i]+ec>=maximum){
                answer.push_back(true);
            }else{
                answer.push_back(false);
            }
        }
        
        return answer;
    }
};

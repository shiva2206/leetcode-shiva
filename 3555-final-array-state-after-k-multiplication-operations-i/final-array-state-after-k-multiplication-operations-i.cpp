class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>> pq;
        
        for(int i = 0;i<nums.size();i++){
            pq.push(vector<int>{nums[i],i});
        }

        for(int i=0;i<k;i++){
            vector<int> res = pq.top();
            pq.pop();
            nums[res[1]] = res[0]*multiplier;
            pq.push(vector<int>{nums[res[1]],res[1] });
        }
        return nums;

    }
};
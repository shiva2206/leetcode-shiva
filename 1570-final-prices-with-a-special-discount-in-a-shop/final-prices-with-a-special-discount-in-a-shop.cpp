class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        stack<int> sta;
        for(int i = 0;i<prices.size();i++){
            while(sta.size()>0 && prices[sta.top()] >= prices[i]){
                prices[sta.top()] -= prices[i];
                sta.pop();
            }
            sta.push(i);
        }
        return prices;
    }
};
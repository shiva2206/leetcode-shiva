class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        unordered_map<int,int> d;
        priority_queue<int,vector<int>,greater<int>> pq;

        for(int i : hand){
            d[i]++;
            if(d[i]==1){
                pq.push(i);
            }
        }

        while(pq.size()>0){
            int x = pq.top();
            for(int i = 0;i<groupSize;i++){
                int y = x +i;
                if(d.count(y)==0) return false;
                d[y]-=1;
                if(d[y]==0){
                    d.erase(y);
                }
            }

            while (pq.size()>0 && d.find(pq.top())==d.end()){
                pq.pop();
            }
        }
        return true;
    }
};
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead;
        for(string s : deadends) dead.insert(s);
        if(dead.count(target) || dead.count("0000")) return -1;
        if("0000" == target) return 0;
        deque<string> que;
        que.push_back("0000");
        int k=1;
        string l = "0123456789";
        while(que.size()>0){
            int p = que.size();
            for(int z = 0;z<p;z++){
                string y =que.front(); 
                que.pop_front();
                for(int i = 0;i<4;i++){
                    string x = y;
                    
                    int a = static_cast<int>(y[i]) - 48;
                    x[i] = l[(a + 1 + 10)%10];
                    if(dead.count(x) == 0){
                        if(x == target) return k;
                        dead.insert(x);
                        que.push_back(x);
                        // cout<<x<<" "<<a<<endl;
                    }
                    x[i] = l[(a-1+10)%10];
                    if(dead.count(x)==0){
                        if(x==target) return k;
                        dead.insert(x);
                        que.push_back(x);
                        // cout<<x<< " "<<a<<endl;
                    }
                }
            }
            k+=1;
        }    
        return -1;

    }
};
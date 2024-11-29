class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        
        if(grid.size()==1 && grid[0][1]>1) return -1;
        if(grid[0].size()==1 && grid[1][0]>1) return -1;
        if(grid[0][1]>1 && grid[1][0]>1) return -1;

        int dirs[4][4] = {{0,1},{1,0},{-1,0},{0,-1}};
        priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>> pq;
        pq.push({0,0,0});
        while(pq.size()>0){
              auto res = pq.top();
        

        int val = res[0], x = res[1], y = res[2];
            if(x==grid.size()-1 && y==grid[0].size()-1) return val;
            pq.pop();

            for(auto p : dirs ){
                int i = p[0]+x;
                int j = p[1]+y;
                if(i<0 || j<0 || i== grid.size() || j==grid[0].size()) continue;
                if(grid[i][j]<0) continue;
                int m = val+1;
                if(m<grid[i][j]){
                    if((grid[i][j]-m)%2==1){
                        m = grid[i][j]+1;
                    }else{
                        m = grid[i][j];
                    }
                }

                grid[i][j] = -m;
                if(m==0) grid[i][j] = INT_MIN;
                pq.push({m,i,j});

            }
        }
        return -1;
    }
};
class Solution {
    public int minimumTime(int[][] grid) {
        
        if(grid[0].length==1 && grid[0][1]>1) return -1;
        if(grid.length==1 && grid[1][0]>1) return -1;
        if(grid[0][1]>1 && grid[1][0]>1) return -1;
        
        int[][] dirs = new int[][]{{0,1},{1,0},{-1,0},{0,-1}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)-> a[0] - b[0]);
        pq.add(new int[]{0,0,0});
        while(pq.size()>0){
            int[] res = pq.poll();
            int val = res[0];
            int x = res[1];
            int y = res[2];
            if(x==grid.length-1 && y==grid[0].length-1) return val;
            for(int[] p : dirs){
                int i = p[0] + x;
                int j = p[1] + y;
                if (i<0 || j<0 || i==grid.length || j==grid[0].length) continue;
                if(grid[i][j]<0) continue;

                int m = val +1;
                if(m<grid[i][j]){
                    if(((grid[i][j] -m)%2)==1){
                        m = grid[i][j]+1;
                    }else{
                        m = grid[i][j];
                    }
                }
                grid[i][j]= -m;
                if(m==0){
                    grid[i][j] = -Integer.MAX_VALUE;
                }
                pq.add(new int[]{m,i,j});
            }
            

        }
        return -1;

    }
}
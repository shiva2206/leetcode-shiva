class Solution {
    public int[][] restoreMatrix(int[] row, int[] col) {
        int[][] res = new int[row.length][col.length];
        int m;
        for(int i = 0;i <row.length;i++){
            for(int j = 0;j<col.length;j++){
                m = Math.min(row[i],col[j]);
                res[i][j] = m;
                row[i] -=m;
                col[j] -=m;  
            }
        }   
        return res;
    }
}
class Solution {
    public List<Integer> luckyNumbers (int[][] mat) {
        int[] row = new int[mat.length];
        int[] col = new int[mat[0].length];
        List<Integer> res = new ArrayList<>();
        Arrays.fill(row,Integer.MAX_VALUE);

        for(int i = 0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                row[i] = Math.min(row[i],mat[i][j]);
                col[j] = Math.max(col[j],mat[i][j]);
            }
        }
        for(int i = 0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                if(row[i]==col[j]){
                    res.add(row[i]);
                }
            }

        }
        return res;
    }
}
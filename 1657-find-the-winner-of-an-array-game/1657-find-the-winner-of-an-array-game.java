class Solution {
    public int getWinner(int[] arr, int k) {
        int m=arr[0];
        int c=0;
        for(int i=1;i<arr.length;i++){
            if(m<arr[i]) {
                c=0;
                m=arr[i];
            }
            c+=1;
            if (c==k) return m;
        }
        return m;

    }
}
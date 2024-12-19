class Solution {
    
    public int maxChunksToSorted(int[] arr) {
       

        int[] d = new int[arr.length+1];
        for(int i = arr.length - 1;i>=0;i--){
            int req = 0 , s= 0;
            for(int j = i;j<arr.length;j++){
                req+= j;
                s+=arr[j];
                if(req==s) d[i] = Math.max(d[i],1 + d[j+1]);
            }
        }
        return d[0];
    }
}

   
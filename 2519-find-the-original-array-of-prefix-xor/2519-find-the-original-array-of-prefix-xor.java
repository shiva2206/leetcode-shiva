class Solution {
    public int[] findArray(int[] pref) {
       
     
       int m=pref[0];
       int n;
       for(int i=1;i<pref.length;i++){
           n=pref[i];
           pref[i]=m^pref[i];
           m=n;
       }
       return pref;
    }
}
class Solution {
    public boolean checkIfExist(int[] arr) {
        HashSet<Integer> d = new HashSet<>();
        for(int i : arr){
            if(d.contains(i*2)) return true;
            if(i%2==0 && d.contains(i/2)) return true;
            d.add(i);
        }       
        return false;
    }
}
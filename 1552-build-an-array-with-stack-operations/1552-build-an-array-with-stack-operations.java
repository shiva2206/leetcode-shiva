class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> res = new ArrayList<>();
        int m=1;
        for(int i : target){
            while (i>m){
                res.add("Push");
                res.add("Pop");
                m+=1;
            }
            res.add("Push");
            m+=1;
        }
        return res;
    }
}
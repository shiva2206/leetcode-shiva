class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> d = new HashMap<>();
        for(String s : strs){
            int[] arr = new int[26];
            for(char c : s.toCharArray()){
                arr[c-'a']+=1;
            }
            String t = Arrays.toString(arr);
            if(d.containsKey(t)){
                d.get(t).add(s);
            }else{
                d.put(t,new ArrayList<>());
                d.get(t).add(s);
                
            }
        }       
        List<List<String>> res = new ArrayList<>();
        for(List<String> vec : d.values()){
            res.add(vec);
        }
        return res;
    }
}
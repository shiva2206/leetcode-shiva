class Solution {
    List<String> l = new ArrayList<>();
    List<String> res = new ArrayList<>();
    HashSet<String> dic;
    public List<String> wordBreak(String s, List<String> wordDict) {
        dic = new HashSet<>(wordDict);
        System.out.println(dic.size());
        dfs(0,s);
        return res;
    }

    public void dfs(int i,String s){
        if(i==s.length()){
            res.add(String.join(" ",l));
           
            return ;
        }
        String q = "";
        for(int j = i;j<s.length();j++){
            q += s.charAt(j);
            if(dic.contains(q)){
                l.add(q);
                dfs(j+1,s);
                l.removeLast();

            }


        }
        return ;
    }
}
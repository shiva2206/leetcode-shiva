class Solution {
    List<List<String>> res = new ArrayList<>();
    List<String> l = new ArrayList<>();
    public List<List<String>> partition(String s) {
        dfs(s,0);
        return res;        
    }
    public boolean isSame(String q){
        int i=0,j = q.length()-1;
        while(i<j){
            if(q.charAt(i)!=q.charAt(j)) return false;
            i+=1;
            j-=1;
        }
        return true;


    }
    public void dfs(String s,int i){
        if(i==s.length()){
            res.add(new ArrayList(l));
            return ;
        }

        String q = "";
        for(int k = i;k<s.length();k++){
            q = q+s.charAt(k);
            if(isSame(q)){
                l.add(q);
                dfs(s,k+1);
                l.remove(l.size()-1);
            }
        }
        return ;
    }
}
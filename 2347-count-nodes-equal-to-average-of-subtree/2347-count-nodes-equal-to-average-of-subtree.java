/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res=0;
    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return res;

    }
    public int[] dfs(TreeNode t){
        if(t==null) return new int[]{0,0};
        int m = t.val;
        int c=1;
        int[] p = dfs(t.left);
        int[] q =dfs(t.right);
        m+=p[1]+q[1];
        c+=p[0]+q[0];
        if (m/c==t.val) res+=1;
        return new int[]{c,m};

    }
}
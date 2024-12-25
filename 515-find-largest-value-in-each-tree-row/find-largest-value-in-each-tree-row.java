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
    public List<Integer> largestValues(TreeNode root) {
        if(root==null) return new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> que = new LinkedList<>();
        que.add(root);
        while(que.size()>0){
            int p = que.size();
            Integer m = Integer.MIN_VALUE;
            for(int i = 0;i<p;i++){
                TreeNode t = que.removeFirst();
                m = Math.max(m,t.val);
                if(t.left!=null) que.add(t.left);
                if(t.right!=null) que.add(t.right);
            }

            res.add(m);
        }
        return res;
    }
}
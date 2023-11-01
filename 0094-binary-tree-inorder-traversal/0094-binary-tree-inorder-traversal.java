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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        while(root!=null){
            if(root.left==null){
                res.add(root.val);
                root=root.right;

            }else{
                TreeNode t = root.left;
                while(t.right!=null && t.right!=root) t=t.right;
                if(t.right==null){
                    t.right=root;
                    root=root.left;
                }else{
                    res.add(root.val);
                    root=root.right;
                }
                
            }
        }
        return res;
    }
}
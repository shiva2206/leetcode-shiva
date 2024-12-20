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
    public TreeNode reverseOddLevels(TreeNode root) {
        List<Integer> q = new ArrayList<>();
        Deque<TreeNode> deq = new LinkedList<>();
        int h = 0;
        deq.add(root);
        while(deq.size()>0){
            int p = deq.size();
            for(int i = 0 ;i<p;i++){
                TreeNode t = deq.removeFirst();
                if(h%2==1){
                    int k = q.get(q.size()-1);
                    q.remove(q.size()-1);
                    t.val = k;
                }

                if(t.left!=null){
                    deq.add(t.left);                 
                    if(h%2==0){
                        q.add(t.left.val);
                    }
                }if(t.right!=null){
                    deq.add(t.right);
                    if(h%2==0){
                        q.add(t.right.val);
                    }
                }
            }
            h+=1;
        }

        return root;

    }
}
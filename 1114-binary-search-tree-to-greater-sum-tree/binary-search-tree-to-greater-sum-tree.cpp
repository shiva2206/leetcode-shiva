/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int s =0;
    void dfs(TreeNode* t){
        if(t==NULL) return;
        dfs(t->right);
        s += t->val;
        t->val = s;
        dfs(t->left);
        
    }
    TreeNode* bstToGst(TreeNode* root) {
        dfs(root);
        return root;
    }
};
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
    TreeNode* reverseOddLevels(TreeNode* root) {
        deque<TreeNode*> deq;
        deq.push_back(root);
        vector<int> q;
        int h =0;
        while(deq.size()>0){
            int p = deq.size();
            for(int i = 0;i<p;i++){
                TreeNode* t = deq.front();
                deq.pop_front();
                if(h%2==1) {
                    t->val = q.back();
                    q.pop_back();
                }
                if(t->left!=NULL){
                    deq.push_back(t->left);
                    if(h%2==0){
                        q.push_back(t->left->val);
                    }
                }if(t->right!=NULL){
                    deq.push_back(t->right);
                    if(h%2==0) q.push_back(t->right->val);
                }

            }
            h+=1;
        }

        return root;
    }
};
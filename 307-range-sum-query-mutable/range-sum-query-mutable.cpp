
class Node{
    public:
        int data ;
        Node* left = NULL;
        Node*right = NULL;


};
class NumArray {
public:
    Node* head ;
    int tot;
    Node* init(int i,int j,vector<int>& nums){
        Node* t = new Node();
        if(i==j){
            t->data = nums[i];
            return t;
        }

        int m = (i+j)/2;
        t->left = init(i,m,nums);
        t->right = init(m+1,j,nums);
        t->data = t->left->data + t->right->data;
        return t;

    }
    NumArray(vector<int>& nums) {
        head = init(0,nums.size()-1,nums);
        tot = nums.size()-1;
    }
    
    void update(int index, int val) {
        change(head,0,tot,index,val);
    }

    int change(Node *t,int i,int j,int index,int val){
        if(j<index || index<i) return 0;
        if(i==j && i==index){
            t->data = val;
            return val;
        }
        int m = (i+j)/2;
        change(t->left,i,m,index,val);
        change(t->right,m+1,j,index,val);

        t->data = t->left->data + t->right->data;
        return t->data;
    }
    
    int sumRange(int left, int right) {
        return dfs(head,0,tot,left,right);
    }

    int dfs(Node* t,int i,int j,int left,int right){
        if(j<left || right<i) return 0;
        if(left<=i && j<=right) return t->data;
        int m = (i+j)/2;
        return  dfs(t->left,i,m,left,right) + dfs(t->right,m+1,j,left,right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
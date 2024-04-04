class Node{
    int data;
    Node left;
    Node right;
}
class NumArray {

    Node head;
    int tot;
    public NumArray(int[] nums) {
        tot = nums.length-1;
        head = init(0,tot,nums);
    }

    public Node init(int i,int j,int[] nums){
        Node t = new Node();
        if(i==j){   
            t.data = nums[i];
            return t;
        }

        int m = (i+j)/2;
        t.left = init(i,m,nums);
        t.right = init(m+1,j,nums);
        t.data = t.left.data + t.right.data;
        return t;
    }

    public int change(Node t,int i,int j,int ind,int val){
        if(j<ind || ind<i) return 0;
        if(i==j && i==ind){
            t.data = val;
            return t.data;
        }

        int m = (i+j)/2;

        change(t.left,i,m,ind,val);
        change(t.right,m+1,j,ind,val);

        t.data = t.left.data + t.right.data;

        return t.data;

    }
    public void update(int index, int val) {
        change(head,0,tot,index,val);        
    }
    
    public int sumRange(int left, int right) {  
        return dfs(head,0,tot,left,right);
    }

    public int dfs(Node t,int i,int j,int left,int right){
        if(j<left || right < i) return 0;
        if(left<=i && j<=right) return t.data;
        int m = (i+j)/2;
        return dfs(t.left,i,m,left,right) + dfs(t.right,m+1,j,left,right);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
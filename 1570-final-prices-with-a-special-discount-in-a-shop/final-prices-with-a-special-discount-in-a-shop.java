class Solution {
    public int[] finalPrices(int[] prices) {
        Stack<Integer> sta = new Stack<>();
        for(int i = 0;i<prices.length;i++){
            while(sta.size()>=1 && prices[sta.peek()] >= prices[i]){
                prices[sta.pop()] -= prices[i];
            }
            sta.push(i);
        }
        return prices;
    }
}
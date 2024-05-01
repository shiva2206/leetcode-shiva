class Solution {
public:
    string reversePrefix(string word, char ch) {

        for(int i = 0;i<word.size();i++){
            if(word[i]==ch){
                int x = 0;
                int y = i;
                while(x<y){
                    char t = word[x];
                    word[x] = word[y];
                    word[y] = t;
                    x+=1;
                    y-=1; 
                }
                return word;
            }
        }   
        return word;     
    }
};
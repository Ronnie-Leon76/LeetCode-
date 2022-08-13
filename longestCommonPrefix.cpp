class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        //bool isLowercase;
        string commonPrefix;
        char current;
        int occurrenceCount;
        /**
        for(int i=0; i<strs.size(); i++){
            if(strs[i][i].islower())
                isLowercase = true;
            else
                isLowercase = false;
        }
        **/
        
        if((strs.size()>0) && (strs.size()<=200)){
            int min = strs[0].size();
            for(int i=0; i<strs.size();i++){
                if(strs[i].size()<min)
                    min = strs[i].size();
            }
            int n = strs.size();
            for(int j=0; j<min; j++){
                current = strs[0][j];
                
                for(int k=1; k<=n; k++){
                    if(strs[k][j] == current){
                        occurrenceCount++;
                    }
                        
                        
                }
                if(occurrenceCount == n){
                    commonPrefix.push_back(current);
                }
                
            }
        } else {
            std::cout<<"Invalid vector string!"<<std::endl;
        }
        return commonPrefix;
    }
};
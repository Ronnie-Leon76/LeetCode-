class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int n;
        if(energy.size() == experience.size())
             n = energy.size();
        bool moreThanHundred;
        for(int i : experience){
            if(i > 100)
              moreThanHundred = true;
            else
                moreThanHundred = false;
        }
        int minHours;
        if((n>=1) && (n<=100) && (initialEnergy>=1) && (!moreThanHundred)){
            int deficientEnergy;
            int deficientExperience;
            for(int i=0; i<n; i++){
                if(initialEnergy>energy[i]){
                    initialEnergy -= energy[i];
                }else if(initialEnergy<=energy[i]){
                    initialEnergy = 0;
                    deficientEnergy += (energy[i] - initialEnergy);
                    //initialEnergy -= energy[i];
                }else if(initialExperience>experience[i]){
                    initialExperience += experience[i];
                }else if(initialExperience<=experience[i]){
                    //initialExperience = 0;
                    deficientExperience += (experience[i] - initialExperience);
                }else{
                    continue;
                }
            }
            if((initialEnergy >= 1) || (initialExperience >= 1)){
                return minHours;
            }else{
                minHours = (deficientEnergy + 1) + (deficientExperience + 1);   
            }
            
        }else{
            std::cout<<"Invalid values!"<<std::endl;
        }
        return minHours;
    }
};
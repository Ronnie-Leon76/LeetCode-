class Solution
{
public:
    string intToRoman(int num)
    {
        string romanNumber;
        if ((num > 0) && (num <= 3999))
        {
            while (num != 0)
            {
                if ((num / 1000) > 0)
                {
                    int q = num / 1000;
                    for(int i=0; i<q; i++)
                        romanNumber += 'M';
                    num = num % 1000;
                }
                else if ((num / 900) > 0)
                {
                    romanNumber += 'C';
                    romanNumber += 'M';
                    num = num % 900;
                }
                else if ((num / 500) > 0)
                {
                    romanNumber += 'D';
                    num = num % 500;
                }
                else if ((num / 400) > 0)
                {
                    romanNumber += 'C';
                    romanNumber += 'D';
                    num = num % 400;
                }
                else if ((num / 100) > 0)
                {
                    int p = num / 100;
                    for(int i=0; i<p; i++)
                        romanNumber += 'C';
                    num = num % 100;
                }
                else if ((num / 90) > 0)
                {
                    romanNumber += 'X';
                    romanNumber += 'C';
                    num = num % 90;
                }
                else if ((num / 50) > 0)
                {
                    romanNumber += 'L';
                    num = num % 50;
                }
                else if((num/40) > 0){
                    romanNumber += 'X';
                    romanNumber += 'L';
                    num = num % 50;
                }
                else if ((num / 10) > 0)
                {
                    int r = num / 10;
                    for(int i=0; i<r; i++)
                        romanNumber += 'X';
                    num = num % 10;
                }
                else if ((num / 9) > 0)
                {
                    romanNumber += 'I';
                    romanNumber += 'X';
                    num = num % 9;
                }
                else if ((num / 5) > 0)
                {
                    romanNumber += 'V';
                    num = num % 5;
                }
                else if ((num / 4) >= 1)
                { 
                    romanNumber += 'I';
                    romanNumber += 'V';
                    num = num % 4;     
                }
                else if ((num / 1) > 0)
                {
                    for(int i = 0; i < num; i++)
                        romanNumber += 'I';
                        num = num % 1;
                }
            }
        }
        else
        {
            std::cout << "Invalid number!" << std::endl;
        }
        return romanNumber;
    }
};
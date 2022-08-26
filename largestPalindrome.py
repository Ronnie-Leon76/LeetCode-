class Solution:
    def largestPalindromic(self, num: str) -> str:
        if len(num)>=1 and len(num)<=100000:
            palindrome = ''
            length = len(num)
            count = 0
            while(count<length):
                substr = num[count]
                for s in num:
                    if substr == s:
                        palindrome.append(s)
                count += 1
            intList = int(list(palindrome))
            largest = intList[0]
            listlen = len(intList)
            palindromeString = ''
            number = intList[i]
            for i in range(listlen):
                if(number>intList[i]):
                    large = number
                else:
                    large = intList[i]
            intList.remove(large)
            palindromeString.append(large)  
            return palindromeString
        else:
            print("Invalid!")
                
                
        
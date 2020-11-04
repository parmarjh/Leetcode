
# link : https://leetcode.com/problems/longest-palindromic-substring/

# need to optimize this program
# we can do that in many ways
#  use index (start,end)  instead  of whole string
#remove extra variable
def isPalindrome(s,start,end):
    s = s[start:end]
    return s == s[-1::-1]
    
      
def longestPalindrome(s):  
    n = len(s)
    start = 0 
    end = 0
    ans_length = 0
    for mid in range (0,n):
        i = 0
        # print("middle = ",mid)
        while(mid+i<n and mid-i>=0):
            # print("checking1  ",s[mid-i:mid+i+1], "= ", isPalindrome(s[mid-i:mid+i+1]))
            if not isPalindrome(s,mid-i,mid+i+1):
                i+=1
                continue
            if ans_length < len(s[mid-i:mid+i+1]):
                ans_length = len(s[mid-i:mid+i+1])
                start = mid-i
                end = mid+i+1
                # ans_string = s[mid-i:mid+i+1]
            i+=1
    
        i = 1
        while(mid-i+1>=0 and mid+i <n):
            # print("checking2  ",s[mid-i+1:mid+i+1], "= ", isPalindrome(s[mid-i+1:mid+i+1]))
            if not isPalindrome(s,mid-i+1,mid+i+1):
                i+=1
                continue
            if ans_length < len(s[mid-i+1:mid+i+1]):
                ans_length = len(s[mid-i+1:mid+i+1])
                start = mid-i+1
                end = mid+i+1
                # ans_string = s[mid-i+1:mid+i+1]
            i+=1
            # ans_length = max(ans_length,len(s[mid:mid+i+1]))
    #     print("ANS : " ,ans_length, ans_string)
    print("ANS : " ,ans_length, s[start:end])

longestPalindrome("abcba")


############################################################################################3


#ACCEPTED SOLUTION :) finally

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len   
        n = length(s)
        start = 0 
        end = 0
        ans_length = 0
        for mid in range (0,n):
            i = 0
            while(mid+i<n and mid-i>=0):
                if s[mid-i] != s[mid+i]:
                    i+=1
                    break
                tmp = len(s[mid-i:mid+i+1])
                if ans_length < tmp:
                    ans_length = tmp
                    start = mid-i
                    end = mid+i+1
                i+=1

            i = 1
            while(mid-i+1>=0 and mid+i <n):
                if s[mid-i+1] != s[mid+i]:
                    i+=1
                    break
                tmp = len(s[mid-i+1:mid+i+1])
                if ans_length < tmp:
                    ans_length = tmp
                    start = mid-i+1
                    end = mid+i+1
                i+=1
        return s[start:end]




##
# we can improve this by not using isPalindrome function 
#just need to check start and end char , are they equal or not 

#it will affects a lot in time complexity

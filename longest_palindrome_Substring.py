
# link : https://leetcode.com/problems/longest-palindromic-substring/

# need to optimize this program
# we can do that in many ways
#  use index (start,end)  instead  of whole string
#remove extra variable
def isPalindrome(s):
    return s == s[-1::-1]
      
def longestPalindrome(s):  
    length  = len(s)
    n = len(s)
    ans_string = ''
    ans_length = 0
    for mid in range (0,length):
        i = 0
        # print("middle = ",mid)
        while(mid+i<n and mid-i>=0):
            # print("checking1  ",s[mid-i:mid+i+1], "= ", isPalindrome(s[mid-i:mid+i+1]))
            if not isPalindrome(s[mid-i:mid+i+1]):
                i+=1
                continue
            if ans_length < len(s[mid-i:mid+i+1]):
                ans_length = len(s[mid-i:mid+i+1])
                ans_string = s[mid-i:mid+i+1]
            i+=1
    
        i = 1
        while(mid-i+1>=0 and mid+i <n):
            # print("checking2  ",s[mid-i+1:mid+i+1], "= ", isPalindrome(s[mid-i+1:mid+i+1]))
            if not isPalindrome(s[mid-i+1:mid+i+1]):
                i+=1
                continue
            if ans_length < len(s[mid-i+1:mid+i+1]):
                ans_length = len(s[mid-i+1:mid+i+1])
                ans_string = s[mid-i+1:mid+i+1]
            i+=1
            # ans_length = max(ans_length,len(s[mid:mid+i+1]))
    #     print("ANS : " ,ans_length, ans_string)
    print("ANS : " ,ans_length, ans_string)

longestPalindrome("faabcbadfa")

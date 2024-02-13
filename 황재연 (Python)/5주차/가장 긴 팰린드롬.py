def solution(strs):
    ans = 0 
    for i in range(len(strs)):
        for j in range(i, len(strs)):
            if strs[i:j + 1] == strs[i:j + 1][::-1]:
                ans = max(ans,j-i+1)
    return ans
import java.util.*;
public class Solution {
    public int solution(String s) {
        for (int i = s.length(); i > 0; i--) {
            for (int j = 0; j + i <= s.length(); j++) {
                if (Palindrome(s, j, j + i - 1)) {
                    return i;
                }
            }
        }
        return 0;
    }

    boolean Palindrome(String value, int start, int end){
        while (start <= end) {
            if (value.charAt(start) != value.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
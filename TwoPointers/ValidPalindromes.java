public boolean isPalindrome(String s) {
        int l = 0, r = s.length()-1;
        while (l<r){
            char i = s.charAt(l);
            char j = s.charAt(r);
            if(!Character.isLetterOrDigit(i)){
                l++;
                continue;
            }
            if(!Character.isLetterOrDigit(j)){
                r--;
                continue;
            }
            if(Character.toLowerCase(i)!=Character.toLowerCase(j)){
                return false;
            }

            l++;
            r--;

        }

        return true;
    }



// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.

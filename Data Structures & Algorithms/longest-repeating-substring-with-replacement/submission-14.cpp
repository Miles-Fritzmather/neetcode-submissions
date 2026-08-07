class Solution {
public:
    int characterReplacement(string s, int k) {
        int best = 0;
        int l = 0;
        int count[26] = {};

        for (int r = 0; r < s.length(); r++) {
            count[s[r] - 'A'] += 1;

            int max = count[0];
            int len = r - l + 1;
            for (int i = 0; i < 26; i++) {
                max = highest(max, count[i]);
            }
            
            while (len - max > k) {
                count[s[l++] - 'A'] -= 1;
                len = r - l + 1;
            }

            best = highest(best, len);
        }

        return best;
    }

    int highest(int a, int b) {
        if (a > b) return a;
        else return b;
    }
};
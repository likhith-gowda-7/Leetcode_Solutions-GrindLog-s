class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels={"a","e","i","o","u"}
        letters=defaultdict(int)
        consonant_count=0
        vowel_count=0
        for ch in s:
            letters[ch]+=1
            if(ch in vowels):
                vowel_count=max(vowel_count,letters[ch])
            else:
                consonant_count=max(consonant_count,letters[ch])
        return vowel_count+consonant_count
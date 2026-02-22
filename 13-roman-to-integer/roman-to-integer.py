class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0

        sc = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        gc = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for c in sc:
            if c in s:
                r += sc[c]
                s = s.replace(c, "")

        for c in s:
            r += gc[c]
        
        return r
        
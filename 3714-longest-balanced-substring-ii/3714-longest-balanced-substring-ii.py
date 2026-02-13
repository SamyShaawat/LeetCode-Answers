class Solution:
    def longestBalanced(self, s: str) -> int:
        # Maps store the first occurrence of a specific difference (state)
        ab = {0: 0}
        bc = {0: 0}
        ca = {0: 0}
        abc = {0: 0}

        cnta = cntb = cntc = 0
        longestLength = 1

        # Handle same-character substrings (e.g., "aaaa")
        currentChar = s[0]
        length = 0
        for ch in s:
            if ch == currentChar:
                length += 1
            else:
                length = 1
                currentChar = ch
            longestLength = max(longestLength, length)

        # Handle balanced substrings using Prefix Sums
        for i, ch in enumerate(s):
            if ch == 'a':
                cnta += 1
            elif ch == 'b':
                cntb += 1
            else:
                cntc += 1

            # Pack two values into one key (same as bit-shifting in C++)
            abId  = ((cntb - cnta) << 32) | (cntc & 0xFFFFFFFF)
            bcId  = ((cntb - cntc) << 32) | (cnta & 0xFFFFFFFF)
            caId  = ((cntc - cnta) << 32) | (cntb & 0xFFFFFFFF)
            abcId = ((cntb - cnta) << 32) | ((cntc - cnta) & 0xFFFFFFFF)

            if abId not in ab:
                ab[abId] = i + 1
            else:
                longestLength = max(longestLength, i - ab[abId] + 1)

            if bcId not in bc:
                bc[bcId] = i + 1
            else:
                longestLength = max(longestLength, i - bc[bcId] + 1)

            if caId not in ca:
                ca[caId] = i + 1
            else:
                longestLength = max(longestLength, i - ca[caId] + 1)

            if abcId not in abc:
                abc[abcId] = i + 1
            else:
                longestLength = max(longestLength, i - abc[abcId] + 1)

        return longestLength
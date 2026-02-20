class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case: if the string is short, it's already as large as it gets
        if not s:
            return ""
        
        results = []
        count = 0
        i = 0
        
        # Step 1: Split s into its top-level special substrings
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # Step 2: Recurse on the inner part (between the first '1' and last '0')
                # We strip the leading '1' and trailing '0', process the inside,
                # then wrap it back up.
                inner_part = self.makeLargestSpecial(s[i + 1:j])
                results.append(f"1{inner_part}0")
                i = j + 1
        
        # Step 3: Sort the special substrings descending to get the largest lex order
        results.sort(reverse=True)

        # Step 4: Join and return
        return "".join(results)
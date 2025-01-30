class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Edge case
        if not s:
            return True
  
        sPointer = 0

        for tPointer in range(len(t)):
            if s[sPointer] == t[tPointer]:
                sPointer += 1

            if sPointer == len(s):
                return True
            
        return False
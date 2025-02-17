class RansomNote:

    def canConstruct(self, ransomNote, magazine):

        mMap = {}
        for mLetter in magazine:
            if mLetter in mMap:
                mMap[mLetter] += 1
            else:
                mMap[mLetter] = 1

        for rLetter in ransomNote:
            if rLetter in mMap:
                if mMap[rLetter] > 0:
                     mMap[rLetter] -= 1
                else:
                    return False
            else:
                return False

        return True

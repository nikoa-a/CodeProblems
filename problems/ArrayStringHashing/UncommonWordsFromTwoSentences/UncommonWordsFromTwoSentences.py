class UncommonWordsFromTwoSentences:

    def uncommonFromSentences(self, s1, s2):

        wordFreq = {}

        for word in s1.split() + s2.split():
            # Increment the frequency of the word in the dictionary by 1
            wordFreq[word] = wordFreq.get(word, 0) + 1

        res = []
        for word, count in wordFreq.items():
            if count == 1:
                res.append(word)

        return res
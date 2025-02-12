class StringEncodeAndDecode (object):

    # The shift value is used to encode and decode the strings
    shift = 3

    def encode(self, strs):

        # Initialize the encoded string
        encodedString = ""
        # Iterate through the strings
        for s in strs:
            # Encode each character in the string
            for char in s:
                # Shift the character by the shift value
                encodedChar = chr(ord(char) + self.shift)
                # Add the encoded character to the encoded string
                encodedString += encodedChar
            # Add a null character to separate the strings
            encodedString += '\0'

        # Return the encoded string
        return encodedString
    
    
    def decode(self, s):

        # Initialize the list of decoded strings
        decodedStringsList = []
        # Initialize the decoded string
        decodedString = ""
        # Iterate through the encoded string
        for char in s:
            # Check if the character is a null character
            if char == "\0":
                # Add the decoded string to the list of decoded strings
                decodedStringsList.append(decodedString)
                decodedString = ""
            # Decode the character
            else:
                decodedChar = chr(ord(char) - self.shift)
                decodedString += decodedChar

        # Return the list of decoded strings
        return decodedStringsList

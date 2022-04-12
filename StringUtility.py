class StringUtility:

  def __init__(self, s):
    self.string = s

  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    for i in range(len(self.string)):
      if (self.string[i] == 'a' or self.string[i] == 'e' or self.string[i] == 'i' or self.string[i] == 'o' or self.string[i] == 'u' ):
        count += 1
    if (count >= 5):
      return "many"
    else:
      return "{}".format(count)

  def bothEnds(self):
    if(len(self.string) <= 2):
      return ''
    else:
      return self.string[0] + self.string[1] + self.string[len(self.string)-2] + self.string[len(self.string)-1]

  def fixStart(self):
    if len(self.string) <= 1 :
      return self.string

    #creates a list of characters in the string by starting with the first char, then appending a * if the character at the given index is the same as the firstChar, appending the character from the string if different.
    firstChar = self.string[0]
    result = [firstChar]
    for i in range(1, len(self.string)):
      if (self.string[i] == firstChar):
        result.append('*')
      else:
        result.append(self.string[i])

    #converts the result list into a string
    resultString = ""
    for i in result:
      resultString += i
      
    return resultString

  def asciiSum(self):
    result = 0
    for i in range(len(self.string)):
      result += ord(self.string[i])
    return result

  def cipher(self):
    shift = len(self.string)
    result = []
    for i in range(shift):
      if(self.string[i] == ' '):
        result.append(' ')
      elif((ord(self.string[i]) + shift) > 122) : 
        #print("yo{} {}".format((ord(self.string[i]) + shift - 97) % 26 + 97, self.string[i]))
        result.append(chr( (ord(self.string[i]) + shift - 97) % 26 + 97))
      elif ((ord(self.string[i]) + shift) > 90 and (ord(self.string[i]) + shift) < 97):
        #print("yo{} {}".format((ord(self.string[i]) + shift - 65) % 26 + 65, self.string[i]))
        result.append(chr( (ord(self.string[i]) + shift - 65) % 26 + 65))
      else:
        result.append(chr( ord(self.string[i]) + shift))

    resultString = ""
    for i in result:
      resultString += i

    return resultString
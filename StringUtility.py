class StringUtility:
  """
  NOTE: I did the extra credit after writing the code normally. So, all of the normal coding I did is commented out as multiline strings.
  """

  #constructor
  def __init__(self, s):
    self.string = s

  #returns the string
  def __str__(self):
    return self.string

  #counts up how many vowels are in each string by storing the vowels in a list and then returning the length of the list if 
  def vowels(self):
    return "many" if len([i for i in self.string if i in 'aeiou']) >= 5 else "{}".format(len([i for i in self.string if i in 'aeiou']))
    """
    count = 0
    for i in range(len(self.string)):
      if (self.string[i] == 'a' or self.string[i] == 'e' or self.string[i] == 'i' or self.string[i] == 'o' or self.string[i] == 'u' ):
        count += 1
    if (count >= 5):
      return "many"
    else:
      return "{}".format(count)
    """

  #returns a string of the beginning 2 char and ending 2 char
  def bothEnds(self):
    return '' if len(self.string) <= 2 else self.string[0] + self.string[1] + self.string[len(self.string)-2] + self.string[len(self.string)-1]
    #The follow
    """
    if(len(self.string) <= 2):
      return ''
    else:
      return self.string[0] + self.string[1] + self.string[len(self.string)-2] + self.string[len(self.string)-1]
    """

  #returns the string but all instances (except for the first) of the first character are censored
  def fixStart(self):
    #print(self.string[0])
    return self.string if len(self.string) <= 1 else self.string[0]+''.join(['*' if (self.string[i] in self.string[0]) else self.string[i] for i in range(1, len(self.string))])

    """
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
    """

  #returns the sum of all the ascii values in the string
  def asciiSum(self):
    return sum([ord(i) for i in self.string])

    """
    result = 0
    for i in range(len(self.string)):
      result += ord(self.string[i])
    return result
    """

  #shifts the string to the right by the length of the string
  def cipher(self):
    return ''.join([" " if i == ' ' else chr((ord(i)+ len(self.string) - 65)%26 + 65) if i.isupper() else chr((ord(i) + len(self.string) - 97)%26 + 97) for i in self.string])

    """
    shift = len(self.string)
    result = []
    for i in range(shift):
      if(self.string[i] == ' '):
        result.append(' ')
      elif((ord(self.string[i]) + shift) > 122) : 
        result.append(chr( (ord(self.string[i]) + shift - 97) % 26 + 97))
      elif ((ord(self.string[i]) + shift) > 90 and (ord(self.string[i]) + shift) < 97):
        result.append(chr( (ord(self.string[i]) + shift - 65) % 26 + 65))
      else:
        result.append(chr( ord(self.string[i]) + shift))

    resultString = ""
    for i in result:
      resultString += i

    return resultString
    """
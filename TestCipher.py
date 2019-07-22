#  File: TestCipher.py

#  Description: A program that decodes or encodes a phrase using two different methods.

#  Student Name: Derrick Hung

#  Student UT EID: dsh989

#  Partner Name: Samuel Talaber

#  Partner UT EID:sjt925

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/9/2018

#  Date Last Modified: 9/10/2018

# takes a single string as input parameter and returns a string
def substitution_encode ( strng ):
    #list of characters for the cipher text
    cipher = ['q' ,'a' ,'z' ,'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't' ,'g' ,'b' ,'y' ,'h' ,'n' ,'u' ,'j' ,'m' ,'i' ,'k', 'o' ,'l' ,'p']
    alpha = ["a", "b", "c",  "d",  "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p","q","r", "s", "t", "u","v", "w","x", "y", "z"]

    #change string into a list format
    strng= list(strng)
    #loop that iterate over the length of the string with a try block that skip an iteration when space is detected
    for x in range (len(strng)):
        try:
            #get order of an element of alphabet within the string list
            idx = ord(strng[x])-ord("a")
            #set the original text elements into cipher elements
            strng[x] = cipher[idx]

        except IndexError:
            continue
    #join the list of character into a string
    strng = "".join(strng)
    return strng

# takes a single string as input parameter and returns a string
def substitution_decode ( strng ):
    cipher = ['q' ,'a' ,'z' ,'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't' ,'g' ,'b' ,'y' ,'h' ,'n' ,'u' ,'j' ,'m' ,'i' ,'k', 'o' ,'l' ,'p']
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    strng = list(strng)
    #loop that iterate over the length of the encoded string, with try block that skips when space is detected
    for x in range(len(strng)):
        try:
            #idx is a variable that get the order of element within the cipher list order
            idx= cipher.index(strng[x])
            #convert idx added with the ASCII value of "a" back to character format
            strng[x]=chr(idx+97)

        except ValueError:
            continue
    #recombine the list of elements back to string format
    strng = "".join(strng)
    return strng

# takes two strings as input parameter and returns a string
def vigenere_encode ( strng, passwd ):
    #convert strng and passwd from string format into list format
    strng = list(strng)
    passwd = list(passwd)

    #loop to extend the passwd list with itself to match the length of the strng list
    for x in range(len(strng) - len(passwd)):
        passwd.extend(passwd[x])
    #loop to detect the spacing within the strng list and insert it within the passwd list and deleting the last element when 1 space is inserted
    for x in range(len(strng)):
        if strng[x] == " ":
            passwd.insert(x, " ")
            passwd = passwd[:-1]

    #loop through the length of the string
    for y in range(len(strng)):
        try:
            #if the character at our position is not a space,
            if strng[y] !=' ':
                #if statement to limit the encoding to include only lower case letters
                if ord(strng[y])>=97 and ord(strng[y])<=122:
                #we take the character value of the remainder of the difference between strng and password from 26 and the character value of a
                    strng[y] = chr(((ord(strng[y]) - ord('a') + ord(passwd[y]) - ord('a')) % 26) + ord('a'))
        #skip an iteration when space(error) is detect
        except:
            continue
    strng = "".join(strng)
    return strng


# takes two strings as input parameter and returns a string
#I think it is getting thrown off because of the spaces with seal here
def vigenere_decode ( strng, passwd ):
    ##convert strng and passwd from string format into list format
    strng = list(strng)
    passwd = list(passwd)
    #loop to extend the passwd list with itself to match the length of the strng list
    for x in range(len(strng) - len(passwd)):
        passwd.extend(passwd[x])
    # loop to detect the spacing within the strng list and insert it within the passwd list and deleting the last element when 1 space is inserted
    for x in range(len(strng)):
        if strng[x] == " ":
            passwd.insert(x, " ")
            passwd = passwd[:-1]

    # loop through the length of the string
    for y in range(len(strng)):
        try:
            #as long as the character in strng is not y
            if strng[y] != ' ':
                # if statement to limit the encoding to include only lower case letters
                if ord(strng[y]) >= 97 and ord(strng[y]) <= 122:
                    #and if its ASCII value is greater than the corresponding passwd characters value
                    if ord(strng[y]) >= ord(passwd[y]):
                        #set that spot to a new character whose value is the difference between the strng and passwd value along with the value of a
                        strng[y] = chr(ord(strng[y]) + ord('a') - ord(passwd[y]))
                    else:
                    #if the ASCII value is less which would cause a negative number, add 26 (the number of letters in the alph) and then the ASCII value of A to return it to the original value
                        strng[y] = chr((ord(strng[y])+26 -ord(passwd[y]))+ ord('a'))
        #skip an iteration if space or error is detected
        except:
            continue
    strng = "".join(strng)
    return strng

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  #read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

'''
this is an incredibly naive interface for doing something
i find occasionally useful. i may come back to improve it
in order to practice proper tkinter design.
'''

import base64
import itertools
from string import ascii_letters
from tkinter import *

def getinput():
    outputtext.delete("1.0", "end")
    text = inputtext.get(1.0, END+"-1c")
    key = keyfield.get(1.0, END+"-1c")
    return text, key

# base64^-1 -> xor. (xor is its own inverse)
def totext():
    text, key = getinput()
    decodedByte = base64.b64decode(text)
    xor_string = ""
    for a, b in zip(decodedByte, itertools.cycle(key)):
        xor_string += chr(a ^ ord(b))
    outputtext.insert(END, xor_string.strip())

# xor -> base64.
def tobase64():
    text, key = getinput()
    xor_string = ""
    for a, b in zip(text, itertools.cycle(key)):
        xor_string += chr(ord(a) ^ ord(b))
    encodedByte = base64.encodebytes(xor_string.encode("utf8"))
    encodedStr = str(encodedByte, "utf8").strip()
    outputtext.insert(END, encodedStr)

def bin2text(text: str):
    return "".join([chr(int(num, 2)) for num in text.split(" ")])
                    
def text2bin(text: str):
    return "".join([format(ord(char),'#010b')[2:] + " " for char in text])

# this makes sure any format binary works, so long as the characters
# are 8-bit. spacing and line breaks don't matter.
def mash2string(rows: list):
    output = ""
    rows = "".join(rows).strip()
    rows = "".join(rows.split(" ")) # now it's just "01101001001010010...010101".
    for index, chara in enumerate(rows): # group in eights.
        output += chara
        output += " " if (index + 1) % 8 == 0 else ""
    return output.strip()

def binascii():
    outputtext.delete("1.0", "end")
    text = inputtext.get(1.0, END+"-1c").split("\n")
    output = ""
    if any([x in ascii_letters + "23456789\',.*()[]\"" for x in "".join(text)]):
        for index, row in enumerate(text):
            if (index + 1) != len(text):
                output += text2bin(row.strip()) + "00001010" # add ord(\n) = 10 after a line.
            else:
                output += text2bin(row.strip())
    else:
        text = mash2string(text)
        output += bin2text(text)
    outputtext.insert(END, output)

# lazily non-OOP implementation for now. i'll likely change this later.
if __name__ == "__main__":

    screen = Tk()
    screen.geometry("395x265")
    screen.title("Binary and XOR tool")

    inputtext = Text(screen, font = ("courier", 11), height=6, width=43)
    Label(screen, text = "key", font = ("courier", 11), justify="left").grid(row=1, column=1)
    keyfield = Text(screen, font = ("courier", 11), height=1, width=20)
    Button(screen, text="ascii <-> binary", fg='blue', command = binascii).grid(row=2, column=0)
    Button(screen, text="xor -> base64", fg="blue", command = tobase64).grid(row=2, column=2, sticky="w")
    Button(screen, text="base64 -> xor", fg="blue", command = totext).grid(row=2, column=2, sticky="e")
    outputtext = Text(screen, font = ("courier", 11), height=6, width=43)

    inputtext.grid(row=0, column=0, columnspan=4)
    keyfield.grid(row=1, column=2, sticky="w")
    outputtext.grid(row=3, column=0, columnspan=4)

    screen.mainloop()

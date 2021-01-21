from string import ascii_letters
from tkinter import *
import glob

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
                
if __name__ == "__main__":

    screen = Tk()
    screen.geometry("395x290+600+400")
    screen.title("Binary <-> Text translator")
    
    def getInput():
        text2.delete("1.0", "end")
        text = text1.get(1.0, END+"-1c").split("\n")
        output = ""
        if any([x in ascii_letters + "23456789\',.*()[]\"" for x in "".join(text)]):
            for index, row in enumerate(text):
                if (index + 1) != len(text):
                    output += text2bin(row.strip()) + "00001010"
                else:
                    output += text2bin(row.strip())
        else:
            text = mash2string(text)
            output += bin2text(text)
        text2.insert(END, output)

    text1 = Text(screen, height = 6, width = 42, font = ("courier", 11))
    text2 = Text(screen, height = 6, width = 42, font = ("courier", 11))
    button = Button(screen, text="Translate.", fg='blue', command = getInput)

    text1.place(x = 5, y = 5)
    text2.place(x = 5, y = 175)
    button.place(x = 5, y = 131)

    screen.mainloop()

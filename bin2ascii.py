from string import ascii_letters
import glob

def bin2text(filename: str):
    with open(filename) as file:
        with open("output_text.txt", "a") as output:
            for row in file:
                output.write("".join([chr(int(num, 2)) for num in row.strip().split(" ")]))
                    
def text2bin(filename: str):
    with open(filename) as file:
        for row in file:
            with open("output_bin.txt", "a") as output:
                output.write("".join([format(ord(char),'#010b')[2:] + " " for char in row]))
                
if __name__ == "__main__":
    # choose filename that does not contain 'output'.
    filenames = glob.glob("*.txt")
    for name in filenames:
        if "output" not in name:
            filename = name
    file = open(filename, "r")
    firstline = file.readline()
    if any([x in ascii_letters for x in firstline]):
        text2bin(filename)
    else:
        bin2text(filename)

from collections import Counter
import re
f = open("C:/Users/David/Desktop/fyp//outSen.txt")
def read(passage):
    words = re.findall(r'\w+', passage)
    count = Counter(words).most_common(10)
    print count

for line in f:
    if "RT @" in line: #get retweet
        with open("C:/Users/David/Desktop/fyp//senRT.txt", "a") as text_file:
            text_file.write(str(re.findall(r"RT @(\w+)", line)))
            text_file.write("\n")
    if "@" in line:
        with open("C:/Users/David/Desktop/fyp//senMT.txt", "a") as text_file:
            text_file.write(str(re.findall(r"@(\w+)", line)))
            text_file.write("\n")
    if "#" in line:
        with open("C:/Users/David/Desktop/fyp//senHash.txt", "a") as text_file:
            text_file.write(str(re.findall(r"#(\w+)", line)))
            text_file.write("\n")
            
with open("C:/Users/David/Desktop/fyp//senRT.txt") as f:
    passage=f.read()
    read(passage)

with open("C:/Users/David/Desktop/fyp//senMT.txt") as f:
    passage=f.read()
    read(passage)
            
with open("C:/Users/David/Desktop/fyp//senHash.txt") as f:
    passage=f.read()
    read(passage)



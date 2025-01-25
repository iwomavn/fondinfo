import re

def process_file(filename: str):
    counters = [0] * 26 

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
  
    words = re.findall(r"\b[a-zA-Z]", content)  

    for letter in words:
        index = ord(letter.lower()) - ord('a') 
        if 0 <= index < 26:  
            counters[index] += 1

    for i, count in enumerate(counters):
        if count > 0:
            letter = chr(i + ord('a'))
            print(f"Le parole che iniziano con '{letter}' sono {count}")

if __name__ == "__main__":
    process_file("license.txt")

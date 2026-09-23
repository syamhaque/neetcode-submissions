from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    charCountMap = {}
    
    for char in word:
        count = charCountMap.get(char, 0)
        charCountMap[char] = count + 1
    
    return charCountMap


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

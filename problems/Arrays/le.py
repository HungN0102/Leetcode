# Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words

# Example:
# ["this", "that", "did", "deed", "them!", "a"]
# -> ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']

def minimumCharactersForWords(words):
    hashmap = {}
    for word in words:
        wordFrequency = countFrequency(word)
        for k in wordFrequency:
            if k not in hashmap:
                hashmap[k] = wordFrequency[k]
                continue
            hashmap[k] = max(hashmap[k], wordFrequency[k])
        
    results = []    
    for k, v in hashmap.items():
        for _ in range(v):
            results.append(k)
    return results


def countFrequency(word):
    hashmap = {}
    for char in word:
        if char not in hashmap:
            hashmap[char] = 0
        hashmap[char] += 1
    return hashmap

minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"])
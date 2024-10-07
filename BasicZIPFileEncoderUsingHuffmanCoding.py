#Hacktoberfest Contribution :-
#Basic ZIP File Encoder Using Huffman Coding
import heapq
from collections import defaultdict

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

# Function to build the codes from the Huffman Tree
def build_codes(node, prefix='', codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes(node.left, prefix + '0', codes)
        build_codes(node.right, prefix + '1', codes)
    return codes

# Function to encode the text using Huffman Coding
def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

# Example usage
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    encoded_text, codes = huffman_encoding(text)
    print("Encoded Text:", encoded_text)
    print("Huffman Codes:", codes)

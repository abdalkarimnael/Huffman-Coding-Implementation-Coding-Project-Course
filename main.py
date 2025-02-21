import heapq
from collections import Counter, defaultdict
import math

# Step 1: Read the text file (story content should be in a file named "to_build_a_fire.txt")
with open(r"Story.txt", "r") as file:
    story = file.read().lower()


# Step 2: Calculate character frequency
frequency = Counter(c for c in story if c.isprintable() and c != '\n')  # Ignore non-printable characters
total_chars = sum(frequency.values())

# Step 3: Calculate probabilities
probabilities = {char: freq / total_chars for char, freq in frequency.items()}

# Step 4: Compute entropy
entropy = -sum(p * math.log2(p) for p in probabilities.values())

# Step 5: Huffman encoding
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(tree):
    codes = {}

    def traverse(node, code):
        if node:
            if node.char is not None:
                codes[node.char] = code
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(tree, "")
    return codes

huffman_tree = build_huffman_tree(frequency)
huffman_codes = generate_huffman_codes(huffman_tree)

# Step 6: Calculate average number of bits per character using Huffman
average_bits_per_char = sum(probabilities[char] * len(huffman_codes[char]) for char in huffman_codes)

# Step 7: Calculate total bits using ASCII and Huffman
nascii = total_chars * 8  # 8 bits per character in ASCII
nhuffman = sum(frequency[char] * len(huffman_codes[char]) for char in huffman_codes)

# Step 8: Compression percentage
compression_percentage = 100 * (1 - (nhuffman / nascii))

# Display results
print(f"Total characters: {total_chars} \n\n\n")
print(f"Character frequencies:\n{frequency}\n\n\n")
print(f"Character probabilities:\n{probabilities}\n\n\n")
print(f"Entropy: {entropy:.4f} bits/character\n\n\n")
print(f"Huffman Codes:\n{huffman_codes}\n\n\n")
print(f"Average bits/character with Huffman: {average_bits_per_char:.4f}\n\n\n")
print(f"Total bits (ASCII): {nascii}\n\n\n")
print(f"Total bits (Huffman): {nhuffman}\n\n\n")
print(f"Compression percentage: {compression_percentage:.2f}%\n\n\n")

# Tabulate results
import pandas as pd

table_data = {
    "Character": list(frequency.keys()),
    "Frequency": list(frequency.values()),
    "Probability": [probabilities[char] for char in frequency.keys()],
    "Huffman Code": [huffman_codes[char] for char in frequency.keys()]
}
df = pd.DataFrame(table_data)
print(df)

# Huffman Coding Implementation

## Team Members
 - **Abdalkarim Eiss** (Me)
 - **Musab Masalmah**

## Overview
This project implements Huffman coding, a lossless data compression algorithm, to analyze and compress text data efficiently. The dataset used is the short novel **"To Build a Fire"** by Jack London. The process includes calculating character frequencies, generating Huffman codes, computing entropy, and comparing compression results with standard ASCII encoding.

## Project Details
### **Theoretical Background**
- **Huffman Coding** assigns variable-length codes to characters based on their frequencies.
- **Prefix-Free Property** ensures that no code is a prefix of another, allowing unique decoding.
- **Huffman Tree Construction** is performed using a greedy approach.
- **Efficiency**: The algorithm runs in **O(n log n)** time.

### **Analysis Performed**
1. **Character Frequency Calculation**
2. **Character Probability Computation**
3. **Huffman Code Assignment**
4. **Entropy Calculation**
5. **Bits per Character Evaluation**
6. **Total Bits Comparison (ASCII vs. Huffman)**
7. **Compression Percentage Calculation**

## Results
| Metric | Value |
|-------------------------|-------------|
| **Total Characters** | 37,733 |
| **Entropy** | 4.1785 bits/char |
| **Avg. Huffman Bits/Char** | 4.2248 |
| **Total Bits (ASCII)** | 301,864 |
| **Total Bits (Huffman)** | 159,416 |
| **Compression Percentage** | **47.19%** |

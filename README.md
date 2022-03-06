
# Huffman Coding Compression Algorithm

With the advent of Digital Era, we need a lot of secondary memory(Hard Disks, SSDs etc) to store our
data. 

I have built this project to address the same.

With this project, I have built a Compression Algorithm which works on 
Huffman Coding. This Algorithm can work on any type of file and can compress 
a given file so that it takes fairly less space, compared to before.

I also have implemented the decompression functionality, with which we can recover 
our original data back from the compressed file.


# What is Huffman Coding Algorithm:

It is lossless data compression algorithm. As this is a lossless compression
algorithm, the file compression ratio is not the best but it ensures that there is
no data loss at all because of the compression.

# Idea of Huffman Coding:

The idea is to assign variable codes to the different bytes present in the file that we are compressing.

Each byte can be represented by a 8 bit ASCII code.
With Huffman coding, we try to assign shorter codes to most frequently occuring bytes and longer codes to less
frequently occuring bytes. 

The Huffman codes are in bits, so it might be the case that most frequently occuring bytes can be 
represented by 7 bits whereas for less frequently occuring bytes, we use 9 bits.

In essence, we will be saving some space.

# Huffman Coding diagram

![App Screenshot](screenshots/Huffman-encoding-procedure.png?raw=true)


credits: Research Gate



# PseudoCode

### Compression
1) Build a frequency dictionary. This will store the mappings b/w a byte's ASCII code and its frequency in the file.

2) Build a min heap. With the help of this min heap, we will build the Huffman Tree. This Huffman Tree will have more frequently occuring 
bytes at a higher level, so that their codes are smaller. This tree will have less frequently occuring bytes at deeper levels so that their codes are bigger.

3) Build the Huffman Tree by selecting 2 min node, popping them from min heap and merging them. Also we make the merged node as parent of the 2 nodes taken from min heap. Then we push this node back into min heap.

4) Assign codes to each byte (by traversing the Huffman Tree from root to leaf)

5) Encode the input text (by replacing character with its code)

6) Each byte is made of 8 bits. We need to ensure the final encoded bit stream is multiple of 8 for proper construction of a byte.
If this is not the case, we pad the sequence. Also we store the number of bits padded as extra information, convert this information to a 8 bit sequence and add it to the front of encoded bit stream. 

7) Write this encoded data to a binary file. This is the compressed file.


### Decompression

1) Read the Compressed (Binary) File.

2) Read the padding information stored in the first 8 bits. Remove this information and the extra padded bits from the end.

3) Decode the bits - read the bits and replace the valid Huffman Code bits with the ASCII codes.

4) Save the decoded data into output file.

# Navigation of the project folder

1) Huffman_Coding : package containing the modules and classes for implementing the Huffman Coding compression algorithm.

2) logger: package containing the modules and classes for implementing the class responsible for logging.

3) main.py: main script of the project.

4) input_files: The folder containing the input files for the compression.

5) compressed_files: folder containing the compressed files.

6) decompressed_files: folder containing the decompressed files.

7) logs: folder storing the logs generated by the project.







## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


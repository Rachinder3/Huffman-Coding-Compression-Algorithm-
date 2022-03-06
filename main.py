from Huffman_Coding.Huffman_Coding import HuffmanCoding

if __name__=="__main__":
    input_file_path="input_files/414982.jpg"
    compressed_file_path = "compressed_files/414982"
    decompressed_file_path = "decompressed_files/decompressed_414982"

    hc = HuffmanCoding(input_file_path)
    # compressing the file

    hc.compress(compressed_file_path)

    # decompressing the file

    hc.decompress(compressed_file_path, decompressed_file_path)
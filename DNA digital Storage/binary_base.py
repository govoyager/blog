def binary_to_dna(binary_string):
    dna_sequence = ""
    binary_length = len(binary_string)

    # Ensure the binary string length is a multiple of 2
    if binary_length % 2 != 0:
        binary_string = "0" + binary_string  # Pad with a leading 0 if needed

    # Define a mapping from binary to DNA bases
    binary_to_dna_mapping = {
        "00": "A",
        "01": "C",
        "10": "G",
        "11": "T"
    }

    # Iterate through the binary string in chunks of 2
    for i in range(0, binary_length, 2):
        chunk = binary_string[i:i + 2]
        dna_base = binary_to_dna_mapping[chunk]
        dna_sequence += dna_base

    return dna_sequence

# Example usage
binary_data = "101101001110010"  # Replace with your binary data
dna_sequence = binary_to_dna(binary_data)
print("Binary:   ", binary_data)
print("DNA Seq.: ", dna_sequence)

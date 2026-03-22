import argparse
import random
import os

def get_mapping(seed_value=12345):
    """Creates a consistent 1:1 map for all 256 ASCII values."""
    all_bytes = list(range(256))
    shuffled = all_bytes[:]
    random.seed(seed_value)
    random.shuffle(shuffled)
    
    encrypt_table = bytes(shuffled)
    decrypt_table = bytearray(256)
    for original, substitution in enumerate(shuffled):
        decrypt_table[substitution] = original
        
    return encrypt_table, bytes(decrypt_table)

def main():
    parser = argparse.ArgumentParser(description="8-bit Substitution Cipher")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", action="store_true", help="Encrypt mode")
    group.add_argument("-d", action="store_true", help="Decrypt mode")
    parser.add_argument("input", help="Input file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    
    args = parser.parse_args()
    en_map, de_map = get_mapping()
    active_map = en_map if args.e else de_map
    
    try:
        with open(args.input, 'rb') as f_in:
            data = f_in.read()
        
        result = data.translate(active_map)
        
        with open(args.output, 'wb') as f_out:
            f_out.write(result)
            
        print(f"Success! Result saved to: {args.output}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
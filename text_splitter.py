import os
import re
import logging
from tqdm import tqdm
import argparse

logging.basicConfig(level=logging.INFO)

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', "_", filename)

def get_unique_filename(filename):
    counter = 1
    base_name, ext = os.path.splitext(filename)
    while os.path.exists(filename):
        filename = f"{base_name}_{counter}{ext}"
        counter += 1
    return filename

def split_text(max_length, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    buffer = ""
    part_number = 1

    print("Enter your large text (press ENTER, and then CTRL+D (Linux) or CTRL+Z (Windows) to finish input):")
    
    try:
        while True:
            line = input()
            buffer += line + "\n"
            
            while len(buffer) >= max_length:
                part = buffer[:max_length]
                buffer = buffer[max_length:]
                
                filename = get_unique_filename(os.path.join(output_dir, f"part{part_number}.txt"))
                
                with open(filename, "w") as file:
                    file.write(part)
                
                word_count = len(part.split())
                logging.info(f"Saved {filename} containing {word_count} words.")
                part_number += 1
        
    except EOFError:
        if buffer.strip():
            filename = get_unique_filename(os.path.join(output_dir, f"part{part_number}.txt"))
            with open(filename, "w") as file:
                file.write(buffer)
            word_count = len(buffer.split())
            logging.info(f"Saved {filename} containing {word_count} words.")

def main():
    parser = argparse.ArgumentParser(description="Split text into parts.")
    parser.add_argument("max_length", type=int, help="Maximum length of each part.")
    args = parser.parse_args()

    if args.max_length <= 0:
        print("Invalid maximum length. Please enter a positive integer.")
        return

    split_text(args.max_length)

if __name__ == "__main__":
    main()

import os

def split_text(max_length):
    # Initialize buffer to accumulate input
    buffer = ""
    part_number = 1  # Start numbering parts from 1
    import logging
logging.basicConfig(level=logging.INFO)
    print("Enter your large text (press ENTER, and then CTRL+D (Linux) or CTRL+Z (Windows) to finish input):")
    
    try:
        while True:
            # Read input line by line
            line = input()
            buffer += line + "\n"
            
            # Split the buffer into parts if it exceeds max_length
            while len(buffer) >= max_length:
                part = buffer[:max_length]  # Extract part of text
                buffer = buffer[max_length:]  # Keep the remaining text
                
                # Save the part to a file
                with open(f"part{part_number}.txt", "w") as file:
                    file.write(part)
                
                print(f"Saved part {part_number}.txt")
                part_number += 1  # Increment part number
        
    except EOFError:
        # Handle end of input (CTRL+D or CTRL+Z)
        if buffer:
            # Save the last part if there's any remaining text
            with open(f"part{part_number}.txt", "w") as file:
                file.write(buffer)
            print(f"Saved part {part_number}.txt")

def main():
    max_length = int(input("Enter the maximum length of each part (e.g., 6000): "))
    
    if max_length <= 0:
        print("Invalid maximum length. Please enter a positive integer.")
        return
    
    split_text(max_length)

if __name__ == "__main__":
    main()
  parser = argparse.ArgumentParser(description="Split text into parts.")
    parser.add_argument("max_length", type=int, help="Maximum length of each part.")
    args = parser.parse_args()

    if args.max_length <= 0:
        print("Invalid maximum length. Please enter a positive integer.")
        return
      
      import re

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', "_", filename)  


with open(sanitize_filename(f"part{part_number}.txt"), "w") as file:
    file.write(part)
    split_text(args.max_length)

    def split_text(max_length, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    buffer = ""
    part_number = 1 
    
 
    with open(f"{output_dir}/part{part_number}.txt", "w") as file:
        file.write(part)
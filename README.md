# Text Cutter

Text Cutter is a Python script that helps split large chunks of text into smaller parts of a specified length. This tool is particularly useful for preparing text input for GPT models or similar use cases where text needs to be divided into manageable chunks.

---

## Features

- Splits text into parts based on a user-defined maximum length.
- Automatically saves each part into separate `.txt` files.
- Handles input interruptions gracefully.
- Ensures unique filenames for each part.
- Includes progress tracking with `tqdm`.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Karthikey1/Text-cutter.git
   cd Text-cutter
   ```

2. Install dependencies:
   ```bash
   pip install tqdm
   ```

---

## Usage

Run the script using the following command:
```bash
python script_name.py <max_length>
```

### Example:
To split a text into parts of 1000 characters:
```bash
python script_name.py 1000
```

---

## How It Works

1. Enter your text line by line.
2. Press `CTRL+D` (Linux/Mac) or `CTRL+Z` (Windows) to finish the input.
3. The script saves each part into separate files in the `output` directory.

---

## Contributing

Contributions are welcome! Please create a pull request or open an issue for suggestions and improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

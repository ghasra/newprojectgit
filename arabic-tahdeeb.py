from src.preprocessing.text_content import ArabicTextProcess

# Initialize the processing class
ASP = ArabicTextProcess()

input_filename = 'data.txt'
output_filename = 'output.txt'

try:
    # Open both files: one for reading, one for writing
    # encoding='utf-8' is strictly required for Arabic text support
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:

        print(f"Processing lines from {input_filename}...")

        # Loop through each line in the data.txt file
        for line in infile:
            # Strip whitespace/newlines from the start and end of the line
            text = line.strip()

            # Skip empty lines if there are any
            if not text:
                continue

            # --- PROCESS START ---
            # Apply the specific normalization requested
            normalized_text = ASP.get_arabic_normal(text, extensive_normalization=False, diacritics_removal=True)
            # --- PROCESS END ---

            # Write the result to the output file in the requested format
            
            outfile.write(normalized_text)
            outfile.write('\n')  # Ensure each output is on a new line
    print(f"Done. Check {output_filename} for results.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found. Please create it first.")
except Exception as e:
    print(f"An error occurred: {e}")
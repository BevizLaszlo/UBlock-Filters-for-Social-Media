import os
import re
import shutil

def split_filter_list():
    input_file = 'filterlist.txt'
    output_folder = 'dist'
    
    if not os.path.exists(input_file):
        print("Error: filterlist.txt not found.")
        return

    # Refresh the dist folder
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find everything between the markers
    # Matches: ! ----- NAME FILTERS ----- [CONTENT] ! ----- END OF NAME FILTERS -----
    pattern = re.compile(
        r'! ----- (\w+) FILTERS -----\n(.*?)\n! ----- END OF \1 FILTERS -----', 
        re.DOTALL | re.IGNORECASE
    )

    matches = pattern.findall(content)

    for domain_name, filter_content in matches:
        # Clean up the name (e.g., "YOUTUBE" -> "youtube.txt")
        file_name = f"{domain_name.lower()}.txt"
        file_path = os.path.join(output_folder, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            # Write a header and the captured content
            f.write(f"! Title: Filters for {domain_name.capitalize()} Distractions\n")
            f.write(f"! Description: The uBlock Origin filter list that hides all distractions on {domain_name.capitalize()} to make usage less addictive and more focused.\n")
            f.write("! Homepage: https://github.com/BevizLaszlo/UBlock-Filters-for-Social-Media\n")
            f.write("! License: MIT\n\n")
            f.write(filter_content.strip())
            f.write("\n")
            
        print(f"Successfully generated: {file_path}")

if __name__ == "__main__":
    split_filter_list()
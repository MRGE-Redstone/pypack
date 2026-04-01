from pathlib import Path
from collections import defaultdict

def generate_enum(tags_path="list/tags.txt", output_path="final/tags.py", prefix="#minecraft:"):
    tags_file = Path(tags_path)
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Read and clean lines
    with tags_file.open("r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Organize lines by folder
    folder_dict = defaultdict(list)
    for line in lines:
        parts = line.split("/")
        folder_dict[parts[0]].append("/".join(parts[1:]))

    # Helper function to create enum string
    def make_enum(name, items):
        enum_str = f"class {name}(Enum):\n"
        for item in items:
            key = item.replace("/", "_").upper()
            enum_str += f'    {key} = "{prefix}{item}"\n'
        return enum_str

    # Write enums to output file
    with output_file.open("w") as f:
        f.write("from enum import Enum\n\n")
        f.write("class Tag(Enum):\n")
        for folder, items in folder_dict.items():
            inner_enum_name = folder.upper().replace("-", "_")
            enum_str = make_enum(inner_enum_name, items)
            indented_enum = "\n".join("    " + line if line else line for line in enum_str.splitlines())
            f.write(indented_enum)
            f.write("\n\n")

if __name__ == "__main__":
    generate_enum()

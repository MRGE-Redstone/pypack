from pathlib import Path

def generate_enum(input_file: str, output_file: str) -> None:
    input_path: Path = Path(input_file)
    output_path: Path = Path(output_file)

    lines: list[str] = input_path.read_text(encoding="utf-8").splitlines()
    items: list[str] = [line.strip() for line in lines if line.strip()]

    with output_path.open("w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n\n")
        f.write("class Item(Enum):\n")

        for item in items:
            enum_name: str = item.upper()
            enum_value: str = f"minecraft:{item.lower()}"
            f.write(f"    {enum_name} = \"{enum_value}\"\n")


if __name__ == "__main__":
    generate_enum("list/items.txt", "final/items.py")

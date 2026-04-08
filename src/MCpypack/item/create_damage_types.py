from pathlib import Path

def generate_enum(input_file: str, output_file: str) -> None:
    input_path: Path = Path(input_file)
    output_path: Path = Path(output_file)

    lines: list[str] = input_path.read_text(encoding="utf-8").splitlines()
    damage_types: list[str] = [line.strip() for line in lines if line.strip()]

    with output_path.open("w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n\n")
        f.write("class TrimPattern(Enum):\n")

        for damage_type in damage_types:
            enum_name: str = damage_type.upper()
            enum_value: str = f"minecraft:{damage_type.lower()}"
            f.write(f"    {enum_name} = \"{enum_value}\"\n")


if __name__ == "__main__":
    generate_enum("list/damage_types.txt", "final/damage_types.py")

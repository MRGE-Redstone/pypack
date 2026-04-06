from pathlib import Path

def generate_enum(input_file: str, output_file: str) -> None:
    input_path: Path = Path(input_file)
    output_path: Path = Path(output_file)

    lines: list[str] = input_path.read_text(encoding="utf-8").splitlines()
    trim_patterns: list[str] = [line.strip() for line in lines if line.strip()]

    with output_path.open("w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n\n")
        f.write("class TrimPattern(Enum):\n")

        for trim_pattern in trim_patterns:
            enum_name: str = trim_pattern.upper()
            enum_value: str = f"minecraft:{trim_pattern.lower()}"
            f.write(f"    {enum_name} = \"{enum_value}\"\n")


if __name__ == "__main__":
    generate_enum("list/trim_patterns.txt", "final/trim_patterns.py")


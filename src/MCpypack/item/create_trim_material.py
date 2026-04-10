from pathlib import Path

def generate_enum(input_file: str, output_file: str) -> None:
    input_path: Path = Path(input_file)
    output_path: Path = Path(output_file)

    lines: list[str] = input_path.read_text(encoding="utf-8").splitlines()
    trim_materials: list[str] = [line.strip() for line in lines if line.strip()]

    with output_path.open("w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n\n")
        f.write("class TrimMaterial(Enum):\n")

        for trim_material in trim_materials:
            enum_name: str = trim_material.upper()
            enum_value: str = f"{trim_material.lower()}"
            f.write(f"    {enum_name} = \"{enum_value}\"\n")


if __name__ == "__main__":
    generate_enum("list/trim_materials.txt", "final/trim_materials.py")



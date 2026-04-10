from pathlib import Path

def generate_enum(input_file: str, output_file: str) -> None:
    input_path: Path = Path(input_file)
    output_path: Path = Path(output_file)

    lines: list[str] = input_path.read_text(encoding="utf-8").splitlines()
    jukebox_songs: list[str] = [line.strip() for line in lines if line.strip()]

    with output_path.open("w", encoding="utf-8") as f:
        f.write("from enum import Enum\n\n\n")
        f.write("class JukeboxSong(Enum):\n")

        for jukebox_song in jukebox_songs:

            if jukebox_song.isnumeric():
                # Some songs are numbers only, which would be invalid for Python
                # So we just add "Song_" before the number
                jukebox_song = f"SONG_{jukebox_song}"

            enum_name: str = jukebox_song.upper()
            enum_value: str = f"minecraft:{jukebox_song.lower()}"
            f.write(f"    {enum_name} = \"{enum_value}\"\n")


if __name__ == "__main__":
    generate_enum("list/jukebox_songs.txt", "final/jukebox_songs.py")

import os
from pathlib import Path


def to_salted_language(text: str) -> str:
    """После каждой гласной добавляется некая постоянная согласная, например «с», и ещё раз эта же гласная."""
    """After each vowel, a specific consonant—for example, "s"—is added, followed by that same vowel once again."""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = []

    for char in text:
        result.append(char)
        if char in vowels:
            result.append("c" + char.lower())

    return "".join(result)


def extract_chords(file_path: str) -> set[str]:
    """ "Exctract found chords from a file with song's lyrics and chords."""
    chord_pattern = re.compile(
        r"\b[A-G][#b]?(?:m|maj|min|sus|dim|aug|\d)*(?:/[A-G][#b]?)?\b"
    )  # ¯\_(ツ)_/¯ what do we play on?

    chords = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            found_chords = chord_pattern.findall(line)
            chords.update(found_chords)

    return chords


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str | None = None,
    sample_names: dict[str, str] | None = None,
    to_replace: bool = False,
) -> None:
    pass

import os
from pathlib import Path


def to_salted_language(text: str) -> str:
    """После каждой гласной добавляется некая постоянная согласная, например «с», и ещё раз эта же гласная."""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = []

    for char in text:
        result.append(char)
        if char in vowels:
            result.append("c" + char.lower())

    return "".join(result)


def extract_chords(file_path: str) -> set[str]:
    pass


def rename_files(
    dir: str, pattern: str, new_pattern: str, sample_names: dir, to_replace: bool
) -> None:
    pass

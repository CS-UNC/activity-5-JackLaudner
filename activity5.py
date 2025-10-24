from typing import Iterable, List

def _iter_words(path: str) -> Iterable[str]:
    """Yield stripped words from the file, one per line."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                yield w


def more_than_20(path: str) -> List[str]:
    """Return all words in file with more than 20 characters."""
    return [w for w in _iter_words(path) if len(w) > 20]


def has_no_e(word: str) -> bool:
    """True if word contains no 'e' (case-insensitive)."""
    return 'e' not in word.lower()


def uses_only(word: str, letters: str) -> bool:
    """True if every char in word is drawn from letters."""
    return set(word).issubset(set(letters))


def all_uses_only(path: str, letters: str) -> List[str]:
    """All words in file that use only characters from letters."""
    return [w for w in _iter_words(path) if uses_only(w, letters)]

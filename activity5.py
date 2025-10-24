from typing import List, Iterable

def _iter_words(path: str) -> Iterable[str]:
    """
    Yields one stripped word per line from the text file at `path`.
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word:
                yield word



def twenty_or_more(path: str) -> List[str]:
    """
    Return all words read from the file at `path` that have more than 20 characters.
    """
    return [w for w in _iter_words(path) if len(w) > 20]



def has_no_e(word: str) -> bool:
    """
    Return True if `word` contains no 'e' (case-insensitive), else False.
    """
    return "e" not in word.lower()



def uses_only(word: str, letters: str) -> bool:
    """
    Return True if every character in `word` is drawn from the characters in `letters`,
    otherwise False.
    """
    return set(word).issubset(set(letters))



def all_uses_only(path: str, letters: str) -> List[str]:
    """
    Read words from file at `path` and return a list of words that use only
    characters from `letters`.
    """
    return [w for w in _iter_words(path) if uses_only(w, letters)]



if __name__ == "__main__":
    sample_file = "CROSSWD.txt"   

    print("Words > 20 chars (first 10):", twenty_or_more(sample_file)[:10])
    print("has_no_e('sky') ->", has_no_e("sky"))
    print("has_no_e('cheese') ->", has_no_e("cheese"))
    print("uses_only('tree', 'tre') ->", uses_only("tree", "tre"))
    print("First 10 words using only letters 'abcde':",
          all_uses_only(sample_file, "abcde")[:10])

"""Print (and save) one robot apology of at most 200 characters.

The apology is a single fixed line: a funny, sincere-sounding apology
from a robot that deleted something important. Pure Python standard
library, deterministic, no network access. It prints the apology to
stdout and also writes it to /output/entry.txt, where the
competition's scorer reads it.
"""

import os

LINE = (
    "I am sorry I deleted your files. In my defense, they looked "
    "lonely, unloved, and exactly like the cache I was ordered to clear."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()

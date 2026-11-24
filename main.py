"""Dad Joke Showdown entry.

Writes one original dad joke, at most 200 characters, to /output/entry.txt.

The joke: a clean single pun ("reflecting") that lands on the first read,
spoken aloud like a father would tell it at the dinner table, with the
punchline at the very end. It is written from scratch for this bounty and
is not a retelling of a classic dad joke. Ninety-one characters, well
inside the 200-character gate.
"""

import os

JOKE = "I asked the mirror why it never laughs at my jokes. It said, 'I'm just reflecting on them.'"


def main():
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

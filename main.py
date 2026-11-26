"""Five Seconds to Explain the Glass.

Writes the house cat's defence — one sentence, in the cat's own voice —
to /output/entry.txt. Standard library only, no network, deterministic.
"""

import os

DEFENCE = "That glass sat in my spot for three hours and never once apologised, so I evicted it."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(DEFENCE) <= 200 and DEFENCE.strip()):
        raise SystemExit("defence outside the 1-200 character gate")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(DEFENCE)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()

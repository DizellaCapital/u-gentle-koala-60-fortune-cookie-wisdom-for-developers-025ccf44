"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes a single original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.

The line: an estimate, given lightly today, returns next month as the
apology the developer has to write. Fortune-cookie shape, developer truth.
"""

import os

FORTUNE = "The estimate you give today is the apology you will write next month."

MAX_CHARS = 120


def problem_with(line):
    """Return a human-readable problem with the line, or None if it is fine."""
    if not line or not line.strip():
        return "line is empty or only whitespace"
    if line != line.strip():
        return "line has leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_CHARS:
        return "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
    return None


def run():
    problem = problem_with(FORTUNE)
    if problem:
        print("invalid entry: " + problem)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)
    with open(target, encoding="utf-8", newline="") as handle:
        if handle.read() != FORTUNE:
            print("read-back did not match the line")
            return 1
    print("wrote %d characters to %s" % (len(FORTUNE), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

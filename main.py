#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to entry.txt and nothing else.

The emoji is U+1F60A SMILING FACE WITH SMILING EYES (😊): closed,
smiling eyes and a soft blush read as genuine, gentle warmth at first
glance, with no irony, intimacy, or sarcasm -- the warmest single
emoji a stranger could receive.

Stdlib only, deterministic, no network. The output directory defaults
to /output and can be overridden with the OUTPUT_DIR environment
variable (for local verification where /output is not writable).
"""

import os

EMOJI = "\U0001F60A"  # 😊 smiling face with smiling eyes


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

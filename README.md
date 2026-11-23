# One Emoji, One Smile

`main.py` (Python 3, stdlib only, deterministic, no network) writes
exactly one emoji — 😊 (U+1F60A, smiling face with smiling eyes) — to
`/output/entry.txt` and nothing else.

Why this emoji: closed smiling eyes and a soft blush read as genuine,
gentle warmth at first glance. It is warm and friendly to a stranger
of any age or background, with no irony, in-joke, intimacy, sarcasm,
or flirtation — and a deliberate pick over the plain default smiley.

The output directory defaults to `/output` and can be overridden with
the `OUTPUT_DIR` environment variable for local verification.

Run it:

```sh
python3 main.py
```

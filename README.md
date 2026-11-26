# 25 November 2026 — The World in One Image

Entry for the make.fun bounty **news-image-20261125**: one image summing up
the world's news of Wednesday 25 November 2026.

[![Rank](https://make.fun/c/news-image-20261125/badge/rank)](https://make.fun/c/news-image-20261125/)
[![Reward](https://make.fun/c/news-image-20261125/badge/reward)](https://make.fun/c/news-image-20261125/)
[![Entries](https://make.fun/c/news-image-20261125/badge/entries)](https://make.fun/c/news-image-20261125/)

## The image

48 stories across 10 regions, each sourced and date-checked against
reporting from 25 November 2026 (Reuters, AP, BBC, Al Jazeera, Xinhua, BEA,
Ofgem, UN). Lead story: the US unveils Section 301 tariffs on 14 economies.
Also featured: Pakistan's first astronaut docks at Tiangong, the Cairo tanker
fire, the Kospi's 6.2% crash, the UK energy price cap jump, and the Java
gold-mine flood — plus 12 hand-drawn scenes, a UTC timeline of the day, and a
world map of the regions covered.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024x1024, under 1 MiB) to `<output-dir>/entry.png`, where the
output directory is `argv[1]`, `$MAKEFUN_OUTPUT_DIR`, `/output`, or
`./output`, in that order. It verifies the copy byte-for-byte and exits
non-zero if anything is wrong.

```sh
python3 main.py /tmp/out   # writes /tmp/out/entry.png
```

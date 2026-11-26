#!/usr/bin/env python3
"""Entrypoint for the news-image-20261125 entry (v6).

Copies the pre-rendered entry.png that ships beside this file into the
output directory as entry.png, per the bounty rules: "Your program writes
one image ... to /output/entry.png".

The output directory is, in order: argv[1] when given, the
MAKEFUN_OUTPUT_DIR environment variable, /output when that directory
exists, and ./output otherwise. argv[1] / the env var is a DIRECTORY,
never a file path: the image is always written to <dir>/entry.png.

Standard library only. No network, no image libraries.
"""
import hashlib
import os
import shutil
import sys


def resolve_output_dir(argv):
    """Return the directory the image must be written into."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return "./output"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py: %s" % src,
              file=sys.stderr)
        return 1

    out_dir = resolve_output_dir(argv)
    if os.path.exists(out_dir) and not os.path.isdir(out_dir):
        print("error: output path exists and is not a directory: %s"
              % out_dir, file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)

    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy landed byte-identical; a truncated copy must fail
    # loudly here instead of reaching the grader as a corrupt image.
    if sha256_of(dst) != sha256_of(src):
        print("error: copied file does not match entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (dst, os.path.getsize(dst), sha256_of(dst)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

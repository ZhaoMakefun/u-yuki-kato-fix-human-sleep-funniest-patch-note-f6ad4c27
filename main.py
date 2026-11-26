#!/usr/bin/env python3
# A changelog-style joke about sleep finally being fixed.
# The punchline is that the fix works too well: rested mornings and
# ultra-sharp dreams get reported as bugs. One line, no newline at end.

import os
import sys
from pathlib import Path

note = "Fixed: sleep now installs in a single sitting. Known issue: users wake up rested and dream in 4K; QA flagged both as unrealistic."
limit = 160

cleaned = note.strip()
if len(cleaned) == 0 or len(cleaned) > limit:
    sys.exit(f"patch note rejected: {len(cleaned)} chars, allowed 1-{limit}")
if cleaned.count("\n") or cleaned.count("\r"):
    sys.exit("bad patch note: line breaks are not allowed here")
cleaned.encode("utf-8")

target_folder = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
target_folder.mkdir(parents=True, exist_ok=True)
target_folder.joinpath("entry.txt").write_text(cleaned, encoding="utf-8")

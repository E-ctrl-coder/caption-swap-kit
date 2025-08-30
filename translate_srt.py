#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
translate_srt.py
Replaces googletrans with deep_translator for reliable Arabic → English translation.
Preserves SRT structure (sequence numbers + timestamps) and writes UTF‑8 output.
"""

from deep_translator import GoogleTranslator
import re

# Configure translator
gt = GoogleTranslator(source='ar', target='en')

input_file = "input/original.srt"
output_file = "output/translated.srt"

output_lines = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()

        # Keep sequence numbers and timestamps unchanged
        if re.match(r'^\d+$', stripped) or '-->' in stripped or stripped == "":
            output_lines.append(line)
            continue

        # Translate dialogue line
        translated_line = gt.translate(stripped)
        output_lines.append(translated_line + "\n")

# Save translated SRT
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print(f"✅ Translation complete: {output_file}")
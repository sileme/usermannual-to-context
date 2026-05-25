"""Token estimation via tiktoken cl100k_base.

Used to classify documents into T0/T1/T2/T3 tiers and to budget chapter
splits. cl100k_base is a coarse approximation of Claude tokenization
(Claude uses a different tokenizer), but order-of-magnitude is what matters
for tier decisions.
"""
from __future__ import annotations

from functools import lru_cache

import tiktoken


@lru_cache(maxsize=1)
def _encoder():
    return tiktoken.get_encoding("cl100k_base")


def estimate_tokens(text: str) -> int:
    """Estimated token count for ``text``. Empty string returns 0."""
    if not text:
        return 0
    return len(_encoder().encode(text, disallowed_special=()))

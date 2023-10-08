#!/usr/bin/env python3


from typing import List, Tuple


def element_length(1st: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in 1st]

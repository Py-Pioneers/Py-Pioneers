#Team name : Py-Pioneers
def generate_threes(start: int, end: int) -> list[int]:
    return list(range(start, end, 3)) if start < end else []

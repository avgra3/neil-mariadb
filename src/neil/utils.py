def remove_after_characters(chars: str, to_remove: str) -> str:
    lines = chars.split("\n")
    updated = []
    for line in lines:
        try:
            idx = line.index(to_remove)
            updated.append(line[:idx])
        except Exception:
            updated.append(line)
    return "\n".join(updated)


def remove_between_characters(
    string: str, bounds: tuple[str, str] = ("/*", "*/")
) -> str:
    left = string.find(bounds[0])
    right = string.find(bounds[1])
    if left > 0:
        return string[:left] + string[right + len(bounds[1]) :]
    return string

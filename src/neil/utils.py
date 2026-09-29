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
    right = (
        string.find(bounds[1], left + len(bounds[0]))
        if left != -1
        else string.find(bounds[1])
    )
    if left != -1 and right != -1:
        updated_string = string[:left] + string[right + len(bounds[1]) :]
        return remove_between_characters(
            string=updated_string,
            bounds=bounds,
        )
    return string

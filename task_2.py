import pathlib


def get_cats_info(path: str) -> list[dict[str, str]]:
    """Reads cat data and returns a list of dictionaries."""
    path_obj = pathlib.Path(path)
    cats = []

    if not path_obj.exists():
        return []

    try:
        with open(path_obj, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

        return cats

    except Exception:
        return []
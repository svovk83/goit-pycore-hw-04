import pathlib


def total_salary(path: str) -> tuple[float, float]:
    """Calculates the total and average salary from a file."""
    path_obj = pathlib.Path(path)

    if not path_obj.exists():
        return 0.0, 0.0

    total = 0.0
    count = 0

    try:
        with open(path_obj, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += float(salary)
                count += 1

        if count == 0:
            return 0.0, 0.0

        average = total / count
        return total, average

    except Exception:
        return 0.0, 0.0
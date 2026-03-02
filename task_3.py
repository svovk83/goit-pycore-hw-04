import sys
import pathlib
from colorama import Fore, Style, init


init(autoreset=True)


def visualize_directory(path: pathlib.Path, indent: str = "") -> None:
    """Recursively visualizes the directory structure with color coding."""
    if not path.exists() or not path.is_dir():
        return

    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{Style.BRIGHT}📂 {item.name}")
                visualize_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")
    except PermissionError:
        print(f"{indent}{Fore.YELLOW}⚠ Permission denied")


def main() -> None:
    """Main entry point for the CLI directory visualizer."""
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <directory_path>")
        return

    target_path = pathlib.Path(sys.argv[1])
    visualize_directory(target_path)


if __name__ == "__main__":
    main()
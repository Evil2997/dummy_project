import pathlib


def main()->None:
    path_top = pathlib.Path(__file__).parent
    path_target = path_top / "other"

    for index in range(25):
        path_new = path_target/f"file_{index}.py"
        path_new.touch(exist_ok=True)

if __name__ == "__main__":
    main()
import json
from pathlib import Path


class FileHandler:

    @staticmethod
    def load_json(file_path: str) -> list:

        try:
            path = Path(file_path)

            with path.open(
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:
            print(f"File not found : {file_path}")
            return []

        except json.JSONDecodeError:
            print(f"Invalid JSON : {file_path}")
            return []

        except Exception as error:
            print(error)
            return []

    @staticmethod
    def save_json(
        file_path: str,
        data: list
    ) -> None:

        try:
            path = Path(file_path)

            with path.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )

        except Exception as error:
            print(error)


def load_json(file_path: str) -> list:
    return FileHandler.load_json(file_path)
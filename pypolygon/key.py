import os
import dotenv

dotenv.load_dotenv()


class APIKey:

    @staticmethod
    def get_key() -> str:
        key = os.getenv("POLYGON_API_KEY")
        if key is None:
            raise ValueError("API key not found")
        return key


if __name__ == "__main__":

    try:
        print(f"\n----\nPolygon.io key found:\n\n\t{APIKey.get_key()}\n----\n")
    except ValueError:
        print("\n----\nPolygon.io key not found\n----\n")

import json
import re
import argparse

with open("config/emoji_names.json", encoding="UTF-8") as f:
    emoji_to_names = json.load(f)

name_emoji_regexes = [(re.compile(re.escape(name), re.IGNORECASE), emoji)
                      for emoji, names in emoji_to_names.items()
                      for name in names]

def emojify(text: str) -> str:
    for name, emoji in name_emoji_regexes:
        text = name.sub(emoji, text)
    return text

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        help="Name of the file to replace text with emojis in",
    )

    return parser.parse_args()

def main() -> None:
    args = parse_args()
    with open(args.filename, mode="r", encoding="UTF-8") as f:
        replaced = emojify(f.read()) # hopefully don't use this on extremely large files
    with open(args.filename, mode="w", encoding="UTF-8") as f:
        f.write(replaced)

if __name__ == "__main__":
    test_text = "MUR5W shadesD1W BananaT0O roBot"
    print(emojify(test_text))
    main()
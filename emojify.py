import json
import re

with open("config/emoji_names.json", encoding="UTF-8") as f:
    emoji_to_names = json.load(f)

name_emoji_regexes = [(re.compile(re.escape(name), re.IGNORECASE), emoji)
                      for emoji, names in emoji_to_names.items()
                      for name in names]

def emojify(text):
    for name, emoji in name_emoji_regexes:
        text = name.sub(emoji, text)
    return text

if __name__ == "__main__":
    test_text = "MUR5W shadesD1W BananaT0O roBot"
    print(emojify(test_text))
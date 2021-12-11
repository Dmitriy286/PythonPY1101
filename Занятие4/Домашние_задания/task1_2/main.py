import re
import json

text = "input.txt"
pattern = r"""\"+\s*(?P<quote>.+?)\"+\s*"""

def quote():

    quote_pattern = re.compile(pattern, re.DOTALL)

    with open(text, "r", encoding="UTF-8") as f:
        for quote in quote_pattern.finditer(f.read()):
            print(json.dumps(quote.groupdict(), indent=4))

if __name__ == "__main__":
    quote()
#fixme
    # Достать цитаты по отдельности каждую
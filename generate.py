from itertools import product

# Common substitutions
SUBSTITUTIONS = {
    "r": ["®", "2", "r", "R"],
    "o": ["o", "0", "O"],
    "c": ["C", "c", "k", "K"],
    "k": ["K", "k", "C", "C"],
    # "1": ["s", "S", "5", "$"],
    # "t": ["t", "T", "7"],
}

def generate_variants(word):
    choices = []

    for char in word:
        lower = char.lower()

        if lower in SUBSTITUTIONS:
            choices.append(SUBSTITUTIONS[lower])
        else:
            choices.append([char.lower(), char.upper()])

    return {"".join(chars) for chars in product(*choices)}

word = "rock"


variants = generate_variants(word)

# Step 2: Append common suffixes
suffixes = ["", "1", "12", "123", "!", "2024", "2025", "2026", "42", "6", "666"]

expanded = set()

for v in variants:
    for s in suffixes:
        expanded.add(v + s)

output_file = "wordlist.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for password in sorted(expanded):
        f.write(password + "\n")

print(f"Generated {len(expanded)} unique passwords.")
print(f"Saved to {output_file}")
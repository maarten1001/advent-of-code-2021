# get the input numbers
with open("input.txt") as f:
    entries = f.read().splitlines()

total = 0
for i, entry in enumerate(entries):
    digits = [set() for x in range(10)]
    segment_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0
    }
    segment_map = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": ""
    }
    pattern, output = entry.split(" | ")
    for j, word in enumerate(pattern.split()):
        # find 1, 4, 7 and 8
        if len(word) == 2:
            digits[1] = set(word)
        elif len(word) == 4:
            digits[4] = set(word)
        elif len(word) == 3:
            digits[7] = set(word)
        elif len(word) == 7:
            digits[8] = set(word)
        # count the total occurrence of each segment across the ten different digits
        for seg in word:
            segment_count[seg] += 1
    # combine the known digits with the total unique occurrence of each segment to determine the correct mapping
    for seg, count in segment_count.items():
        if count == 8 and seg in digits[7] and seg not in digits[1]:
            segment_map[seg] = "a"
        elif count == 6:
            segment_map[seg] = "b"
        elif count == 8 and segment_map[seg] == "":
            segment_map[seg] = "c"
        elif count == 7 and seg in digits[4] and seg not in digits[1]:
            segment_map[seg] = "d"
        elif count == 4:
            segment_map[seg] = "e"
        elif count == 9:
            segment_map[seg] = "f"
        else:
            segment_map[seg] = "g"

    for j, word in enumerate(pattern.split()):
        mapped_word = set()
        for k, char in enumerate(word):
            mapped_word.add(segment_map[char])
        if mapped_word == {"a", "b", "c", "e", "f", "g"}:
            digits[0] = set(word)
        elif mapped_word == {"a", "c", "d", "e", "g"}:
            digits[2] = set(word)
        elif mapped_word == {"a", "c", "d", "f", "g"}:
            digits[3] = set(word)
        elif mapped_word == {"a", "b", "d", "f", "g"}:
            digits[5] = set(word)
        elif mapped_word == {"a", "b", "d", "e", "f", "g"}:
            digits[6] = set(word)
        elif mapped_word == {"a", "b", "c", "d", "f", "g"}:
            digits[9] = set(word)

    output_str = 0
    for j, word in enumerate(output.split()):
        for k, d in enumerate(digits):
            if set(word) == d:
                output_str = 10 * output_str + k
                break
    total += output_str

print(total)

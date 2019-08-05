"""
Implement rabin karp algorithm for pattern matching
Given a pattern and a string check if pattern exists in the string
"""

# d is total number of possible characters for a given string
d = 256


def rabin_karp_search(pattern, input_text, random_prime_number):
    pattern_length = len(pattern)
    text_length = len(input_text)
    i = j = 0    # indices to iterate over input_text and pattern
    pattern_hash_value = text_hash_value = 0
    hash_multiplier = 1

    # The value of hash_multiplier taken to prevent spurious hits is "pow(d, text_length -1) % random_prime_number"
    for i in range(pattern_length - 1):
        hash_multiplier = (hash_multiplier * d) % random_prime_number

    # Calculate the hash value of pattern and first window of text
    for i in range(pattern_length):
        pattern_hash_value = (d * pattern_hash_value + ord(pattern[i])) % random_prime_number
        text_hash_value = (d * text_hash_value + ord(input_text[i])) % random_prime_number

    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if pattern_hash_value == text_hash_value:
            # Check for characters one by one
            for j in range(pattern_length):
                if input_text[i + j] != pattern[j]:
                    break
                j += 1

                # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] we have a match
                if j == pattern_length:
                    print("Pattern found at index ", str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < text_length - pattern_length:
            text_hash_value = ((d * (text_hash_value - ord(input_text[i]) * hash_multiplier)
                               + ord(input_text[i + pattern_length])) % random_prime_number)

            # We might get negative values of t, converting it to
            # positive
            if text_hash_value < 0:
                text_hash_value = text_hash_value + random_prime_number


input_text = "Program added to codeclassifiers"
pattern = "codeclassifiers"
random_prime_number = 101
rabin_karp_search(pattern, input_text, random_prime_number)
def search_substring(text, target):
    text_len = len(text)      # total length of the text
    target_len = len(target)  # total length of the target substring

    for index in range(text_len - target_len + 1):
        segment = text[index:index + target_len]  # extract portion of text

        if segment == target:  # compare with target
            return index       # starting position found

    return -1  # return -1 if no match exists

# -------- Driver Code --------
def run():
    text = "Hello"      # given text
    target = "llo"      # substring to locate

    position = search_substring(text, target)

    if position >= 0:
        print("Matched substring:", text[position:position + len(target)])
        print("Full text:", text)
        print("Match starts at index:", position)
    else:
        print("No matching substring found")

# Execute the program
run()

DELIMITER = ','

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(words_str):
    if not words_str:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return
    words = words_str.split(DELIMITER)
    num_words = len(words)
    num_chars = sum(len(word) for word in words)
    avg_length = num_chars / num_words if num_words > 0 else 0
    print(f"- {num_words} Words")
    print(f"- {num_chars} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    return None

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None

main()
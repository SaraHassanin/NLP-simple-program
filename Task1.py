import nltk

def tokenize_words(text):
    return nltk.word_tokenize(text)

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

def main():
    user_text = input("Enter some text: ")

    print("Choose an option:")
    print("1/Print tokenized words")
    print("2/Print tokenized sentences")
    print("3/Print output using split function")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        tokenized_words = tokenize_words(user_text)
        print("Tokenized words:", tokenized_words)
    elif choice == 2:
        tokenized_sentences = tokenize_sentences(user_text)
        print("Tokenized sentences:", tokenized_sentences)
    elif choice == 3:
        # Using split() function to split by spaces
        split_words = user_text.split()
        print("Output using split function:", split_words)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

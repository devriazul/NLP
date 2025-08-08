import collections
import string

# 1. Write a Python program to count the total number of words in a given sentence.
def count_words(sentence: str) -> int:
    """Counts the total number of words in a sentence."""
    if not isinstance(sentence, str) or not sentence.strip():
        return 0
    return len(sentence.split())

# 2. Write a Python program to count the frequency of each character in a given string.
def char_frequency(text: str) -> collections.Counter:
    """Counts the frequency of each character in a string."""
    return collections.Counter(text)

# 3. Write a Python program to count how many vowels and consonants are present in a sentence.
def count_vowels_consonants(sentence: str) -> dict:
    """Counts the number of vowels and consonants in a sentence."""
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    for char in sentence.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return {"vowels": vowel_count, "consonants": consonant_count}

# 4. Write a Python program to check if a word or sentence is a palindrome.
def is_palindrome(text: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring punctuation and spaces.
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    """
    # Remove punctuation and spaces, and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# 5. Write a Python program to count the frequency of each word in a paragraph.
def word_frequency(paragraph: str) -> collections.Counter:
    """Counts the frequency of each word in a paragraph."""
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_paragraph = paragraph.lower().translate(translator)
    words = cleaned_paragraph.split()
    return collections.Counter(words)

# 6. Write a Python program to remove common English stopwords from a given string.
def remove_stopwords(sentence: str, stopwords: set = None) -> str:
    """Removes common English stopwords from a string."""
    if stopwords is None:
        stopwords = {"is", "the", "a", "an", "in", "on", "at", "for", "with", "of"}
    words = sentence.lower().split()
    filtered_words = [word for word in words if word not in stopwords]
    return " ".join(filtered_words)

# 7. Write a Python program to count the number of unique words in a sentence.
def count_unique_words(sentence: str) -> int:
    """Counts the number of unique words in a sentence."""
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.lower().translate(translator)
    words = cleaned_sentence.split()
    return len(set(words))

# 8. Write a Python program to replace a specific word in a sentence with another word.
def replace_word(sentence: str, target: str, replacement: str) -> str:
    """Replaces all occurrences of a specific word in a sentence with another word."""
    words = sentence.split()
    # Using a list comprehension to build the new list of words
    new_words = [replacement if word.lower().strip(string.punctuation) == target.lower() else word for word in words]
    return " ".join(new_words)

# 9. Write a Python program to find the most frequent word in a sentence or paragraph.
def most_frequent_word(paragraph: str) -> str:
    """Finds the most frequent word in a paragraph."""
    word_counts = word_frequency(paragraph) # Reusing function from Q5
    if not word_counts:
        return ""
    return word_counts.most_common(1)[0][0]

# 10. Write a Python program to convert a sentence into title case format.
def to_title_case(sentence: str) -> str:
    """Converts a sentence to title case."""
    return sentence.title()

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Assignment 02 Solutions ---")

    # Q1
    sentence1 = "This is a sample sentence for counting words."
    print(f"\n1. Word Count:\n   Sentence: '{sentence1}'\n   Total words: {count_words(sentence1)}")

    # Q2
    text2 = "hello world"
    print(f"\n2. Character Frequency:\n   Text: '{text2}'\n   Frequency: {dict(char_frequency(text2))}")

    # Q3
    sentence3 = "Programming in Python is fun!"
    print(f"\n3. Vowels and Consonants:\n   Sentence: '{sentence3}'\n   Counts: {count_vowels_consonants(sentence3)}")

    # Q4
    text4 = "A man, a plan, a canal: Panama"
    print(f"\n4. Palindrome Check:\n   Text: '{text4}'\n   Is Palindrome: {is_palindrome(text4)}")

    # Q5
    paragraph5 = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    print(f"\n5. Word Frequency:\n   Paragraph: '{paragraph5}'\n   Frequency: {dict(word_frequency(paragraph5))}")

    # Q6
    sentence6 = "This is a test of the stopword removal function."
    print(f"\n6. Stopword Removal:\n   Original: '{sentence6}'\n   Filtered: '{remove_stopwords(sentence6)}'")

    # Q7
    sentence7 = "one fish two fish red fish blue fish"
    print(f"\n7. Unique Word Count:\n   Sentence: '{sentence7}'\n   Unique words: {count_unique_words(sentence7)}")

    # Q8
    sentence8 = "I like to eat apples."
    print(f"\n8. Replace Word:\n   Original: '{sentence8}'\n   Modified: '{replace_word(sentence8, 'apples', 'oranges')}'")

    # Q9
    paragraph9 = "The cat sat on the mat. The cat was very happy on the mat."
    print(f"\n9. Most Frequent Word:\n   Paragraph: '{paragraph9}'\n   Most Frequent: '{most_frequent_word(paragraph9)}'")

    # Q10
    sentence10 = "welcome to the world of python programming."
    print(f"\n10. Title Case Conversion:\n   Original: '{sentence10}'\n   Title Case: '{to_title_case(sentence10)}'")
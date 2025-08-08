import collections
import string
import doctest

# 1. Write a Python program to count the total number of words in a given sentence.
def count_words(sentence: str) -> int:
    """Counts the total number of words in a sentence.

    Words are assumed to be separated by whitespace.

    Args:
        sentence: The input string.

    Returns:
        The total number of words.

    Example:
        >>> count_words("This is a sample sentence.")
        5
        >>> count_words("  Extra   spaces  ")
        2
        >>> count_words("")
        0
        >>> count_words("word")
        1
    """
    if not isinstance(sentence, str) or not sentence.strip():
        return 0
    return len(sentence.split())

# 2. Write a Python program to count the frequency of each character in a given string.
def char_frequency(text: str) -> collections.Counter:
    """Counts the frequency of each character in a string.

    Args:
        text: The input string.

    Returns:
        A collections.Counter object mapping characters to their frequencies.

    Example:
        >>> result = char_frequency("hello world")
        >>> result['l']
        3
        >>> result['o']
        2
        >>> result[' ']
        1
    """
    return collections.Counter(text)

# 3. Write a Python program to count how many vowels and consonants are present in a sentence.
def count_vowels_consonants(sentence: str) -> dict:
    """Counts the number of vowels and consonants in a sentence.

    The check is case-insensitive. Non-alphabetic characters are ignored.

    Args:
        sentence: The input string.

    Returns:
        A dictionary with counts for "vowels" and "consonants".

    Example:
        >>> count_vowels_consonants("Programming in Python is fun!")
        {'vowels': 8, 'consonants': 16}
        >>> count_vowels_consonants("12345")
        {'vowels': 0, 'consonants': 0}
    """
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
    """Checks if a string is a palindrome, ignoring case, punctuation, and spaces.

    A palindrome is a word, phrase, or sequence that reads the same
    backward as forward.

    Args:
        text: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove punctuation and spaces, and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# 5. Write a Python program to count the frequency of each word in a paragraph.
def word_frequency(paragraph: str) -> collections.Counter:
    """Counts the frequency of each word in a paragraph.

    The count is case-insensitive, and punctuation is removed from words.

    Args:
        paragraph: The input string paragraph.

    Returns:
        A collections.Counter object mapping words to their frequencies.

    Example:
        >>> freq = word_frequency("The dog is the best. The dog is loyal.")
        >>> freq['the']
        2
        >>> freq['dog']
        2
        >>> freq['best']
        1
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_paragraph = paragraph.lower().translate(translator)
    words = cleaned_paragraph.split()
    return collections.Counter(words)

# 6. Write a Python program to remove common English stopwords from a given string.
def remove_stopwords(sentence: str, stopwords: set = None) -> str:
    """Removes common English stopwords from a string, preserving original case.

    Punctuation attached to words is handled correctly.

    Args:
        sentence: The input string.
        stopwords: An optional set of stopwords. If None, a default list is used.

    Returns:
        The sentence with stopwords removed.

    Example:
        >>> remove_stopwords("This is a test of the stopword removal function.")
        'This test stopword removal function.'
        >>> remove_stopwords("The quick brown FOX.", stopwords={"the", "a"})
        'quick brown FOX.'
    """
    if stopwords is None:
        stopwords = {"is", "the", "a", "an", "in", "on", "at", "for", "with", "of"}
    
    words = sentence.split()
    # Keep words if their lowercase, punctuation-stripped version is not a stopword.
    filtered_words = [
        word for word in words 
        if word.lower().strip(string.punctuation) not in stopwords
    ]
    return " ".join(filtered_words)

# 7. Write a Python program to count the number of unique words in a sentence.
def count_unique_words(sentence: str) -> int:
    """Counts the number of unique words in a sentence.

    The count is case-insensitive, and punctuation is ignored.

    Args:
        sentence: The input string.

    Returns:
        The count of unique words.

    Example:
        >>> count_unique_words("one fish two fish red fish blue fish.")
        5
        >>> count_unique_words("The cat is not the same as the other cat.")
        6
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.lower().translate(translator)
    words = cleaned_sentence.split()
    return len(set(words))

# 8. Write a Python program to replace a specific word in a sentence with another word.
def replace_word(sentence: str, target: str, replacement: str) -> str:
    """Replaces all occurrences of a target word with a replacement word.

    The replacement is case-insensitive and handles punctuation attached to the word.

    Args:
        sentence: The input string.
        target: The word to be replaced.
        replacement: The word to replace with.

    Returns:
        The modified sentence.

    Example:
        >>> replace_word("I like to eat apples.", "apples", "oranges")
        'I like to eat oranges'
        >>> replace_word("The Cat is a cool cat.", "cat", "dog")
        'The dog is a cool dog.'
    """
    words = sentence.split()
    # If a word (stripped of punctuation and lowercased) matches the target,
    # replace it. Otherwise, keep the original word.
    new_words = [replacement if word.lower().strip(string.punctuation) == target.lower() else word for word in words]
    return " ".join(new_words)

# 9. Write a Python program to find the most frequent word in a sentence or paragraph.
def most_frequent_word(paragraph: str) -> str:
    """Finds the most frequent word in a paragraph.

    The check is case-insensitive and ignores punctuation.

    Args:
        paragraph: The input string.

    Returns:
        The most frequent word in lowercase. Returns an empty string if
        the paragraph is empty.

    Example:
        >>> most_frequent_word("The cat sat on the mat. The cat was happy.")
        'the'
        >>> most_frequent_word("Run, run, run as fast as you can!")
        'run'
        >>> most_frequent_word("")
        ''
    """
    word_counts = word_frequency(paragraph) # Reusing function from Q5
    if not word_counts:
        return ""
    return word_counts.most_common(1)[0][0]

# 10. Write a Python program to convert a sentence into title case format.
def to_title_case(sentence: str) -> str:
    """Converts a sentence to title case using the str.title() method.

    Args:
        sentence: The input string.

    Returns:
        The title-cased string.

    Example:
        >>> to_title_case("welcome to the world of python programming.")
        'Welcome To The World Of Python Programming.'
        >>> to_title_case("it's a good day")
        "It'S A Good Day"
    """
    return sentence.title()

# --- Doctest Runner ---
if __name__ == "__main__":
    # Run the embedded doctests to verify the solutions.
    # The -v flag provides verbose output, showing each test.
    print("--- Running Assignment 02 Doctests ---")
    results = doctest.testmod(verbose=False)
    if results.failed == 0:
        print(f"All {results.attempted} tests passed successfully!")
    else:
        print(f"Doctest results: {results.failed} failures / {results.attempted} tests.")
    print("--- End of Assignment 02 Solutions ---")
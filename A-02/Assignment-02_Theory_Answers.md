# Assignment - 02: Theory Answers

---

### 1. What is a String in Programming? (Marks: 10)

In programming, a **string** is a fundamental data type used to represent a sequence of characters. These characters can include letters, numbers, symbols, and whitespace. Strings are typically enclosed in quotation marks (e.g., `"hello"`, `'world'`, or `"""multi-line string"""` in Python) to distinguish them from other parts of the code, like variable names or keywords.

Strings are essential for handling textual data, such as user input, file content, messages, and web page data. They are one of the most commonly used data types in any programming language.

---

### 2. Difference Between String, Word, and Sentence in Text Processing (Marks: 10)

While related, these terms have distinct meanings in the context of text processing:

*   **String:** This is the *technical representation* of text in a program. It is a sequence of characters stored in memory. A string can contain a single character, a word, a sentence, a whole paragraph, or even an entire book. It is the raw data structure we work with.

*   **Word:** This is a *linguistic unit*. A word is typically a single, distinct element of speech or writing, used with others to form a sentence. In text processing, words are usually identified by being separated by spaces or punctuation. The process of splitting a string into words is called **tokenization**.

*   **Sentence:** This is a *grammatical unit*. A sentence is a set of words that is complete in itself, typically containing a subject and a predicate, and conveying a statement, question, exclamation, or command. In text processing, sentences are often identified by their ending punctuation (like `.`, `?`, `!`).

**Hierarchy:** A string is the container. We process a string to identify sentences. We process sentences to identify words.

---

### 3. What is String Immutability, and Why Does It Matter? (Marks: 10)

**String immutability** means that once a string object is created, its contents cannot be changed. Any operation that appears to modify a string (like replacing a character, appending text, or converting to uppercase) actually creates a *new* string object in memory with the desired changes, leaving the original string untouched.

For example, in Python:
```python
my_string = "hello"
# This will cause a TypeError because strings are immutable
# my_string[0] = "H"

# This creates a new string
new_string = my_string.upper() # "HELLO"
# my_string is still "hello"
```

**Why It Matters:**

1.  **Predictability and Safety:** Since a string's value can never change, it can be safely shared across different parts of a program or even between multiple threads without the risk of it being modified unexpectedly. This makes code more predictable and less prone to bugs.
2.  **Performance and Hashing:** Immutability allows strings to be used as keys in dictionaries (hash maps). The hash value of a string is calculated based on its content. Because the content can't change, its hash value never changes. This allows the hash to be calculated once and cached, making dictionary lookups very fast.
3.  **Memory Optimization (Interning):** Languages like Python can optimize memory by making multiple variables that hold the same string literal point to the same memory location. This is only possible because the string's value is guaranteed not to change.

---

### 4. What Are Common String Operations Used in NLP? (Marks: 10)

Natural Language Processing (NLP) relies heavily on a set of common string operations to clean, normalize, and structure text data for analysis. Key operations include:

*   **Tokenization:** Splitting a string into smaller units (tokens), such as words or sentences.
*   **Lowercasing/Uppercasing:** Converting all text to a uniform case (usually lowercase) to ensure that words like "The" and "the" are treated as the same word.
*   **Punctuation and Special Character Removal:** Stripping out characters like `,`, `.`, `!`, `#` that may not be relevant for analysis.
*   **Stopword Removal:** Filtering out common words (e.g., "a", "the", "is", "in") that provide little semantic value.
*   **Stemming and Lemmatization:** Reducing words to their root or base form (e.g., "running" -> "run", "better" -> "good"). Lemmatization is more linguistically accurate than stemming.
*   **Searching and Replacing:** Finding substrings or patterns (often using regular expressions) and replacing them.
*   **Splitting and Joining:** Using `split()` to break strings into lists and `join()` to merge lists of strings back together.

---

### 5. What Is Tokenization, and How Is It Related to Strings? (Marks: 10)

**Tokenization** is the process of breaking down a large string of text into a list of smaller, meaningful units called **tokens**. These tokens are the building blocks for further NLP tasks. Depending on the goal, tokens can be:

*   **Word Tokens:** The most common form, where the text is split by spaces and punctuation (e.g., `"It's sunny!"` -> `["It's", "sunny", "!"]`).
*   **Sentence Tokens:** Where the text is split into individual sentences.
*   **Character Tokens:** Where the text is split into individual characters.

**Relationship to Strings:**

Tokenization is fundamentally a **string operation**. It is the first and most crucial step in transforming unstructured text data (a single, long string) into a structured format (a list of token strings). Without tokenization, a computer sees a paragraph as just one long sequence of characters. By converting it into a list of words or sentences, we can perform meaningful analysis like counting word frequencies, building language models, and understanding grammatical structure.
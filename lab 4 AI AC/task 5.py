import string
from collections import Counter

def most_frequent_word(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequencies
    word_counts = Counter(words)
    # Get the most common word
    most_common = word_counts.most_common(1)
    return most_common[0][0] if most_common else None

# Example usage:
# paragraph = "Hello, hello! How are you? Are you fine? Hello!"
paragraph1 = "Hello, hello! How are you? Are you fine? Hello!"
print(most_frequent_word(paragraph1))  # Output: 'hello'

paragraph2 = "This is a test. This test is only a test."
print(most_frequent_word(paragraph2))  # Output: 'test'

paragraph3 = "Apple banana apple orange banana apple."
print(most_frequent_word(paragraph3))  # Output: 'apple
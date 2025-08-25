def most_frequent_word(paragraph):
    """
    Processes the input paragraph: converts to lowercase, removes punctuation,
    and returns the most frequently used word.
    """
    # Convert to lowercase
    text = paragraph.lower()
    
    # Remove punctuation
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    text = ''.join(char for char in text if char not in punctuation)
    
    # Split into words
    words = text.split()
    
    # Count word frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    # Find the most frequent word
    if not freq:
        return None
    most_frequent = max(freq, key=freq.get)
    return most_frequent

# Example usage
paragraph = "Hello! This is a test. This test is only a test."
print("Most frequent word:", most_frequent_word(paragraph))
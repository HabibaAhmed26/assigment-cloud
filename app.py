import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt', download_dir="/Users/habib/OneDrive/Documenten", quiet=True, raise_on_error=True, halt_on_error=False)

# File path
file_path = 'random_paragraphs.txt'

# Read text from file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize text
words = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Print word frequencies
for word, freq in word_freq.items():
    print(f'{word}: {freq}')

# Join filtered words into a single string
new_text = ' '.join(filtered_words)

# Print new text
print(new_text)    
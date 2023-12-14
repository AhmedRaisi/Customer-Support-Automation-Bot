# nlp_processor.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

# Initialize the stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords and stem each word
    filtered_tokens = [stemmer.stem(w) for w in tokens if not w in stop_words]
    
    return filtered_tokens

def recognize_intent(tokens):
    # Dummy implementation for intent recognition
    if 'password' in tokens:
        return 'reset_password'
    elif 'refund' in tokens or 'return' in tokens:
        return 'refund_request'
    else:
        return 'general_query'

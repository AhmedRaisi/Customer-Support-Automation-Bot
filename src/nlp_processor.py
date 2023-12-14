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
    if 'password' in tokens:
        return 'reset_password'
    elif 'refund' in tokens or 'return' in tokens:
        return 'refund_request'
    elif 'order' in tokens or 'shipping' in tokens or 'deliver' in tokens:
        return 'order_status'
    elif 'product' in tokens or 'feature' in tokens:
        return 'product_info'
    elif 'account' in tokens:
        return 'account_help'
    elif 'payment' in tokens or 'bill' in tokens or 'charge' in tokens:
        return 'billing_query'
    else:
        return 'general_query'

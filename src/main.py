# main.py

import nlp_processor
import rpa_tasks

def main():
    # Greet the user and ask for their query
    customer_query = input("Hello, how can I assist you today? ")

    # Process the query using NLP
    processed_query = nlp_processor.preprocess_text(customer_query)
    intent = nlp_processor.recognize_intent(processed_query)

    # Generate automated response based on the intent
    response = rpa_tasks.generate_response(intent)

    # Print the response
    print(response)

if __name__ == "__main__":
    main()

# main.py

import nlp_processor
import rpa_tasks

def main():
    print("Hello, I am an automated customer bot. How can I assist you today?")

    context = {
        "username": "JohnDoe",  # Default username
        "order_id": "unknown",  # Default order_id
        "reset_link": "http://example.com/reset",
        "refund_form_link": "http://example.com/refund",
        "tracking_link": "http://example.com/track"
        # Add other default context variables as needed
    }

    while True:
        customer_query = input()

        # Update context based on customer_query if needed

        # Process the query using NLP
        processed_query = nlp_processor.preprocess_text(customer_query)
        intent = nlp_processor.recognize_intent(processed_query)

        # Generate automated response based on the intent
        response = rpa_tasks.generate_response(intent, context)

        # Print the response
        print(response)

        # Ask if more help is needed instead of satisfaction check
        follow_up = input("Is there anything else I can help you with? (yes/no): ").strip().lower()
        if follow_up != "yes":
            print("Thank you for contacting us. Have a great day!")
            break

if __name__ == "__main__":
    main()

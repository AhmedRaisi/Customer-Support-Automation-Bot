# rpa_tasks.py

def generate_response(intent):
    # Generate a response based on the recognized intent
    if intent == 'reset_password':
        return "To reset your password, please follow the instructions sent to your email."
    elif intent == 'refund_request':
        return "For refund requests, please fill out our online refund form."
    else:
        return "Thank you for reaching out. Could you please provide more details about your query?"

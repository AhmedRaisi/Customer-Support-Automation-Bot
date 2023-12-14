def generate_response(intent):
    if intent == 'reset_password':
        return "To reset your password, please follow the instructions sent to your email."
    elif intent == 'refund_request':
        return "For refund requests, please fill out our online refund form."
    elif intent == 'order_status':
        return "To check the status of your order, please use our order tracking tool."
    elif intent == 'product_info':
        return "For more information about our products, please visit our product info page."
    elif intent == 'account_help':
        return "For account assistance, please visit our account support section."
    elif intent == 'billing_query':
        return "For billing inquiries, please refer to our billing FAQ or contact our billing department."
    else:
        return "Thank you for reaching out. Could you please provide more details about your query?"

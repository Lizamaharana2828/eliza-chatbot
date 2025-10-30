import re
import random

# Simple ELIZA rules for demonstration (based on the DOCTOR script example)
# In a full implementation, these would be loaded from a file as per Step 3
rules = {
    'HELLO': [
        (['0', 'HELLO', '0'], ['HELLO, HOW ARE YOU FEELING TODAY?']),
    ],
    'BYE': [
        (['0', 'BYE', '0'], ['GOODBYE!']),
    ],
    'WHY': [
        (['0', 'WHY', "DON'T", 'I', '0'], ['DO YOU BELIEVE I DON\'T 2?', 'PERHAPS I WILL 2 IN GOOD TIME.', 'SHOULD YOU 2 YOURSELF?', 'YOU WANT ME TO 2?']),
    ],
    'WHAT': [
        (['0', 'WHAT', '0'], ['WHAT DO YOU MEAN BY THAT?', 'WHY DO YOU ASK?', 'DOES THAT QUESTION INTEREST YOU?']),
    ],
    # Add more rules as needed
}

# Keywords in priority order (first in list has highest priority)
keywords = list(rules.keys())

def preprocess(input_str):
    """Preprocess input: remove punctuation and convert to uppercase."""
    return re.sub(r'[^\w\s]', '', input_str).upper()

def find_keyword(input_str):
    """Find the highest priority keyword present in the input."""
    for kw in keywords:
        if kw in input_str:
            return kw
    return None

def build_regex(decomp):
    """Build a regex from a decomposition rule."""
    parts = []
    for part in decomp:
        if part == '0':
            parts.append(r'(.*?)')
        else:
            parts.append(re.escape(part))
    return r'\s*'.join(parts) + r'\s*'

def respond(input_str):
    """Generate a response based on the input."""
    input_str = preprocess(input_str)
    kw = find_keyword(input_str)
    if not kw:
        return "I SEE."  # Edge case: no keyword matches
    
    for decomp, responses in rules[kw]:
        regex = build_regex(decomp)
        match = re.match(regex, input_str, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if isinstance(response, tuple) and response[0] == '=':
                # Fallback to another keyword
                return respond_to_other(response[1], input_str)
            else:
                # Replace placeholders (1, 2, etc.) with matched groups
                for i, group in enumerate(match.groups(), 1):
                    response = response.replace(str(i), group.strip())
                return response
    return "I SEE."  # Fallback if no decomp matches

def respond_to_other(other_kw, input_str):
    """Respond using another keyword's rules (for fallback)."""
    for decomp, responses in rules.get(other_kw, []):
        regex = build_regex(decomp)
        match = re.match(regex, input_str, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            for i, group in enumerate(match.groups(), 1):
                response = response.replace(str(i), group.strip())
            return response
    return "I SEE."

# Main loop (Steps 1 and 2)
print("ELIZA: HELLO, I AM ELIZA. HOW CAN I HELP YOU?")
while True:
    user_input = input("YOU: ").strip()
    if user_input.lower() in ['quit', 'goodbye', 'bye']:
        print("ELIZA: GOODBYE!")
        break
    response = respond(user_input)
    print("ELIZA: " + response)

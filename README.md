<h1>ELIZA Chatbot</h1>
<h2>Description</h2>
<h3>This is a simple implementation of the classic ELIZA chatbot, an early natural language processing program developed by Joseph Weizenbaum in the 1960s. ELIZA simulates a Rogerian psychotherapist by using pattern matching and substitution to create the illusion of understanding. This version is built in Python and follows a step-by-step challenge to recreate ELIZA's core logic.

Inspired by the original DOCTOR script, this chatbot responds to user inputs by mirroring concerns, turning questions back on the user, and providing therapist-like replies. It's a fun way to explore early AI concepts and see if modern users still fall for the "ELIZA effect"!</h3>

<h2>Features</h2>

<h3>Pattern Matching: Uses regex-based decomposition rules to match user inputs against keywords like "HELLO", "WHY", "WHAT", and "BYE".
Dynamic Responses: Generates varied replies by randomly selecting from response lists and substituting placeholders with user input parts.
Keyword Priority: Processes keywords in order of priority (e.g., "HELLO" before "WHY").
Fallback Handling: Responds with generic phrases like "I SEE." for unmatched inputs.
Quit Functionality: Allows users to exit with commands like "quit", "goodbye", or "bye".
Extensible: Rules are stored in a data structure, making it easy to add more patterns or load from a file.</h3>

Usage
Starting: Run the script as above. ELIZA will display a welcome message.
Interacting: Type your messages at the "YOU:" prompt. ELIZA will respond based on patterns.
Quitting: Type "quit", "goodbye", or "bye" to end the session.
Examples:
Input: "Hello" → ELIZA: "HELLO, HOW ARE YOU FEELING TODAY?"
Input: "Why don't I go outside?" → ELIZA: "DO YOU BELIEVE I DON'T go outside?" (or a similar random response)
Input: "What is this?" → ELIZA: "WHAT DO YOU MEAN BY THAT?" (or another variant)
Input: "Something random" → ELIZA: "I SEE." (fallback for no match)
How It Works
Preprocessing: Input is cleaned (punctuation removed, converted to uppercase) for case-insensitive matching.
Keyword Detection: Scans for prioritized keywords in the input.
Decomposition and Matching: Converts rules (e.g., (0 WHY DON'T I 0)) into regex patterns to match and capture parts of the input.
Reassembly: Substitutes placeholders in responses (e.g., 2 for the second captured group) to create personalized replies.
Fallbacks: If no keyword or pattern matches, defaults to "I SEE."
This mimics ELIZA's algorithm without true intelligence—just clever pattern substitution!

Screenshots/Examples
(Add images here if you upload them to the repo)

Example interaction:

ELIZA: HELLO, I AM ELIZA. HOW CAN I HELP YOU?
YOU: Hello
ELIZA: HELLO, HOW ARE YOU FEELING TODAY?
YOU: Why don't I try harder?
ELIZA: SHOULD YOU try harder YOURSELF?
YOU: bye
ELIZA: GOODBYE!

Extending the Project
Add More Rules: Edit the rules dictionary in eliza.py to include additional keywords, decompositions, and responses.
Load from File: Implement Step 3 of the challenge by parsing the full DOCTOR script (available from ELIZA Archaeology sites) into the rules structure.
Host Online: Use Flask or another web framework to create a web interface and share a live demo.
Custom Scripts: Create your own therapist personas by modifying rules.

Credits
Original ELIZA concept by Joseph Weizenbaum (1966).
Challenge inspiration from Coding Challenges.
Resources: ELIZA Archaeology site, Weizenbaum's CACM paper, and Wikipedia.

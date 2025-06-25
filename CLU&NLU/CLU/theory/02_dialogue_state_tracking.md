# CLU Theory: Dialogue State Tracking

Dialogue state tracking (DST) is a core component of conversational systems. It keeps track of the user's goals, filled slots, and conversation context across multiple turns.

## Key Concepts
- **Slots:** Variables to be filled (e.g., origin, destination, date)
- **State:** The current values of all slots and user goals
- **Update:** Each user turn may update the state (e.g., provide a missing slot)

## Example
User: "I want to book a flight."
- State: {intent: book_flight, origin: None, destination: None, date: None}

User: "From New York to Paris."
- State: {intent: book_flight, origin: New York, destination: Paris, date: None}

User: "On June 10th."
- State: {intent: book_flight, origin: New York, destination: Paris, date: June 10th}

DST enables robust, multi-turn conversations and is essential for real-world assistants.

For more, see [Microsoft CLU Dialogue Management](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/tutorial-dialogue).

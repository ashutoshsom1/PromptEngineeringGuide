# NLU Theory: Semantic Parsing

Semantic parsing is the process of mapping natural language to structured representations, such as logical forms, SQL queries, or API calls. It enables machines to understand and execute user instructions.

## Key Concepts
- **Logical Form:** A structured representation of meaning (e.g., lambda calculus, SQL)
- **End-to-End Models:** Neural models that map text directly to structured outputs
- **Applications:** Question answering, virtual assistants, database querying

## Example
Text: "Show me all flights from Paris to Berlin on June 10th."
Semantic Parse: `SELECT * FROM flights WHERE origin='Paris' AND destination='Berlin' AND date='2022-06-10'`

For more, see [Stanford CoreNLP Semantic Parsing](https://stanfordnlp.github.io/CoreNLP/).

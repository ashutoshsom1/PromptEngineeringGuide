# NLU Theory: Evaluation Metrics

Evaluating NLU models is essential for building robust language understanding systems. Common metrics include:

- **Accuracy:** Percentage of correct predictions (e.g., for classification)
- **Precision & Recall:** Precision is the fraction of relevant instances among the retrieved, recall is the fraction of relevant instances that were retrieved
- **F1 Score:** Harmonic mean of precision and recall
- **Entity-level F1:** For NER, measures overlap between predicted and true entities
- **Confusion Matrix:** Visualizes model performance across classes

## Example
If your model predicts the correct label for 85 out of 100 samples, accuracy is 85%.

For more, see [spaCy Evaluation](https://spacy.io/usage/training#metrics) and [Hugging Face Evaluation](https://huggingface.co/docs/evaluate/index).

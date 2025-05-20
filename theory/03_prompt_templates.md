# Prompt Templates

Prompt templates are reusable patterns for constructing prompts. They help standardize and automate prompt creation for different tasks and models.

## Benefits

- Consistency across tasks
- Easier experimentation
- Faster iteration
- Enables sharing and reproducibility

## Example Template

```text
Task: {task_description}
Input: {input_text}
Instruction: {instruction}
Output:
```

## Advanced Template Patterns

- **Role-based templates:** Assign a role to the model (e.g., "You are a helpful assistant...")
- **Instruction + Context:** Provide clear instructions and relevant context
- **Delimiters:** Use triple backticks or XML tags to separate sections
- **Dynamic placeholders:** Use variables for easy substitution

For more template ideas, see [Prompt Elements](https://www.promptingguide.ai/introduction/elements) and [Prompting Examples](https://www.promptingguide.ai/introduction/examples).

---

Explore the `/examples` directory for Python code that uses prompt templates.

# Types of Prompts

Prompt engineering leverages a wide variety of prompt types and techniques to achieve different goals. The most up-to-date types, as referenced from [promptingguide.ai](https://www.promptingguide.ai/), include:

## Zero-shot Prompting

- No examples are provided.
- The model is expected to perform the task based solely on the instruction.

## Few-shot Prompting

- A few examples are included in the prompt to guide the model.
- Improves performance on complex or ambiguous tasks.

## Chain-of-Thought Prompting

- Encourages the model to reason step-by-step.
- Useful for tasks requiring logical reasoning or multi-step solutions.

## Meta Prompting

- Prompts that instruct the model to generate or improve other prompts.

## Self-Consistency

- Generates multiple reasoning paths and selects the most consistent answer.

## Generate Knowledge Prompting

- Prompts the model to generate relevant knowledge before answering.

## Prompt Chaining

- Combines multiple prompts in sequence to solve complex tasks.

## Tree of Thoughts (ToT)

- Explores multiple reasoning paths in a tree structure for complex reasoning.

## Retrieval Augmented Generation (RAG)

- Integrates external knowledge or documents into the prompt for more accurate responses.

## ReAct (Reason + Act)

- Combines reasoning and tool use in a single prompt for agent-like behavior.

## Reflexion

- Prompts the model to reflect on and improve its previous outputs.

## Multimodal CoT

- Applies chain-of-thought reasoning to multimodal (text + image) tasks.

## Other Advanced Techniques

- Directional Stimulus Prompting (DSP)
- Program-Aided Language Models (PAL)
- Active-Prompt
- Automatic Prompt Engineer (APE)

---

See the `/examples` and `/notebooks` directories for code demonstrations of each type. For more, visit [Prompt Engineering Guide](https://www.promptingguide.ai/techniques).

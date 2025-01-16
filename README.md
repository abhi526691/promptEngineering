# Prompt Engineering

This project focused on using prompting techniques like Zero-Shot, Few-Shot, Chain-Of-Thought(CoT) and Directional Stimulus Prompting (DSP) for guiding language model to perform tasks effectively. This repository includes implementations of various prompting strategies, evaluation metrics, and key insights into improving the quality of chatbot responses.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Prompting Techniques](#prompting-techniques)
- [Metrics Overview](#metrics-overview)
- [Key Insights](#key-insights)
- [Hosting and Repository Links](#hosting-and-repository-links)
- [Acknowledgements](#acknowledgements)

---

## Project Overview

This project demonstrates various prompting strategies to guide language models in generating high-quality responses. The implemented prompting types are evaluated using metrics like ROUGE-L and BERT Score. The goal is to compare techniques and derive insights into the best practices for improving semantic understanding and response quality.

## Features

- **Prompting Strategies**: Implements Zero-shot, Few-shot, Chain-of-Thought, and Directional Stimulus Prompting.
- **Metrics Evaluation**: Uses ROUGE-L and BERT Score to evaluate model outputs.
- **Comparative Analysis**: Provides insights into the performance of different prompting techniques.
- **Streamlit Interface**: User-friendly interface for interacting with the model and visualizing results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abhi526691/promptEngineering
   cd base_directory
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

---

## Usage

1. Run the application using Streamlit:

   ```bash
   streamlit run app.py
   ```

2. Interact with the UI to explore the implemented prompting techniques and view the evaluation metrics.
3. Review insights and performance comparisons for each technique.

---

## Prompting Techniques

The following prompting strategies are explored:

1. **Zero-Shot Prompting**: No examples are provided; the model relies on general knowledge.
2. **Few-Shot Prompting**: A few input-output examples are included to guide the model.
3. **Chain-of-Thought (CoT)**: Breaks down reasoning into intermediate steps for complex tasks.
4. **Directional Stimulus Prompting (DSP)**: Provides explicit instructions to shape the model's response.

---

## Metrics Overview

### ROUGE-L
- Evaluates structural similarity between generated responses and reference texts.
- Focuses on precision, recall, and relevance.

### BERT Score
- Measures semantic similarity using embeddings from a pre-trained BERT model.
- Focuses on meaning rather than exact word matches.

---

## Key Insights

- **Best Technique**: Chain-of-Thought with Updated Responses demonstrates the highest ROUGE-L and BERT Scores.
- **Zero-Shot**: Performs poorly due to the lack of examples.
- **Few-Shot**: Performance improves significantly with examples.
- **DSP**: Useful for shaping responses but less effective in semantic understanding.

---

## Hosting and Repository Links

- **App Hosting**: [NLP_Assignment4 Streamlit App](https://abhi526691-nlp-assignment4-app-pvf4vt.streamlit.app/)
- **GitHub Repository**: [NLP_Assignment4 GitHub](https://github.com/abhi526691/NLP_Assignment4)

---

## Acknowledgements

- **Contributors**: [Abhishek Pandey](https://github.com/abhi526691), [Ram Krishna Dhakal](https://github.com/rkdhakal)
- **Tools Used**:
  - [Streamlit](https://streamlit.io/) for UI development.
  - [Hugging Face Transformers](https://huggingface.co/transformers/) for implementing BERT-based evaluations.

---

This project showcases effective methods for guiding language models through advanced prompting techniques and evaluates their impact using robust metrics. It serves as a valuable resource for researchers and practitioners in the field of NLP.



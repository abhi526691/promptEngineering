import os
import pandas as pd
import streamlit as st
from groq import Groq

# Base Class for Chatbot


class Base:
    def __init__(self, dataset):
        os.environ["GROQ_API_KEY"] = "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"
        self.client = Groq()
        self.df = dataset  # Use the preloaded dataset
        self.LLAMA3_70B_INSTRUCT = "llama-3.1-70b-versatile"
        self.LLAMA3_8B_INSTRUCT = "llama3.1-8b-instant"
        self.DEFAULT_MODEL = self.LLAMA3_70B_INSTRUCT

    def assistant(self, content: str):
        return {"role": "assistant", "content": content}

    def user(self, content: str):
        return {"role": "user", "content": content}

    def system(self, content: str):
        return {"role": "system", "content": content}

    def chat_completion(self, messages, temperature=0.6, top_p=0.9) -> str:
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.DEFAULT_MODEL,
                temperature=temperature,
                top_p=top_p,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

    def completion(self, prompt: str, temperature=0.6, top_p=0.9) -> str:
        return self.chat_completion([self.user(prompt)], temperature=temperature, top_p=top_p)

    def random_sample(self, n: int):
        few_shot_list = []
        try:
            random_data = self.df.sample(n)
        except ValueError:
            st.error("Error: Not enough data in the dataset for sampling.")
            return []

        human_list = random_data["human"]
        gpt_list = random_data["gpt"]
        few_shot_list.append(
            self.system(
                "You are a chatbot. For each message, return a response based on user input.")
        )
        for i, j in zip(human_list, gpt_list):
            few_shot_list.append(self.user(i))
            few_shot_list.append(self.assistant(j))
        return few_shot_list

    def random_sample_cot(self, n: int):
        few_shot_list = []
        try:
            random_data = self.df.sample(n)
        except ValueError:
            st.error("Error: Not enough data in the dataset for sampling.")
            return []

        human_list = random_data["human"]
        gpt_list = random_data["gpt_cot"]
        few_shot_list.append(
            self.system(
                "You are a chatbot that uses step-by-step reasoning (Chain of Thought).")
        )
        for human, gpt in zip(human_list, gpt_list):
            few_shot_list.append(self.user(human))
            few_shot_list.append(self.assistant(gpt))
        return few_shot_list

    def generate_response(self, few_shot_list, text: str):
        few_shot_list.append(self.user(text))
        return self.chat_completion(messages=few_shot_list)

    def gpt_dsp(self, human_input, hint="empathetic and structured"):
        return f"Hint: Respond to the following input in an {hint} manner.\nUser Input: {human_input}"


# Prompt Engineering Class
class PromptEngineering(Base):
    def zero_shot(self, prompt):
        return self.completion(prompt)

    def few_shot(self, sample_size, human_input):
        few_shot_list = self.random_sample(sample_size)
        if not few_shot_list:
            return "Error: Few-shot prompt generation failed due to insufficient data."
        return self.generate_response(few_shot_list, human_input)

    def chain_of_thought(self, sample_size, human_input):
        few_shot_list = self.random_sample_cot(sample_size)
        if not few_shot_list:
            return "Error: Chain of Thought (CoT) prompt generation failed due to insufficient data."
        return self.generate_response(few_shot_list, human_input)

    def directional_stimulus_prompting(self, human_input, hint="empathetic and structured"):
        dsp_prompt = self.gpt_dsp(human_input, hint=hint)
        return self.generate_response([], dsp_prompt)


# Streamlit UI
st.set_page_config(page_title="Chatbot with Prompt Engineering", layout="wide")
st.title("ChatGPT-like Chatbot with Prompt Engineering")

# Load the dataset once
try:
    dataset = pd.read_csv("final.csv")
except FileNotFoundError:
    st.error("Error: 'final_preprocessed.csv' not found.")
    dataset = pd.DataFrame(columns=["human", "gpt", "gpt_cot"])

# Initialize Prompt Engineering with the loaded dataset
prompt_engineering = PromptEngineering(dataset)


# Store conversation history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
            "content": "Hello! I am your AI assistant. How can I help you today?"}
    ]

# Sidebar for selecting prompt engineering technique
with st.sidebar:
    st.header("Prompt Engineering Settings")
    technique = st.selectbox(
        "Choose a Prompt Engineering Technique:",
        ["Zero-Shot", "Few-Shot",
            "Chain of Thought (CoT)", "Directional Stimulus Prompting (DSP)"]
    )
    if technique in ["Few-Shot", "Chain of Thought (CoT)"]:
        num_examples = st.slider(
            "Number of examples:", min_value=1, max_value=5, value=3)
        st.session_state.messages = [
            {"role": "assistant",
                "content": "Hello! I am your AI assistant. How can I help you today?"}
        ]
    if technique == "Directional Stimulus Prompting (DSP)":
        dsp_hint = st.text_input(
            "Enter a hint for DSP:", "empathetic and structured")
        st.session_state.messages = [
            {"role": "assistant",
                "content": "Hello! I am your AI assistant. How can I help you today?"}
        ]

# Input box and Send button
st.write("### Your Message")
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input(
        "Type your message here:", key="user_input", label_visibility="collapsed"
    )
with col2:
    send_clicked = st.button("Send")

# Handle "Send" button click
if send_clicked and user_input.strip():
    # Add user input to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate assistant response based on selected technique
    if technique == "Zero-Shot":
        response = prompt_engineering.zero_shot(user_input)
    elif technique == "Few-Shot":
        response = prompt_engineering.few_shot(num_examples, user_input)
    elif technique == "Chain of Thought (CoT)":
        response = prompt_engineering.chain_of_thought(
            num_examples, user_input)
    elif technique == "Directional Stimulus Prompting (DSP)":
        response = prompt_engineering.directional_stimulus_prompting(
            user_input, dsp_hint)
    else:
        response = "Invalid technique selected."

    # Add assistant response to conversation history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

    # # Rerun to update the UI immediately
    # st.experimental_rerun()

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Assistant:** {message['content']}")

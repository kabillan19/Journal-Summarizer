# AI-Powered Daily Journal Summarizer

This is a simple Streamlit app that uses the LLaMA 3.1 model with Groq capabilities to generate summaries of daily journal entries based on user-provided prompts. The app is designed to make it easy to create and analyze journal entries using advanced AI language models.

## Features

- **Text Input:** Users can input a custom prompt for their journal entry.
- **AI Summarization:** The app uses the `llama-3.1-70b-versatile` model to generate a summary based on the input.
- **Streamlit Interface:** Provides a simple and interactive web interface.

## Installation

To run this app locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install the required dependencies:**
   ```bash
   pip install streamlit langchain_groq
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter your prompt in the text input field.
2. Click the "Submit" button.
3. The app will generate and display a journal summary based on your input.

### Expected Output

The app will produce a summarized journal entry based on the input prompt provided.

## Configuration

- **Model:** `llama-3.1-70b-versatile`
- **Temperature:** 1 (Controls the randomness of the output)
- **Max Tokens:** 4096 (Maximum length of the output)

## Troubleshooting

- Ensure that your `groq_api_key` is valid and has access to the required services.
- Make sure you have the necessary Python packages installed.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the Streamlit and LangChain teams for creating such powerful tools for building AI applications.

```

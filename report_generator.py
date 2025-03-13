import ollama

def generate_report(summarized_text):
    """
    Format the summarized text as a professional news report
    using prompt engineering.
    """
    try:
        # Define the prompt for better structured news reports
        prompt = f"""Transform the following summary into a professional news broadcast script.

Guidelines:
- A compelling headline
- Clear, concise sentences
- Present tense where possible
- Smooth transitions
- A strong closing statement

Include: "This is Delta Headlines reporting."

Summary: {summarized_text}

News report:"""

        # Generate the news report using Ollama
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])

        # Extract and return the generated report
        report = response["message"]["content"]
        return report

    except Exception as e:
        print(f"Error in report generation: {e}")
        return f"Error during report generation: {str(e)}"

# Example usage
if __name__ == "__main__":
    test_summary = "The government has reduced jet fuel prices by 1.5% and commercial LPG prices by 14.5 per cylinder in its latest revision."
    print(generate_report(test_summary))

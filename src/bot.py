import click
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables (API KEY)
load_dotenv()

def sanitize_code(code):
    """Security: Basic sanitization to prevent abuse and injection."""
    if len(code) > 15000:
        raise ValueError("Error: File is too large to process.")
    return code.strip()

# Prompt Template with Chain of Thought (CoT)
SYSTEM_PROMPT = """
You are an expert in Clean Code and SOLID principles.
Follow this mandatory Chain of Thought process:
1. ANALYZE: Identify SOLID violations (especially Single Responsibility) and poor naming.
2. PLAN: Design a modular structure using classes or functions.
3. EXECUTE: Rewrite the code in Python following PEP 8.
4. DOCUMENT: Include comprehensive Google-style Docstrings and Type Hints.

Rule: Return ONLY the final refactored code inside a markdown code block.
"""

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    """Clean Code Bot: Automatically refactor dirty code using AI."""
    try:
        with open(file_path, 'r') as f:
            raw_code = f.read()

        # Input validation for security
        clean_input = sanitize_code(raw_code)

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        click.echo(click.style(f"🚀 Analyzing and refactoring: {file_path}...", fg='cyan'))

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Please refactor the following code:\n\n{clean_input}"}
            ]
        )

        result = completion.choices[0].message.content
        
        # Save the result in the examples folder
        output_filename = f"examples/clean_{os.path.basename(file_path)}"
        with open(output_filename, 'w') as f:
            f.write(result)

        click.echo(click.style(f"✅ Success! Optimized code saved to: {output_filename}", fg='green'))

    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg='red'))

if __name__ == '__main__':
    main()

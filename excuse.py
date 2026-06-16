from openai import OpenAI
import os

def generate_excuse(problem):
    try:
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        prompt = """
        You are an AI excuse generator.
        User types a problem and you generates the most ridiculous excuse possible.

        Examples:

        "Why didn't you do homework?"
        "A squirrel started a startup and hired me."
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Generate an excuse for the following problem: {problem}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating excuse: {str(e)}"
from flask import Flask, render_template, request, jsonify
from summarizer import TextSummarizer

# Initialize Flask app and summarizer
app = Flask(__name__)
summarizer = TextSummarizer()

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Render the home page for the app and process text summarization requests.

    For GET requests: Displays the form for user input.
    For POST requests: Summarizes the input text and displays the result.
    """
    if request.method == "POST":
        # Handle POST request: retrieve user input and generate summary text

        # Get user input from the form
        user_text = request.form.get("user_text")
        
        # Check if the input is empty or only contains whitespace
        if not user_text.strip():
            # Render the page with an error
            return render_template("index.html", summary="Please enter some text.")

        # Use the summarizer to generate a summary of the input text
        summary = summarizer.summarize(user_text)
        # Render the page with the summary and the original input
        return render_template("index.html", summary=summary, user_text=user_text)

    # Handle GET request: render the default page without the summary
    return render_template("index.html", summary=None)

@app.route("/api/summarize", methods=["POST"])
def api_summarize():
    """
    API endpoint for text summarization.

    Accepts a JSON payload with a "text" field, generates a summary 
    using the summarizer, and returns the result as a JSON response.
    """

    # Parse the incoming JSON payload from the request
    data = request.get_json()

    # Validate the input: check if "text" is present and not empty
    if "text" not in data or not data["text"].strip():
        # Respond with an error message and HTTP status 400 (bad request)
        return jsonify({"error": "Text input is required"}), 400

    # Use the summarizer to generate a summary of the provided text
    summary = summarizer.summarize(data["text"])

    # Return the summary in a JSON response
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)

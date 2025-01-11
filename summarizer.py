from transformers import pipeline

class TextSummarizer:
    """
    A text summarization utility using a pre-trained transformer model.
    
    This class leverages the Hugging Face Transformers library to perform 
    text summarization using a specified model. By default, it uses the 
    "facebook/bart-large-cnn" model.
    """

    def __init__(self, model_name="facebook/bart-large-cnn"):
        """
        Initializes the TextSummarizer with a pre-trained model.

        Parameters:
        - model_name (str): The name of the pre-trained model to use. 
          Defaults to "facebook/bart-large-cnn".
        """
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=100, min_length=30):
        """
        Summarizes the input text.

        Parameters:
        - text (str): The input text to summarize. It should be a reasonably 
          large string of content that requires summarization.
        - max_length (int): The maximum length of the summary. Defaults to 100.
        - min_length (int): The minimum length of the summary. Defaults to 30.

        Returns:
        - str: The summarized text.

        Raises:
        - ValueError: If the input text is empty or None.
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty.")
        
        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
        )
        return summary[0]["summary_text"]

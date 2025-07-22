from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def generate_titles(content, num_titles=3):
    try:
        logger.debug(f"Input content: {content[:1000]}")  # Log first 1000 chars
        # Initialize czearing/article-title-generator
        model_name = "czearing/article-title-generator"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
        
        # Summarize content
        if len(content) > 500:
            content = content[:500]
            logger.debug(f"Content truncated to 500 chars: {content}")
        summary = generator(f"summarize: {content}", max_length=50, min_length=10, do_sample=False)[0]['generated_text'].strip()
        logger.debug(f"Generated summary: {summary}")
        
        # Generate titles
        prompt = f"Generate a catchy blog title for: {summary}"
        logger.debug(f"Prompt: {prompt}")
        titles_raw = generator(
            prompt,
            max_length=30,  # Allow longer titles
            min_length=10,
            do_sample=True,
            num_beams=10,
            no_repeat_ngram_size=3,
            temperature=1.5,  # Higher for diversity
            top_p=0.9,
            top_k=50,  # Add top-k sampling
            num_return_sequences=num_titles
        )
        
        # Clean up titles
        titles = []
        for i, title_dict in enumerate(titles_raw):
            title = title_dict['generated_text'].strip().capitalize()
            # Robust prompt removal
            for prefix in [prompt, prompt.lower(), "generate a catchy blog title for:", "Generate a catchy blog title for:"]:
                title = title.replace(prefix, '').replace(prefix.lower(), '').strip()
            if title.endswith('.'):
                title = title[:-1]
            if not title or len(title) < 5:
                title = f"Blog title {i+1}"
            titles.append(title)
        
        # Ensure unique titles
        titles = list(dict.fromkeys(titles))[:num_titles]
        while len(titles) < num_titles:
            titles.append(f"Blog title {len(titles)+1}")
        
        logger.debug(f"Generated titles: {titles}")
        return titles
    except Exception as e:
        logger.error(f"Error generating titles: {str(e)}")
        return [f"Fallback Title {i+1}" for i in range(num_titles)]
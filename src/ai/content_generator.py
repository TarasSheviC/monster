from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ContentGenerator:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def generate_comment(self, post_content, personality):
        prompt = f"Написать {personality['communication_style']} комментарий к посту: {post_content}"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

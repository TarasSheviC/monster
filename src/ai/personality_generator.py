import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class PersonalityGenerator:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def generate_personality(self):
        prompt = "Создать легенду для ВКонтакте:"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=200, num_return_sequences=1)
        personality = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return {
            "background": personality,
            "communication_style": random.choice(["Дружелюбный", "Саркастичный", "Формальный", "Casual"]),
            "interests": random.sample(["технологии", "искусство", "спорт", "путешествия", "наука"], k=3)
        }

import torch

def load_model(model_name="gpt2"):
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

def generate_text(model, tokenizer, prompt, max_length=150):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length)
    return tokenizer.decode(output[0], skip_special_tokens=True)

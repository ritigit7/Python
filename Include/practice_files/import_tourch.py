import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Encode the input text
input_text = "What is the meaning of life?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate the response
output = model.generate(input_ids)

# Decode the output
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)

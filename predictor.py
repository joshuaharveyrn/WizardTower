# predictor.py
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# download the pretrained DistilGPT2 model and set it to evaluation
model = GPT2LMHeadModel.from_pretrained("distilgpt2")
model.eval()
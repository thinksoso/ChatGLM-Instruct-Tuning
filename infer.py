import torch
from transformers import AutoTokenizer, AutoModel
from modeling_chatglm import ChatGLMForConditionalGeneration
tokenizer = AutoTokenizer.from_pretrained(
    "THUDM/chatglm-6b", trust_remote_code=True)
model = ChatGLMForConditionalGeneration.from_pretrained(
    "output/your_model_dir").half().cuda()

response, history = model.chat(tokenizer, "你好", history=[],max_length=256)
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", max_length=256,history=history)
print(response)

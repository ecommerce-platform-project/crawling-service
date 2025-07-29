
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# tokenizer = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")
# model = AutoModelForSequenceClassification.from_pretrained("beomi/KcELECTRA-base")

# text = "친구에게 소개받아서 먹으러 왔는데 넘 맛있어용!! 파스타나 리조또 종류도 많고 가격도 괜찮아요"

# inputs = tokenizer(text, return_tensors="pt", truncation=True)
# outputs = model(**inputs)
# probs = torch.softmax(outputs.logits, dim=-1)
# label = torch.argmax(probs, dim=-1).item()
# print(f'label {label}')
# print("긍정" if label == 1 else "부정")
from transformers import AutoModelForTokenClassification, AutoTokenizer
model_name = "w11wo/indonesian-roberta-base-posp-tagger"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.save_pretrained('./model')
tokenizer.save_pretrained('./model')
from transformers import AutoModel, AutoTokenizer

# Using the community model
# BERT Base
tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')
model = AutoModel.from_pretrained('neuralmind/bert-base-portuguese-cased')



# sentence_embedins = model.encoder()

help(model)
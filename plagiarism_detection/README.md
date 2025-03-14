## BERT Model

### Scope: Plagiarism Detection

Tools: pandas, numpy, sklearn torch, keras, transformers

These are the steps taken to train an instance of Google's BERT model (bert-base-uncased).

It uses the BertTokenizer to encode text and an instance of AutoModelForSequenceClassification model to create vector embeddings from text using the tokenizer. Tensors were created using Torch.

The dataset for training was gotten from Kaggle here: https://www.kaggle.com/datasets/jjinho/wikipedia-20230701?select=a.parquet

It was downloaded, uploaded to a google drive, mounted and loaded by the code.

This model was trained on Wikipedia articles dated up to 2023-07-01 from the a.parquet file. This file contains Wikipedia articles that begin with the letter A only. The sample size used was 100 for tests.

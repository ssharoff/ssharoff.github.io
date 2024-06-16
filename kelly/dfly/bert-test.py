#!/usr/bin/env python
# coding: utf-8
# the script tests the predictions obtained from running ./bert-train.py

import time
teststart=int(time.time())

import pandas as pd
import numpy as np
import sys

mname = sys.argv[1] # the pytorch model
fname = sys.argv[2] # the test file name, formatted as Label\tText

label_dict = {'vikidia': 0, 'wiki': 1}
df = pd.read_csv(fname,sep='\t',names=['class','text'] , dtype={'class': str, 'text': str}, keep_default_na=False)
texts = df.text.values.tolist()
# sanity check to prevent errors down the pipeline
for i,l in enumerate(texts):
    if not isinstance(l, str):
        print(f'Error in line {i+1}, type={type(l)}, line="{l}"', file=sys.stderr)

df['label'] = df['class'].replace(label_dict)
for i,v in enumerate(df.label.values.tolist()):
    if not isinstance(v,int):
        print(f'Error in line {i+1}, type={type(v)}, line="{v}"', file=sys.stderr)

import torch
from transformers import BertTokenizer
from torch.utils.data import TensorDataset, DataLoader
from sklearn.metrics import f1_score, confusion_matrix
from transformers import BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained("bert-base-multilingual-cased",
                                                      num_labels=len(label_dict),
                                                      output_attentions=False,
                                                      output_hidden_states=False)


def f1_score_func(preds, labels):
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    return f1_score(labels_flat, preds_flat, average='weighted')

def plot_confusion_matrix(preds, labels, label_dict):
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    label_to_name = {value: key for key, value in label_dict.items()}

    cm = confusion_matrix(labels_flat, preds_flat)
    print(cm)

def metrics_per_class(preds, labels, label_dict):
    label_dict_inverse = {v: k for k, v in label_dict.items()}

    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()

    # Calculate confusion matrix
    cm = confusion_matrix(labels_flat, preds_flat)

    for label in np.unique(labels_flat):
        # True Positives
        TP = cm[label, label]
        # False Positives: sum of the corresponding column minus TP
        FP = np.sum(cm[:, label]) - TP
        # False Negatives: sum of the corresponding row minus TP
        FN = np.sum(cm[label, :]) - TP

        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        recall = TP / (TP + FN) if (TP + FN) != 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

        print(f'Class: {label_dict_inverse[label]}')
        print(f'Accuracy: {TP}/{TP+FN} (True Positives / Total Actual Positives)')
        print(f'Precision: {precision:.2f}')
        print(f'Recall: {recall:.2f}')
        print(f'F1 Score: {f1:.2f}\n')


def evaluate(dataloader_val):

    model.eval()

    loss_val_total = 0
    predictions, true_vals = [], []

    for batch in dataloader_val:

        batch = tuple(b.to(device) for b in batch)

        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }

        with torch.no_grad():
            outputs = model(**inputs)

        loss = outputs[0]
        logits = outputs[1]
        loss_val_total += loss.item()

        logits = logits.detach().cpu().numpy()
        label_ids = inputs['labels'].cpu().numpy()
        predictions.append(logits)
        true_vals.append(label_ids)

    loss_val_avg = loss_val_total/len(dataloader_val)

    predictions = np.concatenate(predictions, axis=0)
    true_vals = np.concatenate(true_vals, axis=0)

    return loss_val_avg, predictions, true_vals

model = BertForSequenceClassification.from_pretrained("bert-base-multilingual-cased", num_labels=2)
model.load_state_dict(torch.load(mname))
device = "cpu"
if torch.cuda.is_available():
    device = "cuda"
    model = model.to(device)

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased', # 'xlm-roberta-base',
                                      do_lower_case=True)
encoded_data_predict = tokenizer.batch_encode_plus(
    texts,
    add_special_tokens=True,
    return_attention_mask=True,
    padding='longest',
    max_length=512,
    truncation=True,
    return_tensors='pt'
)

input_ids_predict = encoded_data_predict['input_ids']
attention_masks_predict = encoded_data_predict['attention_mask']
labels_predict = torch.tensor(df.label.values.tolist())

dataset_predict = TensorDataset(input_ids_predict, attention_masks_predict, labels_predict)


batch_size = 5
dataloader_predict = DataLoader(dataset_predict,
                              batch_size=batch_size)

predict_loss, predictions, true_predict = evaluate(dataloader_predict)
predict_f1 = f1_score_func(predictions, true_predict)

print(f'Processing {fname} in {int(time.time())-teststart} sec')
print(f'Prediction loss: {predict_loss}')
print(f'F1 Score (Weighted): {predict_f1}')
plot_confusion_matrix(predictions, true_predict, label_dict)
metrics_per_class(predictions, true_predict, label_dict)

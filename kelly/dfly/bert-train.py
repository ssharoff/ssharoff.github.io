#!/usr/bin/env python
# coding: utf-8
# The scripts trains a BERT model for predicting classes from a one-line dataset:
# CLASS\tTEXT

import time
starttime=int(time.time())

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

fname=sys.argv[1]
model_name=sys.argv[2] if len(sys.argv)>2 else 'bert-base-multilingual-cased'
# 'xlm-roberta-base',

df = pd.read_csv(fname,sep='\t',names=['class','text'])
loadedtime=int(time.time())
print(f'Loading {fname} in {loadedtime-starttime} secs. \nSanity test:', file=sys.stderr)
print(df.head(), file=sys.stderr)
print(df['class'].value_counts(), file=sys.stderr)
label_dict = {'vikidia': 0, 'wiki': 1}
df['label'] = df['class'].replace(label_dict)
print(df['label'].value_counts(), file=sys.stderr)

import random

seed_val = 42
random.seed(seed_val)
np.random.seed(seed_val)

X_train, X_val, y_train, y_val = train_test_split(df.index.values,
                                                  df.label.values,
                                                  test_size=0.15,
                                                  stratify=df.label.values)
df['data_type'] = ['not_set']*df.shape[0]
df.loc[X_train, 'data_type'] = 'train'
df.loc[X_val, 'data_type'] = 'val'

print(df.groupby(['class', 'label', 'data_type']).count().sort_values(['label']), file=sys.stderr)

import torch
from transformers import BertTokenizer
from torch.utils.data import TensorDataset
from transformers import BertForSequenceClassification

torch.manual_seed(seed_val)
torch.cuda.manual_seed_all(seed_val)

tokenizer = BertTokenizer.from_pretrained(model_name, do_lower_case=True)

encoded_data_train = tokenizer.batch_encode_plus(
    df[df.data_type=='train'].text.values,
    add_special_tokens=True,
    return_attention_mask=True,
    pad_to_max_length=True,
    max_length=512,
    truncation=True,
    return_tensors='pt'
)

encoded_data_val = tokenizer.batch_encode_plus(
    df[df.data_type=='val'].text.values,
    add_special_tokens=True,
    return_attention_mask=True,
    pad_to_max_length=True,
    max_length=512,
    truncation=True,
    return_tensors='pt'
)


input_ids_train = encoded_data_train['input_ids']
attention_masks_train = encoded_data_train['attention_mask']
labels_train = torch.tensor(df[df.data_type=='train'].label.values)

input_ids_val = encoded_data_val['input_ids']
attention_masks_val = encoded_data_val['attention_mask']
labels_val = torch.tensor(df[df.data_type=='val'].label.values)

dataset_train = TensorDataset(input_ids_train, attention_masks_train, labels_train)
dataset_val = TensorDataset(input_ids_val, attention_masks_val, labels_val)


model = BertForSequenceClassification.from_pretrained(model_name,
                                                      num_labels=len(label_dict),
                                                      output_attentions=False,
                                                      output_hidden_states=False)


from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

batch_size = 3

dataloader_train = DataLoader(dataset_train,
                              sampler=RandomSampler(dataset_train),
                              batch_size=batch_size)

dataloader_validation = DataLoader(dataset_val,
                                   sampler=SequentialSampler(dataset_val),
                                   batch_size=batch_size)

from transformers import AdamW, get_linear_schedule_with_warmup

optimizer = AdamW(model.parameters(),
                  lr=1e-5,
                  eps=1e-8)

epochs = 6

scheduler = get_linear_schedule_with_warmup(optimizer,
                                            num_warmup_steps=0,
                                            num_training_steps=len(dataloader_train)*epochs)

from sklearn.metrics import f1_score, confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns

def f1_score_func(preds, labels):
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    return f1_score(labels_flat, preds_flat, average='weighted')

def accuracy_per_class(preds, labels):
    label_dict_inverse = {v: k for k, v in label_dict.items()}

    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()

    for label in np.unique(labels_flat):
        y_preds = preds_flat[labels_flat==label]
        y_true = labels_flat[labels_flat==label]
        print(f'Class: {label_dict_inverse[label]}')
        print(f'Accuracy: {len(y_preds[y_preds==label])}/{len(y_true)}\n')

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


device = 'cuda'

model = model.to(device)

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

beforetraining=int(time.time())
print(f'Training/loading: {beforetraining-loadedtime} secs', file=sys.stderr)

for epoch in range(1, epochs+1):
    epochstart=int(time.time())

    model.train()

    loss_train_total = 0

    for batch in dataloader_train:

        model.zero_grad()

        batch = tuple(b.to(device) for b in batch)

        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }

        outputs = model(**inputs)

        loss = outputs[0]
        loss_train_total += loss.item()
        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

        optimizer.step()
        scheduler.step()

    torch.save(model.state_dict(), f"model-{fname}-e{epoch}.pth")

    loss_train_avg = loss_train_total/len(dataloader_train)
    print(f'Epoch {epoch} completed in {int(time.time())-epochstart} secs')
    print(f'Training loss: {loss_train_avg}')
    val_loss, predictions, true_vals = evaluate(dataloader_validation)
    val_f1 = f1_score_func(predictions, true_vals)
    print(f'Validation loss: {val_loss}')
    print(f'F1 Score (Weighted): {val_f1}')
    #accuracy_per_class(predictions, true_vals)
    plot_confusion_matrix(predictions, true_vals, label_dict)
    metrics_per_class(predictions, true_vals, label_dict)

for language in ['fr', 'en', 'it', 'ca', 'es', 'ru']:
    teststart=int(time.time())
    df = pd.read_csv(f'test-{language}.dat',sep='\t',names=['class','text'])
    df['label'] = df['class'].replace(label_dict)
    print(df.head(), file=sys.stderr)

    tokenizer = BertTokenizer.from_pretrained(model_name, do_lower_case=True)

    encoded_data_predict = tokenizer.batch_encode_plus(
        df.text.values,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=512,
        truncation=True,
        return_tensors='pt'
    )

    input_ids_predict = encoded_data_predict['input_ids']
    attention_masks_predict = encoded_data_predict['attention_mask']
    labels_predict = torch.tensor(df.label.values)

    dataset_predict = TensorDataset(input_ids_predict, attention_masks_predict, labels_predict)


    batch_size = 3

    dataloader_predict = DataLoader(dataset_predict,
                                  sampler=RandomSampler(dataset_predict),
                                  batch_size=batch_size)

    predict_loss, predictions, true_predict = evaluate(dataloader_predict)
    predict_f1 = f1_score_func(predictions, true_predict)

    print(f'{language} tested in {int(time.time())-teststart} sec')
    print(f'Predictions loss: {predict_loss}')
    print(f'F1 Score (Weighted): {predict_f1}')
    plot_confusion_matrix(predictions, true_predict, label_dict)
    metrics_per_class(predictions, true_predict, label_dict)

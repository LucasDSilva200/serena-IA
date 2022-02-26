import yaml
import numpy as np
import sklearn as skl
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing 
import array


data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())
inputs,outputs = [],[]
for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'],command['action']))

#processar texto:palavras,caracteres,bytes,sub-palavras

chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)

chr2idx ={}
idx2chr={}

for i,ch in enumerate(chars):
    chr2idx[ch]=i
    idx2chr[i]=ch



max_seq = max([len(x) for x in inputs])

print('Número de chars ',len(chars))
print('Maior número de chars ',max_seq)

#criar dataset one-hot(número de exemplos, tamanho da sequêcia, num de caracteres) one-hot

input_data = np.zeros((len(inputs),max_seq,len(chars)),dtype='int32')
labels=set(outputs)
labels2idx={}
idx2label={}
for k,label in enumerate(labels):
    labels2idx[label]=k
    idx2label[k]=label
output_data=[]
for output in outputs:
    output_data.append(labels2idx[output])


enc = OneHotEncoder(drop='if_binary').fit(output_data)
enc.transform(output_data,output_data[output]).toarray
#CONTINUAR QUANDO EU TIVER MAIS CONHECIMENTO

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, chr2idx[ch]]=1.0

print(enc[0])


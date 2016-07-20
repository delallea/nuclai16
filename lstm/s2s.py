import pickle
import itertools
import numpy as np

import seq2seq
from seq2seq.models import SimpleSeq2seq


print('Creating model')
model = SimpleSeq2seq(input_dim=1, hidden_dim=12, output_length=8, output_dim=1, depth=1)
print('Compiling model')
model.compile(loss='mse', optimizer='rmsprop')

print('Creating data')
X = np.zeros((256, 8, 1), dtype=np.float32)
X[:,:,0] = list(itertools.product([0.0, 1.0], repeat=8))

print('Fitting model')
model.fit(X, X, batch_size=32, nb_epoch=1000, verbose=1)

print('Predicting')
y = model.predict(X)

print('Outputting result')
for i in range(16):
    print(X[i,:,0], y[i,:,0] > 0.5)

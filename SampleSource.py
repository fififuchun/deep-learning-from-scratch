# Sample

import chainer
import chainer.functions as F
import chainer.iterators
import chainer.links as L
from chainer import training
import chainer.optimizer

# Network def
class CNN(chainer.Chain):
    def __init__(self, train= True):
        super(CNN, self).__init__(
            l1 = L.linear(28*28, 100),
            l2 = L.linear(100, 10),
        )
    def __call__(self, x):
        h = F.sigmoid(self.l1(x))
        h = self.l2(h)
        return h

# Load
train, test= chainer.datasets.get_mnist(ndim=3)

# Set
model = L.Classifier(CNN())
optimizer= chainer.optimizer.Adam()
optimizer.setup(model)
train_iter= chainer.iterators.SerialIterator(train, batch_size=100)
updater= training.StandardUpdater(train_iter, optimizer)
trainer= training.Trainer(updater, (5, 'epoch'), out='result')

# Run
trainer.run()

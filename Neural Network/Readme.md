Artificial neural networks (ANNs), usually simply called neural networks (NNs), are computing systems inspired by the biological neural networks that constitute animal brains.

An ANN is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain. Each connection, like the synapses in a biological brain, can transmit a signal to other neurons. An artificial neuron that receives a signal then processes it and can signal neurons connected to it. The "signal" at a connection is a real number, and the output of each neuron is computed by some non-linear function of the sum of its inputs. The connections are called edges. Neurons and edges typically have a weight that adjusts as learning proceeds. The weight increases or decreases the strength of the signal at a connection. Neurons may have a threshold such that a signal is sent only if the aggregate signal crosses that threshold. Typically, neurons are aggregated into layers. Different layers may perform different transformations on their inputs. Signals travel from the first layer (the input layer), to the last layer (the output layer), possibly after traversing the layers multiple times.

-------------------------
![](https://upload.wikimedia.org/wikipedia/commons/4/44/Neuron3.png)


How artificaial neural network looks
----------------------------
![](https://github.com/DASHANANT/Deep-Learning-Basics-Python-files/blob/main/Neural%20Network/Architecture-of-multilayer-artificial-neural-network-with-error-backpropagation.png)



When to apply Neural Networks ?
----------------------------

- Firstly, neural networks require clear and informative data (and mostly big data) to train. Try to imagine Neural Networks as a child. It first observes how its parent walks. Then it tries to walk on its own, and with its every step, the child learns how to perform a particular task. It may fall a few times, but after few unsuccessful attempts, it learns how to walk. If you don’t let it walk, it might not ever learn how to walk. The more exposure you can provide to the child, the better it is.
- It is prudent to use Neural Networks for complex problems such as image processing. Neural nets belong to a class of algorithms called representation learning algorithms. These algorithms break down complex problems into simpler form so that they become understandable (or “representable”). Think of it as chewing food before you gulp. This would be harder for traditional (non-representation learning) algorithms.
- When you have appropriate type of neural network to solve the problem. Each problem has its own twists. So the data decides the way you solve the problem. For example, if the problem is of sequence generation, recurrent neural networks are more suitable. Whereas, if it is image related problem, you would probably be better of taking convolutional neural networks for a change.
- Last but not the least, hardware requirements are essential for running a deep neural network model. Neural nets were “discovered” long ago, but they are shining in the recent years for the main reason that computational resources are better and more powerful. If you want to solve a real life problem with these networks, get ready to buy some high-end hardware!

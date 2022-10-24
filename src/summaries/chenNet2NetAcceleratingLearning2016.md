@chenNet2NetAcceleratingLearning2016 introduce the idea of training a larger
student network from an existing smaller teacher network by using
*function-preserving transformations*.
These transformations (*Net2Net* operations) allow the rapid transfer of learned
knowledge and omits the need to retrain the larger network from scratch.

The authors propose two operations two increase the student network's size:

1. Growing in width: adding more units in each hidden layer and
2. growing in depth: adding more hidden layers.

Growth along the **width** dimension is achieved by randomly splitting the original
neurons (*Net2WiderNet* operation, see *@fig:splitting_neuron). Input weights of new neurons are copied from existing
and the output weight of existing neurons is equally distributed among all
copies (the old neuron and all new copies).

If no dropout is used, @chenNet2NetAcceleratingLearning2016 propose to add a small
noise to the input weights to break the symmetry.

![Illustration of *Net2WiderNet*. Here, a single neuron is split in two parts. However, multiple neurons can be split in one operation and each neuron may be split in multiple parts](img/splitting_neuron){#fig:splitting_neuron width=10cm}

Growth along the depth dimension is achieved by adding new layers which are
initialized with the identity function.
This requires idempotent activation functions: the activation function $\phi$
needs to chosen such that $\phi(\mathbf{I}\phi(\mathbf{v}))$ for any vector $\mathbf{v}$.
For rectified linear units (ReLU) this is the case, for some the identity matrix
may be replace with a different matrix, in some cases it may not be as easy
to construct an identity layer.



The experiments are conducted on an Inception network architecture [@szegedyGoingDeeperConvolutions2014],
a convolutional neural network (CNN).
They show that rapid transfer of knowledge through the two types of network
transformations is possible, allowing the faster exploration of model families
contained in this architecture space.

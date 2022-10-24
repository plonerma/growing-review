This publication offers an incremental extension to enable branched architectures
using function-preserving transformations [@chenNet2NetAcceleratingLearning2016]
and growing the model using a RL agent based meta-controller as in @caiEfficientArchitectureSearch2017.

@caiPathLevelNetworkTransformation2018 propose *path-level* transformations
which allows the branching of neural networks (whereas @chenNet2NetAcceleratingLearning2016
initially proposed just growing deeper and wider).
Instead of restricting the architecture space to sequences of layers,
@caiPathLevelNetworkTransformation2018 represent their network architecture as
trees.


![Illustration of a series of network transformations. The last part shows the tree-structure of the transformation. Figure from @caiPathLevelNetworkTransformation2018. \label{fig:path_level}](img/path_level){#fig:path_level width=100%}


Each *path-level* transformation follows either an *add* or a *concatenation*
merge scheme.
In the *add* scheme, a layer is replaced by two copies and each of their outputs
is multiplied by 0.5. This is similar to splitting a neuron, except on a layer
level. Transformation (a) in *@fig:path_level shows such a transformation.

In the *concatenation* scheme (step (b) in *@fig:path_level), the outputs dimensions (in a fully connected
layer: neuron outputs, in a convolutional layer: output channels, etc.)
are split among the different branches and the output of each branch is later
concatenated. This introduces branches while preserving the function and each
branch is unique.

These two schemes do not introduce a significant change to the network. However,
in combination with the existing operations [in @chenNet2NetAcceleratingLearning2016],
this can lead to a variety of branched architectures.

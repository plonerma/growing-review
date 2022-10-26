---

shorttitle: Network Morphism

---


@weiNetworkMorphism2016 follow a very similar path to @chenNet2NetAcceleratingLearning2016:
*function-preserving transformations* are used to grow a parent
(or "teacher") network to a child (or "student") network while maintaining
the same function.

@weiNetworkMorphism2016 point out that using an identity layer for growing in
depth (which they refer to as "IdMorp") may be sub-optimal as it is extremely
sparse. Additionally, they reiterate the requirement of idempotent activation
functions, which they deem insufficient.

Through an iterative procedure, a convolutional layer is decomposed into
two layers, retaining a large number of non-zero entries.

@weiStableNetworkMorphism2019 furhter improve the decomposition method in order
to minimize the performance drop after transforming (growing) the network.


Instead of relying on idempotent activation functions, @weiNetworkMorphism2016
introduce parametric activation functions for new layers:
A parameter $a$ interpolates between the identity function and the non-linear
activation function. $a$ is initialized with one such that there is essentially
no activation function. Over the course of future training, the parameter
can be learned to make the activation function non-linear [for an example see *@fig:ptanh or
the parametric rectified activation units (PReLU), @heDelvingDeepRectifiers2015].

![Illustration of an parametric tanh function: with $a=1$ the function is equal to the identity function, with $a=0$ it is equal to tanh.](img/parametric_tanh){#fig:ptanh}

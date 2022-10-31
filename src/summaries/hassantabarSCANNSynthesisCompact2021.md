---
shorttitle: SCANN
why: NAS
when: Fixed schedule
where: Connections based on gradient, Neurons based on activation
how: Connections based on gradient, Neurons are split
---


@hassantabarSCANNSynthesisCompact2021 develop SCANN to produce compact and
accurate feed-forward networks (FFNNs).
In this paper, they aim to improve on prior work (namely: [NeST](#sec:daiNeSTNeuralNetwork2018))
and allow the method to grow in depth as well.


SCANN includes three operations to modify the network architecture:

1. Growing new connections,
2. growing new neurons, and
3. pruning existing connections.


New connections are grown based on the gradient magnitude they would exhibit
(if they were present). This follows the proposal of @daiNeSTNeuralNetwork2018
for [NeST](#sec:daiNeSTNeuralNetwork2018).

New neurons are grown based on the activations existing neurons exhibit when
training data is passed through the network: Neurons with large activation
magnitude are selected for splitting.

Finally, connections which have small weight magnitudes are pruned. This is
similar to [NeST](#sec:daiNeSTNeuralNetwork2018) as well.


@hassantabarSCANNSynthesisCompact2021 describe three training schemes with
different configurations of network modification operations:
Different orders of executing the operations as well as different degrees of
growth and pruning and different sizes of initial networks.

They show that all of these three training schemes can yield well performing
models with different numbers of parameters.

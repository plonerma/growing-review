---
why: NAS
when: "Growth phase, then prune phase with iterative retraining in each phase"
where: Gradient-based selection
how: Initialization based on gradient
---


@daiNeSTNeuralNetwork2018 utilize growth with network architecture search (NAS)
in mind. They note that trial-and-error approaches are inefficient as a process
and can (as a product) lead to inefficient architectures which might far more
parameters than required.
To combat these issues, they propose NeST, which trains
weights as well as the architecture.

![Illustration of the steps for synthesizing an architecture using NeST [figure from @daiNeSTNeuralNetwork2018].](img/nest){#fig:nest width=100%}

NeST starts with an initial small network (a *seed architecture*). In a first
phase, the network is grown by adding new connections based on their gradient
(assuming they already existed with an weight of 0), and growing new neurons
in a layer $l$ in order to connect existing neurons $n$ and $m$ in layers $l-1$ and $l+1$
which if they were connected directly, exhibited a large gradient magnitude:

$$
G_{m,n} = \frac{\partial L}{\partial u_m^{l+1}} x_n^{l-1} \ge threshold
$$

Here, $u_m^{l+1}$ is the sum of incoming activations of neuron $m$ in layer $l+1$
and $x_n^{l-1}$ is the activation of neuron $n$ in layer $l+1$.
The threshold is calculated using a growth proportion.

In a second phase, weights are iteratively pruned. Between each pruning step,
the network is retrained to recover its performance.

It should be noted however, that NeST does not grow additional layers (nor does
it remove layers) and hence is limited to a fixed number of layers.

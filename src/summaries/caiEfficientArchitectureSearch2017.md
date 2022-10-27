---
shorttitle: NAS using Net Transforms
why: NAS
when: Fixed schedule
where: Decided by RL agent
how: "Function-preserving transforms"
---

@caiEfficientArchitectureSearch2017 propose using a reinforcement learning (RL)
agent as a meta-controller in order to decide when and where the network is grown
(using function-preserving transformations).

By using variable-length strings [see @zophNeuralArchitectureSearch2017] to
represent the network architecture, an RL agent can be used to generate a
function-preserving transformation [@chenNet2NetAcceleratingLearning2016].

The network architecture is encoded using an bidirectional LSTM and the encoding
is then fed to a number of actor networks which decides whether and where
transformations should be applied. For each possible network transformation
there is one actor network. For an illustration, see *@fig:cail_rl_agent.

![Illustration of the architecture embedding. Figure from @caiEfficientArchitectureSearch2017](img/cai_rl_agent){#fig:cail_rl_agent width=100%}


In each growth phase, 10 networks are sampled from the meta-controller and trained
for 20 epochs (on image datasets CIFAR-10 and SVHN). Based on the accuracy
on held out validation data ($acc_v$), a reward for the meta-controller is calculated.
Instead of directly using the accuracy as reward signal, @caiEfficientArchitectureSearch2017
propose using a non-linear transformation in order to increase the reward
if the accuracy is already high (an increase of 1% starting at 90% is more difficult
than starting at 60%):

$$
\tan(acc_v \times \frac{\pi}{2})
$$

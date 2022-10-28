---
shorttitle: NASH
why: NAS
when: Iterativly grow and train a set of networks, then pick the best
where: Randomly selected (multiple alternatives)
how: Function-preserving transforms
---

@elskenSimpleEfficientArchitecture2017 propose an iterative NAS algorithm
(Neural Architecture Search by Hillclimbing; short: NASH)
which -- in each growth step -- produces a set of grown child networks
(using function-preserving transformations). Each child is trained for a small
number of epochs before the most promising candidate is chosen. This best
performing child is then used for repeating the procedure (see +@fig:nash).

![Illustration of the NASH algorithm. A set of children is grown and trained. Then the best candidate is chosen. Figure from @elskenSimpleEfficientArchitecture2017.](img/nash){#fig:nash width=100%}

Additionally, they use a different set of network morphisms
(or *function-preserving transformations*) such as an interpolating layer
[similar to the parametric activation functions in @weiNetworkMorphism2016]:
Here an existing layer is replaced by an affine combination of the existing
layer and some new ones (starting with all weights of the new layers being 0,
and the weight of the existing layer to be 1).

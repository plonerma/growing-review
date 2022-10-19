@rusuProgressiveNeuralNetworks2016 develop *Progressive Networks* for tackling
catastrophic forgetting. The idea is to grow networks when learning new tasks.
The older parts of the networks are frozen and their function incoporated
using adapters to allow for knowledge transfer from earlier tasks.
Each time a new tasks is learned, the network is further extended (a new column
is added).


![Figure from @rusuProgressiveNeuralNetworks2016 illustrating the use of columns and adapters.](img/progressive_nn_columns){width=10cm}

GradMax focuses on the question **how** new neurons are initialized.
They propose initializing new neurons such that the gradient norm of new weights
are maximized while maintaining the models function.
By enforcing large gradient norms of the new weights, the objective function
is guaranteed to decrease in the next step of gradient descent.

When using a step size of $\frac{1}{\beta}$, the loss is upperbounded by:

$$
L(W_{new}) \le L(W) - \frac{\beta}{2} \| \nabla L (W) \|^2
$$

The maximum gradient norms are approximated using singular value decomposition
(SVD).


![Figure from @evciGradMaxGrowingNeural2022, showing the described upper bound.](img/gradmax_upper_bound){ width=10cm }


The authors note that this idea could also be utilized to select **where**
new neurons should be grown. The decision where to add new neurons could be
made by looking at the singular values (e,g, selecting the
largest or adding a neuron, once the singular value reaches a threshold).
This idea is very similar to the strategy of @wuFirefly2021 which use a very
similar technique to choose **where** to grow neurons (but use a different
initialization strategy).

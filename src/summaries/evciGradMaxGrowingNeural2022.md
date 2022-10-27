---
shorttitle: GradMax
why: NAS
when: Fixed Schedule
where: Fixed (GradMax could be adapted for this decision)
how: By maximizing the gradient of new parts using SVD
---


@evciGradMaxGrowingNeural2022 focus on the question **how** new neurons are initialized.
They propose initializing new neurons such that the gradient norm of new weights
are maximized while maintaining the models function.
By enforcing large gradient norms of the new weights, the objective function
is guaranteed to decrease in the next step of gradient descent.

When using a step size of $\frac{1}{\beta}$ on a function with a
$\beta$-Lipschitz gradient, the loss is upperbounded by:

$$
L(W_{new}) \le L(W) - \frac{\beta}{2} \| \nabla L (W) \|^2
$$

While a constant Lipschitz constant generally does not necessarily exist in
neural networks the authors use this as a motivation to assume that large
gradient norms will lead to large decreases in the loss function after the next


In GradMax, the maximum gradient norms (with some constraint) are approximated
using singular value decomposition (SVD).
The authors additionally provide experiments using optimization to produce large
gradient norms instead of using the closed-form solution of SVD. While they find
that SVD usually produces better results, it can only be used, if the activation
function returns 0 given an input of 0.

The authors note that this idea could also be utilized to select **where**
new neurons should be grown. The decision where to add new neurons could be
made by looking at the singular values (e,g, selecting the
largest or adding a neuron, once the singular value reaches a threshold).
This idea is very similar to the strategy of @wuFirefly2021 which use a very
similar technique to choose **where** to grow neurons (but use a different
initialization strategy).

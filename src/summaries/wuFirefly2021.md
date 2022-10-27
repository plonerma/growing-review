---
shorttitle: Firefly
why: NAS and CL
when: Fixed Schedule
where: Decided based on gradient information
how: Function-preserving transforms
---


@wuFirefly2021 propose alternating between training and growth steps.
In each growth step, the network is grown to be wider and deeper.
During each growth step, multiple candidate elements (neurons or layers)
are temporarily added to the network.
The contribution of each candidate part is multiplied with some step size
$\epsilon$ to maintain the original function.
By using the training data (or some portion of it), one can then calculate
how beneficial these new parts might be during future training.
@wuFirefly2021 show that by using Taylor approximation, this reduces
to looking a the gradients of these new parts.


Additionally, @wuFirefly2021 test their approach in a CL task-incremental
setting. For each task, a neuron mask is created (which can be retrieved using
the available task identifier). This allows the model to share structure while
maintaining its function on old tasks and hence to maintain a good average
accuracy even after multiple tasks have been learned.



![Figure from @wuFirefly2021 illustrating how new neurons can be added.](img/firefly_new_neurons){#fig:firefly_new_neurons width=100% }

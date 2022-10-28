---
shorttitle: Progressive Stacking
why: Accelerate pre-training
when: Fixed schedule
where: Duplicated layers added on top
how: Duplication of existing layers
---


@gongEfficientTrainingBERT2019 observe, that self-attention distributions across
different layers of well-trained BERT model typically exhibit a large degree of
similarity.
Hence, they propose starting the pre-training of BERT models with a smaller
number (3) of hidden layers. Over the course of the training, these pre-trained
layers are duplicated twice (and added on top, see *@fig:progressive_stacking)
and trained between each stacking operations in order to differentiate the layers.

By training with few layers for a large portion of the pre-training,
@gongEfficientTrainingBERT2019 can reduce the pre-training time by $\sim 35\%$
with only a small loss of performance.


![In each stacking step, the number of layers is doubled [@gongEfficientTrainingBERT2019].](img/progressive_stacking){#fig:progressive_stacking height=5cm}

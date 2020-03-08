# Neural LP

This is the implementation of Neural Logic Programming, proposed in the following paper:

[Differentiable Learning of Logical Rules for Knowledge Base Reasoning](https://arxiv.org/abs/1702.08367).
Fan Yang, Zhilin Yang, William W. Cohen.
NIPS 2017.

## Requirements (my environment)
- GeForce GTX 1660 Ti
- Windows 10 Pro. 64-bit
- Python 3.5 (since Tensorflow 1.0.1 whl file supports only cp35-cp35m-win_amd64.)
- Numpy 
- Tensorflow 1.0.1 cpu version (my GPU doen't support CUDA 8 which Tensorflow 1.0.1 supports. If your GPU support CUDA 8, the GPU version might be ok...)

## Quick start
The following command starts training a dataset about family relations, and stores the experiment results in the folder `exps/demo/`.

```
python src/main.py --datadir=datasets/family --exps_dir=exps/ --exp_name=demo
```

Wait for around 8 minutes, navigate to `exps/demo/`, there is `rules.txt` that contains learned logical rules. 

## Evaluation
To evaluate the prediction results, follow the steps below. The first two steps is preparation so that we can compute _filtered_ ranks (see [TransE](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf) for details).

We use the experiment from Quick Start as an example. Change the folder names (datasets/family, exps/dev) for other experiments.
```
python eval/collect_all_facts.py --path=datasets\\family
python eval/get_truths.py datasets/family
python eval/evaluate.py --preds=exps/demo/test_predictions.txt --truths=datasets/family/truths.pckl
```



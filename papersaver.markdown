---
layout: page
comments: false
title:  "PaperSaver"
permalink: /papersaver/
---
**Top keywords:** **`network`** (2), **`learn`** (2), **`layer`** (1), **`autoencoder`** (1), **`sentence`** (1), **`hierarchy`** (1), **`text`** (1), **`dynamic`** (1), **`lstm`** (1), **`different`** (1), **`utilize`** (1), **`rl`** (1), **`hierarchical`** (1), **`convolutional`** (1), **`generating`** (1)

___

2018 March 28 03:29AM

**Title**: [From neural PCA to deep unsupervised learning](https://arxiv.org/abs/1411.7783)

**Keywords**: `network`, `learn`, `autoencoder`, `hierarchy`, `layer`, `level`, `denoising`, `encoder`

**Abstract**:
A network supporting deep unsupervised learning is presented. The network is an autoencoder with lateral shortcut connections from the encoder to decoder at each level of the hierarchy. The lateral shortcut connections allow the higher levels of the hierarchy to focus on abstract invariant features. While standard autoencoders are analogous to latent variable models with a single layer of stochastic variables, the proposed network is analogous to hierarchical latent variables models. Learning combines denoising autoencoder and denoising sources separation frameworks. Each layer of the network contributes to the cost function a term which measures the distance of the representations produced by the encoder and the decoder. Since training signals originate from all levels of the network, all layers can learn efficiently even in deep networks. The speedup offered by cost terms from higher levels of the hierarchy and the ability to learn invariant features are demonstrated in experiments.

**Notes:**



- Submitted on 28 Nov 2014 (v1), last revised 2 Feb 2015 (this version, v2)


___

2018 March 28 03:27AM

**Title**: [A Convolutional Neural Network for Modelling Sentences](https://arxiv.org/abs/1404.2188v1)

**Keywords**: `network`, `sentence`, `convolutional`, `dcnn`, `pooling`, `sentiment prediction`, `dynamic`, `task`

**Abstract**:
The ability to accurately represent sentences is central to language understanding. We describe a convolutional architecture dubbed the Dynamic Convolutional Neural Network (DCNN) that we adopt for the semantic modelling of sentences. The network uses Dynamic k-Max Pooling, a global pooling operation over linear sequences. The network handles input sentences of varying length and induces a feature graph over the sentence that is capable of explicitly capturing short and long-range relations. The network does not rely on a parse tree and is easily applicable to any language. We test the DCNN in four experiments: small scale binary and multi-class sentiment prediction, six-way question classification and Twitter sentiment prediction by distant supervision. The network achieves excellent performance in the first three tasks and a greater than 25% error reduction in the last task with respect to the strongest baseline.

**Notes:**



- Submitted on 8 Apr 2014


___

2018 March 28 03:21AM

**Title**: [A Hierarchical Neural Autoencoder for Paragraphs and Documents](https://arxiv.org/abs/1506.01057)

**Keywords**: `paragraph`, `model`, `embedding`, `coherence`, `reconstruct`, `generating`, `text`, `lstm`

**Abstract**:
Natural language generation of coherent long texts like paragraphs or longer documents is a challenging problem for recurrent networks models. In this paper, we explore an important step toward this generation task: training an LSTM (Long-short term memory) auto-encoder to preserve and reconstruct multi-sentence paragraphs. We introduce an LSTM model that hierarchically builds an embedding for a paragraph from embeddings for sentences and words, then decodes this embedding to reconstruct the original paragraph. We evaluate the reconstructed paragraph using standard metrics like ROUGE and Entity Grid, showing that neural models are able to encode texts in a way that preserve syntactic, semantic, and discourse coherence. While only a first step toward generating coherent text units from neural models, our work has the potential to significantly impact natural language generation and summarization\footnote{Code for the three models described in this paper can be found at www.stanford.edu/~jiweil/ .

**Notes:**



- 6 Jun 2015


___

2018 March 28 02:31AM

**Title**: [Hierarchical Imitation and Reinforcement Learning](https://arxiv.org/abs/1803.00590)

**Keywords**: `learn`, `hierarchical`, `framework`, `different`, `rl`, `utilize`, `horizon`, `demonstrate`

**Abstract**:
We study the problem of learning policies over long time horizons. We present a framework that leverages and integrates two key concepts. First, we utilize hierarchical policy classes that enable planning over different time scales, i.e., the high level planner proposes a sequence of subgoals for the low level planner to achieve. Second, we utilize expert demonstrations within the hierarchical action space to dramatically reduce cost of exploration. Our framework is flexible and can incorporate different combinations of imitation learning (IL) and reinforcement learning (RL) at different levels of the hierarchy. Using long-horizon benchmarks, including Montezuma's Revenge, we empirically demonstrate that our approach can learn significantly faster compared to hierarchical RL, and can be significantly more label- and sample-efficient compared to flat IL. We also provide theoretical analysis of the labeling cost for certain instantiations of our framework.

**Notes:**



- a hierarchical imitation learning framework that exploits two levels of hierarchy to effectively learn over long time horizons

---
layout: page
comments: false
title:  "PaperSaver"
permalink: /papersaver/
---
**Top keywords:** **`learn`** (8), **`network`** (5), **`model`** (5), **`neural`** (4), **`approach`** (3), **`rnn`** (2), **`rl`** (2), **`architecture`** (2), **`trained`** (2), **`memory`** (2), **`convolutional`** (2), **`demonstrate`** (2), **`models`** (2), **`representations`** (2), **`task`** (2)

___

**(#1) Title:** [Strategic Attentive Writer for Learning Macro-Actions](https://arxiv.org/abs/1606.04695) (added 2018 March 28 04:53AM)

**Meta:** Alexander (Sasha) Vezhnevets, Volodymyr Mnih, John Agapiou, Simon Osindero, Alex Graves, Oriol Vinyals, Koray Kavukcuoglu, Submitted on 15 Jun 2016

**Keywords:** `learn`, `plan`, `straw`, `macro actions`, `temporally`, `prediction`, `demonstrate`, `end`

**Abstract:** We present a novel deep recurrent neural network architecture that learns to build implicit plans in an end-to-end manner by purely interacting with an environment in reinforcement learning setting. The network builds an internal plan, which is continuously updated upon observation of the next input from the environment. It can also partition this internal representation into contiguous sub- sequences by learning for how long the plan can be committed to - i.e. followed without re-planing. Combining these properties, the proposed model, dubbed STRategic Attentive Writer (STRAW) can learn high-level, temporally abstracted macro- actions of varying lengths that are solely learnt from data without any prior information. These macro-actions enable both structured exploration and economic computation. We experimentally demonstrate that STRAW delivers strong improvements on several ATARI games by employing temporally extended planning strategies (e.g. Ms. Pacman and Frostbite). It is at the same time a general algorithm that can be applied on any sequence data. To that end, we also show that when trained on text prediction task, STRAW naturally predicts frequent n-grams (instead of macro-actions), demonstrating the generality of the approach.

___

**(#2) Title:** [Pointer Networks](https://arxiv.org/abs/1506.03134) (added 2018 March 28 04:28AM)

**Meta:** Oriol Vinyals, Meire Fortunato, Navdeep Jaitly, Submitted on 9 Jun 2015 (v1), last revised 2 Jan 2017 (this version, v2)

**Keywords:** `sequence`, `problem`, `attention`, `neural`, `ptr net`, `input`, `output`, `learn`

**Abstract:** We introduce a new neural architecture to learn the conditional probability of an output sequence with elements that are discrete tokens corresponding to positions in an input sequence. Such problems cannot be trivially addressed by existent approaches such as sequence-to-sequence and Neural Turing Machines, because the number of target classes in each step of the output depends on the length of the input, which is variable. Problems such as sorting variable sized sequences, and various combinatorial optimization problems belong to this class. Our model solves the problem of variable size output dictionaries using a recently proposed mechanism of neural attention. It differs from the previous attention attempts in that, instead of using attention to blend hidden units of an encoder to a context vector at each decoder step, it uses attention as a pointer to select a member of the input sequence as the output. We call this architecture a Pointer Net (Ptr-Net). We show Ptr-Nets can be used to learn approximate solutions to three challenging geometric problems -- finding planar convex hulls, computing Delaunay triangulations, and the planar Travelling Salesman Problem -- using training examples alone. Ptr-Nets not only improve over sequence-to-sequence with input attention, but also allow us to generalize to variable size output dictionaries. We show that the learnt models generalize beyond the maximum lengths they were trained on. We hope our results on these tasks will encourage a broader exploration of neural learning for discrete problems.

___

**(#3) Title:** [On Learning to Think: Algorithmic Information Theory for Novel Combinations of Reinforcement Learning Controllers and Recurrent Neural World Models](https://arxiv.org/abs/1511.09249) (added 2018 March 28 04:23AM)

**Meta:** Submitted on 30 Nov 2015

**Keywords:** `learn`, `rnnai`, `model`, `rnn based`, `rl`, `rnn`, `abstract`, `reasoning`

**Abstract:** This paper addresses the general problem of reinforcement learning (RL) in partially observable environments. In 2013, our large RL recurrent neural networks (RNNs) learned from scratch to drive simulated cars from high-dimensional video input. However, real brains are more powerful in many ways. In particular, they learn a predictive model of their initially unknown environment, and somehow use it for abstract (e.g., hierarchical) planning and reasoning. Guided by algorithmic information theory, we describe RNN-based AIs (RNNAIs) designed to do the same. Such an RNNAI can be trained on never-ending sequences of tasks, some of them provided by the user, others invented by the RNNAI itself in a curious, playful fashion, to improve its RNN-based world model. Unlike our previous model-building RNN-based RL machines dating back to 1990, the RNNAI learns to actively query its model for abstract reasoning and planning and decision making, essentially "learning to think." The basic ideas of this report can be applied to many other cases where one RNN-like system exploits the algorithmic information content of another. They are taken from a grant proposal submitted in Fall 2014, and also explain concepts such as "mirror neurons." Experimental results will be described in separate papers.

___

**(#4) Title:** [On the Expressive Power of Deep Neural Networks](https://arxiv.org/abs/1606.05336v6) (added 2018 March 28 04:22AM)

**Meta:** Submitted on 16 Jun 2016 (v1), last revised 18 Jun 2017 (this version, v6)

**Keywords:** `network`, `expressivity`, `regularization`, `trajectory`, `compute`, `weights`, `trajectory length`, `neural network`

**Abstract:** We propose a new approach to the problem of neural network expressivity, which seeks to characterize how structural properties of a neural network family affect the functions it is able to compute. Our approach is based on an interrelated set of measures of expressivity, unified by the novel notion of trajectory length, which measures how the output of a network changes as the input sweeps along a one-dimensional path. Our findings can be summarized as follows: 
(1) The complexity of the computed function grows exponentially with depth. 
(2) All weights are not equal: trained networks are more sensitive to their lower (initial) layer weights. 
(3) Regularizing on trajectory length (trajectory regularization) is a simpler alternative to batch normalization, with the same performance.

___

**(#5) Title:** [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357) (added 2018 March 28 04:20AM)

**Meta:** Submitted on 7 Oct 2016 (v1), last revised 4 Apr 2017 (this version, v3)

**Keywords:** `convolution`, `inception v3`, `inception`, `depthwise separable convolution`, `inception module`, `architecture`, `outperforms inception`, `xception`

**Abstract:** We present an interpretation of Inception modules in convolutional neural networks as being an intermediate step in-between regular convolution and the depthwise separable convolution operation (a depthwise convolution followed by a pointwise convolution). In this light, a depthwise separable convolution can be understood as an Inception module with a maximally large number of towers. This observation leads us to propose a novel deep convolutional neural network architecture inspired by Inception, where Inception modules have been replaced with depthwise separable convolutions. We show that this architecture, dubbed Xception, slightly outperforms Inception V3 on the ImageNet dataset (which Inception V3 was designed for), and significantly outperforms Inception V3 on a larger image classification dataset comprising 350 million images and 17,000 classes. Since the Xception architecture has the same number of parameters as Inception V3, the performance gains are not due to increased capacity but rather to a more efficient use of model parameters.

___

**(#6) Title:** [Reasoning with Memory Augmented Neural Networks for Language Comprehension](https://arxiv.org/abs/1610.06454v2) (added 2018 March 28 04:18AM)

**Meta:** Submitted on 20 Oct 2016 (v1), last revised 28 Feb 2017 (this version, v2)

**Keywords:** `hypothesis test`, `approach`, `test`, `nse`, `comprehension`, `neural`, `hypothesis`, `previous`

**Abstract:** Hypothesis testing is an important cognitive process that supports human reasoning. In this paper, we introduce a computational hypothesis testing approach based on memory augmented neural networks. Our approach involves a hypothesis testing loop that reconsiders and progressively refines a previously formed hypothesis in order to generate new hypotheses to test. We apply the proposed approach to language comprehension task by using Neural Semantic Encoders (NSE). Our NSE models achieve the state-of-the-art results showing an absolute improvement of 1.2% to 2.6% accuracy over previous results obtained by single and ensemble systems on standard machine comprehension benchmarks such as the Children's Book Test (CBT) and Who-Did-What (WDW) news article datasets.

___

**(#7) Title:** [Neural Networks with Few Multiplications](https://arxiv.org/abs/1510.03009) (added 2018 March 28 04:05AM)

**Meta:** Submitted on 11 Oct 2015 (v1), last revised 26 Feb 2016 (this version, v3)

**Keywords:** `training`, `multiplications`, `binarize`, `stochastic`, `computation`, `weights`, `neural networks`, `convert`

**Abstract:** For most deep learning algorithms training is notoriously time consuming. Since most of the computation in training neural networks is typically spent on floating point multiplications, we investigate an approach to training that eliminates the need for most of these. Our method consists of two parts: First we stochastically binarize weights to convert multiplications involved in computing hidden states to sign changes. Second, while back-propagating error derivatives, in addition to binarizing the weights, we quantize the representations at each layer to convert the remaining multiplications into binary shifts. Experimental results across 3 popular datasets (MNIST, CIFAR10, SVHN) show that this approach not only does not hurt classification performance but can result in even better performance than standard stochastic gradient descent training, paving the way to fast, hardware-friendly training of neural networks.

___

**(#8) Title:** [Memory Networks](https://arxiv.org/abs/1410.3916) (added 2018 March 28 04:04AM)

**Meta:** Submitted on 15 Oct 2014 (v1), last revised 29 Nov 2015 (this version, v11)

**Keywords:** `models`, `long term memory`, `qa`, `component`, `learn`, `memory networks`, `task`, `memory`

**Abstract:** We describe a new class of learning models called memory networks. Memory networks reason with inference components combined with a long-term memory component; they learn how to use these jointly. The long-term memory can be read and written to, with the goal of using it for prediction. We investigate these models in the context of question answering (QA) where the long-term memory effectively acts as a (dynamic) knowledge base, and the output is a textual response. We evaluate them on a large-scale QA task, and a smaller, but more complex, toy task generated from a simulated world. In the latter, we show the reasoning power of such models by chaining multiple supporting sentences to answer questions that require understanding the intension of verbs.

___

**(#9) Title:** [InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets](https://arxiv.org/abs/1606.03657) (added 2018 March 28 04:03AM)

**Meta:** Submitted on 12 Jun 2016

**Keywords:** `infogan`, `dataset`, `representations`, `digit`, `learn`, `disentangled`, `interpretable`, `generative adversarial`

**Abstract:** This paper describes InfoGAN, an information-theoretic extension to the Generative Adversarial Network that is able to learn disentangled representations in a completely unsupervised manner. InfoGAN is a generative adversarial network that also maximizes the mutual information between a small subset of the latent variables and the observation. We derive a lower bound to the mutual information objective that can be optimized efficiently, and show that our training procedure can be interpreted as a variation of the Wake-Sleep algorithm. Specifically, InfoGAN successfully disentangles writing styles from digit shapes on the MNIST dataset, pose from lighting of 3D rendered images, and background digits from the central digit on the SVHN dataset. It also discovers visual concepts that include hair styles, presence/absence of eyeglasses, and emotions on the CelebA face dataset. Experiments show that InfoGAN learns interpretable representations that are competitive with representations learned by existing fully supervised methods.

___

**(#10) Title:** [On Multiplicative Integration with Recurrent Neural Networks](https://arxiv.org/abs/1606.06630) (added 2018 March 28 03:59AM)

**Meta:** Submitted on 21 Jun 2016 (v1), last revised 12 Nov 2016 (this version, v2)

**Keywords:** `rnn models`, `rnn`, `multiplicative integrated`, `introduce`, `structural`, `integrated`, `mi`, `difference`

**Abstract:** We introduce a general and simple structural design called Multiplicative Integration (MI) to improve recurrent neural networks (RNNs). MI changes the way in which information from difference sources flows and is integrated in the computational building block of an RNN, while introducing almost no extra parameters. The new structure can be easily embedded into many popular RNN models, including LSTMs and GRUs. We empirically analyze its learning behaviour and conduct evaluations on several tasks using different RNN models. Our experimental results demonstrate that Multiplicative Integration can provide a substantial performance boost over many of the existing RNN models.

___

**(#11) Title:** [Stacked Hourglass Networks for Human Pose Estimation](https://arxiv.org/abs/1603.06937v2) (added 2018 March 28 03:55AM)

**Meta:** Submitted on 22 Mar 2016 (v1), last revised 26 Jul 2016 (this version, v2)

**Keywords:** `network`, `processed`, `architecture`, `mpii`, `outcompeting`, `convolutional`, `upsampling`, `flic`

**Abstract:** This work introduces a novel convolutional network architecture for the task of human pose estimation. Features are processed across all scales and consolidated to best capture the various spatial relationships associated with the body. We show how repeated bottom-up, top-down processing used in conjunction with intermediate supervision is critical to improving the performance of the network. We refer to the architecture as a "stacked hourglass" network based on the successive steps of pooling and upsampling that are done to produce a final set of predictions. State-of-the-art results are achieved on the FLIC and MPII benchmarks outcompeting all recent methods.

___

**(#12) Title:** [Learning to Understand Phrases by Embedding the Dictionary](https://arxiv.org/abs/1504.00548) (added 2018 March 28 03:50AM)

**Meta:** Submitted on 2 Apr 2015 (v1), last revised 22 Mar 2016 (this version, v4)

**Keywords:** `definition`, `lexical`, `dictionaries`, `representations`, `phrases`, `trained`, `models`, `architectures`

**Abstract:** Distributional models that learn rich semantic word representations are a success story of recent NLP research. However, developing models that learn useful representations of phrases and sentences has proved far harder. We propose using the definitions found in everyday dictionaries as a means of bridging this gap between lexical and phrasal semantics. Neural language embedding models can be effectively trained to map dictionary definitions (phrases) to (lexical) representations of the words defined by those definitions. We present two applications of these architectures: "reverse dictionaries" that return the name of a concept given a definition or description and general-knowledge crossword question answerers. On both tasks, neural language embedding models trained on definitions from a handful of freely-available lexical resources perform as well or better than existing commercial systems that rely on significant task-specific engineering. The results highlight the effectiveness of both neural embedding architectures and definition-based training for developing models that understand phrases and sentences.

___

**(#13) Title:** [End-To-End Memory Networks](https://arxiv.org/abs/1503.08895) (added 2018 March 28 03:49AM)

**Meta:** Submitted on 31 Mar 2015 (v1), last revised 24 Nov 2015 (this version, v5)

**Keywords:** `model`, `hops`, `multiple computational`, `trained`, `less supervision`, `memory`, `approach`, `memory network`

**Abstract:** We introduce a neural network with a recurrent attention model over a possibly large external memory. The architecture is a form of Memory Network (Weston et al., 2015) but unlike the model in that work, it is trained end-to-end, and hence requires significantly less supervision during training, making it more generally applicable in realistic settings. It can also be seen as an extension of RNNsearch to the case where multiple computational steps (hops) are performed per output symbol. The flexibility of the model allows us to apply it to tasks as diverse as (synthetic) question answering and to language modeling. For the former our approach is competitive with Memory Networks, but with less supervision. For the latter, on the Penn TreeBank and Text8 datasets our approach demonstrates comparable performance to RNNs and LSTMs. In both cases we show that the key concept of multiple computational hops yields improved results.

___

**(#14) Title:** [Neural Language Correction with Character-Based Attention](https://arxiv.org/abs/1603.09727v1) (added 2018 March 28 03:46AM)

**Meta:** Submitted on 31 Mar 2016

**Keywords:** `error`, `approach`, `method`, `network`, `language`, `learner`, `flexibility`, `neural`

**Abstract:** Natural language correction has the potential to help language learners improve their writing skills. While approaches with separate classifiers for different error types have high precision, they do not flexibly handle errors such as redundancy or non-idiomatic phrasing. On the other hand, word and phrase-based machine translation methods are not designed to cope with orthographic errors, and have recently been outpaced by neural models. Motivated by these issues, we present a neural network-based approach to language correction. The core component of our method is an encoder-decoder recurrent neural network with an attention mechanism. By operating at the character level, the network avoids the problem of out-of-vocabulary words. We illustrate the flexibility of our approach on dataset of noisy, user-generated text collected from an English learner forum. When combined with a language model, our method achieves a state-of-the-art F0.5-score on the CoNLL 2014 Shared Task. We further demonstrate that training the network on additional data with synthesized errors can improve performance.

___

**(#15) Title:** [Masked Autoregressive Flow for Density Estimation](https://arxiv.org/abs/1705.07057) (added 2018 March 28 03:40AM)

**Meta:** last revised 11 Jan 2018 (this version, v3)

**Keywords:** `model`, `autoregressive model`, `autoregressive flow`, `density estimation`, `flow`, `masked autoregressive`, `stack`, `random numbers`

**Abstract:** Autoregressive models are among the best performing neural density estimators. We describe an approach for increasing the flexibility of an autoregressive model, based on modelling the random numbers that the model uses internally when generating data. By constructing a stack of autoregressive models, each modelling the random numbers of the next model in the stack, we obtain a type of normalizing flow suitable for density estimation, which we call Masked Autoregressive Flow. This type of flow is closely related to Inverse Autoregressive Flow and is a generalization of Real NVP. Masked Autoregressive Flow achieves state-of-the-art performance in a range of general-purpose density estimation tasks.

___

**(#16) Title:** [Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937) (added 2018 March 28 03:37AM)

**Meta:** Submitted on 2 Nov 2017

**Keywords:** `representation`, `learn`, `model`, `vae`, `vq`, `discrete`, `vector quantisation`, `autoregressive`

**Abstract:** Learning useful representations without supervision remains a key challenge in machine learning. In this paper, we propose a simple yet powerful generative model that learns such discrete representations. Our model, the Vector Quantised-Variational AutoEncoder (VQ-VAE), differs from VAEs in two key ways: the encoder network outputs discrete, rather than continuous, codes; and the prior is learnt rather than static. In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ). Using the VQ method allows the model to circumvent issues of "posterior collapse" -- where the latents are ignored when they are paired with a powerful autoregressive decoder -- typically observed in the VAE framework. Pairing these representations with an autoregressive prior, the model can generate high quality images, videos, and speech as well as doing high quality speaker conversion and unsupervised learning of phonemes, providing further evidence of the utility of the learnt representations.

___

**(#17) Title:** [Deep Voice 3: Scaling Text-to-Speech with Convolutional Sequence Learning](https://arxiv.org/abs/1710.07654v3) (added 2018 March 28 03:36AM)

**Meta:** last revised 22 Feb 2018 (this version, v3)

**Keywords:** `deep voice 3`, `tts`, `neural`, `synthesis`, `speech synthesis`, `speech`, `scale`, `ten`

**Abstract:** We present Deep Voice 3, a fully-convolutional attention-based neural text-to-speech (TTS) system. Deep Voice 3 matches state-of-the-art neural speech synthesis systems in naturalness while training ten times faster. We scale Deep Voice 3 to data set sizes unprecedented for TTS, training on more than eight hundred hours of audio from over two thousand speakers. In addition, we identify common error modes of attention-based speech synthesis networks, demonstrate how to mitigate them, and compare several different waveform synthesis methods. We also describe how to scale inference to ten million queries per day on one single-GPU server.

___

**(#18) Title:** [From neural PCA to deep unsupervised learning](https://arxiv.org/abs/1411.7783) (added 2018 March 28 03:29AM)

**Meta:** Submitted on 28 Nov 2014 (v1), last revised 2 Feb 2015 (this version, v2)

**Keywords:** `network`, `learn`, `autoencoder`, `hierarchy`, `layer`, `level`, `denoising`, `encoder`

**Abstract:** A network supporting deep unsupervised learning is presented. The network is an autoencoder with lateral shortcut connections from the encoder to decoder at each level of the hierarchy. The lateral shortcut connections allow the higher levels of the hierarchy to focus on abstract invariant features. While standard autoencoders are analogous to latent variable models with a single layer of stochastic variables, the proposed network is analogous to hierarchical latent variables models. Learning combines denoising autoencoder and denoising sources separation frameworks. Each layer of the network contributes to the cost function a term which measures the distance of the representations produced by the encoder and the decoder. Since training signals originate from all levels of the network, all layers can learn efficiently even in deep networks. The speedup offered by cost terms from higher levels of the hierarchy and the ability to learn invariant features are demonstrated in experiments.

___

**(#19) Title:** [A Convolutional Neural Network for Modelling Sentences](https://arxiv.org/abs/1404.2188v1) (added 2018 March 28 03:27AM)

**Meta:** Submitted on 8 Apr 2014

**Keywords:** `network`, `sentence`, `convolutional`, `dcnn`, `pooling`, `sentiment prediction`, `dynamic`, `task`

**Abstract:** The ability to accurately represent sentences is central to language understanding. We describe a convolutional architecture dubbed the Dynamic Convolutional Neural Network (DCNN) that we adopt for the semantic modelling of sentences. The network uses Dynamic k-Max Pooling, a global pooling operation over linear sequences. The network handles input sentences of varying length and induces a feature graph over the sentence that is capable of explicitly capturing short and long-range relations. The network does not rely on a parse tree and is easily applicable to any language. We test the DCNN in four experiments: small scale binary and multi-class sentiment prediction, six-way question classification and Twitter sentiment prediction by distant supervision. The network achieves excellent performance in the first three tasks and a greater than 25% error reduction in the last task with respect to the strongest baseline.

___

**(#20) Title:** [A Hierarchical Neural Autoencoder for Paragraphs and Documents](https://arxiv.org/abs/1506.01057) (added 2018 March 28 03:21AM)

**Meta:** 6 Jun 2015

**Keywords:** `paragraph`, `model`, `embedding`, `coherence`, `reconstruct`, `generating`, `text`, `lstm`

**Abstract:** Natural language generation of coherent long texts like paragraphs or longer documents is a challenging problem for recurrent networks models. In this paper, we explore an important step toward this generation task: training an LSTM (Long-short term memory) auto-encoder to preserve and reconstruct multi-sentence paragraphs. We introduce an LSTM model that hierarchically builds an embedding for a paragraph from embeddings for sentences and words, then decodes this embedding to reconstruct the original paragraph. We evaluate the reconstructed paragraph using standard metrics like ROUGE and Entity Grid, showing that neural models are able to encode texts in a way that preserve syntactic, semantic, and discourse coherence. While only a first step toward generating coherent text units from neural models, our work has the potential to significantly impact natural language generation and summarization\footnote{Code for the three models described in this paper can be found at www.stanford.edu/~jiweil/ .

___

**(#21) Title:** [Hierarchical Imitation and Reinforcement Learning](https://arxiv.org/abs/1803.00590) (added 2018 March 28 02:31AM)

**Keywords:** `learn`, `hierarchical`, `framework`, `different`, `rl`, `utilize`, `horizon`, `demonstrate`

**Abstract:** We study the problem of learning policies over long time horizons. We present a framework that leverages and integrates two key concepts. First, we utilize hierarchical policy classes that enable planning over different time scales, i.e., the high level planner proposes a sequence of subgoals for the low level planner to achieve. Second, we utilize expert demonstrations within the hierarchical action space to dramatically reduce cost of exploration. Our framework is flexible and can incorporate different combinations of imitation learning (IL) and reinforcement learning (RL) at different levels of the hierarchy. Using long-horizon benchmarks, including Montezuma's Revenge, we empirically demonstrate that our approach can learn significantly faster compared to hierarchical RL, and can be significantly more label- and sample-efficient compared to flat IL. We also provide theoretical analysis of the labeling cost for certain instantiations of our framework.

**Notes:**



- a hierarchical imitation learning framework that exploits two levels of hierarchy to effectively learn over long time horizons

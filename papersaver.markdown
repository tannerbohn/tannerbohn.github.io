---
layout: page
comments: false
title:  "PaperSaver"
permalink: /papersaver/
---
**Top keywords:** **`model`** (16), **`learn`** (12), **`neural`** (8), **`approach`** (6), **`network`** (5), **`sentence`** (4), **`sequence`** (4), **`learning`** (4), **`trained`** (4), **`word`** (4), **`models`** (4), **`semantic`** (3), **`text`** (3), **`rnn`** (3), **`rl`** (3)

___

**(#50) Title:** [From Word Embeddings To Document Distances](http://www.cs.cornell.edu/~kilian/papers/wmd_metric.pdf) (added 2018 March 28 09:57PM)

**Meta:** Matt J. Kusner, Yu Sun, Nicholas I. Kolkin, Kilian Q. Weinberger, Proceedings of the 32 nd International Conference on Machine Learning, Lille, France, 2015

**Keywords:** `distance`, `document`, `word`, `wmd`, `metric`, `movers distance`, `embedded`, `document classification`

**Abstract:** We present the Word Movers Distance (WMD),
a novel distance function between text documents.
Our work is based on recent results in
word embeddings that learn semantically meaningful
representations for words from local cooccurrences
in sentences. The WMD distance
measures the dissimilarity between two text documents
as the minimum amount of distance that
the embedded words of one document need to
travel to reach the embedded words of another
document. We show that this distance metric can
be cast as an instance of the Earth Movers Distance,
a well studied transportation problem for
which several highly efficient solvers have been
developed. Our metric has no hyperparameters
and is straight-forward to implement. Further, we
demonstrate on eight real world document classification
data sets, in comparison with seven stateof-the-art
baselines, that the WMD metric leads
to unprecedented low k-nearest neighbor document
classification error rates.

___

**(#49) Title:** [The Transition to Minimal Consciousness through the Evolution of Associative Learning](https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01954/full) (added 2018 March 28 09:53PM)

**Meta:** 22 December 2016

**Keywords:** `sentience`, `consciousness`, `ual`, `minimal consciousness`, `minimal`, `proposal`, `learning`, `function`

**Abstract:** The minimal state of consciousness is sentience. This includes any phenomenal sensory experience  exteroceptive, such as vision and olfaction; interoceptive, such as pain and hunger; or proprioceptive, such as the sense of bodily position and movement. We propose unlimited associative learning (UAL) as the marker of the evolutionary transition to minimal consciousness (or sentience), its phylogenetically earliest sustainable manifestation and the driver of its evolution. We define and describe UAL at the behavioral and functional level and argue that the structural-anatomical implementations of this mode of learning in different taxa entail subjective feelings (sentience). We end with a discussion of the implications of our proposal for the distribution of consciousness in the animal kingdom, suggesting testable predictions, and revisiting the ongoing debate about the function of minimal consciousness in light of our approach.

___

**(#48) Title:** [OUT-OF-CLASS NOVELTY GENERATION: AN EXPERIMENTAL FOUNDATION](https://openreview.net/pdf?id=ByEPMj5el) (added 2018 March 28 04:35PM)

**Meta:** Mehdi Cherti & Balazs K   egl, Akn Kazakc , Under review as a conference paper at ICLR 2017

**Keywords:** `generate`, `creativity`, `model`, `classes`, `machine learning`, `novelty`, `evaluating`, `distribution novelty`

**Abstract:** Recent advances in machine learning have brought the field closer to computational
creativity research. From a creativity research point of view, this offers the
potential to study creativity in relationship with knowledge acquisition. From a
machine learning perspective, however, several aspects of creativity need to be
better defined to allow the machine learning community to develop and test hypotheses
in a systematic way. We propose an actionable definition of creativity as
the generation of out-of-distribution novelty. We assess several metrics designed
for evaluating the quality of generative models on this new task. We also propose
a new experimental setup. Inspired by the usual held-out validation, we hold out
entire classes for evaluating the generative potential of models. The goal of the
novelty generator is then to use training classes to build a model that can generate
objects from future (hold-out) classes, unknown at training time - and thus, are
novel with respect to the knowledge the model incorporates. Through extensive
experiments on various types of generative models, we are able to find architectures
and hyperparameter combinations which lead to out-of-distribution novelty.

___

**(#47) Title:** [TOWARDS AN AUTOMATIC TURING TEST: LEARNING TO EVALUATE DIALOGUE RESPONSES](https://openreview.net/pdf?id=HJ5PIaseg) (added 2018 March 28 04:32PM)

**Meta:** Under review as a conference paper at ICLR 2017, Ryan Lowe Michael Noseworthy Iulian V. Serban Nicolas Angelard-Gontier Yoshua Bengio Joelle Pineau

**Keywords:** `evaluating`, `response`, `model`, `human`, `adem`, `automatic evaluating`, `dialogue`, `correlate`

**Abstract:** Automatically evaluating the quality of dialogue responses for unstructured domains
is a challenging problem. Unfortunately, existing automatic evaluation
metrics are biased and correlate very poorly with human judgements of response
quality (Liu et al., 2016). Yet having an accurate automatic evaluation procedure
is crucial for dialogue research, as it allows rapid prototyping and testing of new
models with fewer expensive human evaluations. In response to this challenge, we
formulate automatic dialogue evaluation as a learning problem. We present an evaluation
model (ADEM) that learns to predict human-like scores to input responses,
using a new dataset of human response scores. We show that the ADEM models
predictions correlate significantly, and at level much higher than word-overlap metrics
such as BLEU, with human judgements at both the utterance and system-level.
We also show that ADEM can generalize to evaluating dialogue models unseen
during training, an important step for automatic dialogue evaluation

___

**(#46) Title:** [Learning to Skim Text](https://arxiv.org/abs/1704.06877) (added 2018 March 28 04:12PM)

**Meta:** Adams Wei Yu, Hongrae Lee, Quoc V. Le, (Submitted on 23 Apr 2017 (v1), last revised 29 Apr 2017 (this version, v2))

**Keywords:** `read`, `model`, `recurrent`, `jump`, `word`, `text`, `lstm`, `promise`

**Abstract:** Recurrent Neural Networks are showing much promise in many sub-areas of natural language processing, ranging from document classification to machine translation to automatic question answering. Despite their promise, many recurrent models have to read the whole text word by word, making it slow to handle long documents. For example, it is difficult to use a recurrent network to read a book and answer questions about it. In this paper, we present an approach of reading text while skipping irrelevant information if needed. The underlying model is a recurrent network that learns how far to jump after reading a few words of the input text. We employ a standard policy gradient method to train the model to make discrete jumping decisions. In our benchmarks on four different tasks, including number prediction, sentiment analysis, news article classification and automatic Q\&A, our proposed model, a modified LSTM with jumping, is up to 6 times faster than the standard sequential LSTM, while maintaining the same or even better accuracy.

___

**(#45) Title:** [Neural Optimizer Search with Reinforcement Learning](https://arxiv.org/abs/1709.07417) (added 2018 March 28 04:11PM)

**Meta:** Irwan Bello, Barret Zoph, Vijay Vasudevan, Quoc V. Le, (Submitted on 21 Sep 2017 (v1), last revised 22 Sep 2017 (this version, v2))

**Keywords:** `optimization`, `train`, `architectures`, `gradient`, `neural`, `discovering`, `controller`, `update`

**Abstract:** We present an approach to automate the process of discovering optimization methods, with a focus on deep learning architectures. We train a Recurrent Neural Network controller to generate a string in a domain specific language that describes a mathematical update equation based on a list of primitive functions, such as the gradient, running average of the gradient, etc. The controller is trained with Reinforcement Learning to maximize the performance of a model after a few epochs. On CIFAR-10, our method discovers several update rules that are better than many commonly used optimizers, such as Adam, RMSProp, or SGD with and without Momentum on a ConvNet model. We introduce two new optimizers, named PowerSign and AddSign, which we show transfer well and improve training on a variety of different tasks and architectures, including ImageNet classification and Google's neural machine translation system.

___

**(#44) Title:** [Searching for Activation Functions](https://arxiv.org/abs/1710.05941) (added 2018 March 28 04:10PM)

**Meta:** Prajit Ramachandran, Barret Zoph, Quoc V. Le, (Submitted on 16 Oct 2017 (v1), last revised 27 Oct 2017 (this version, v2))

**Keywords:** `activation function`, `relu`, `swish`, `search`, `swish unit`, `replace relus`, `discover activation`, `discover`

**Abstract:** The choice of activation functions in deep networks has a significant effect on the training dynamics and task performance. Currently, the most successful and widely-used activation function is the Rectified Linear Unit (ReLU). Although various hand-designed alternatives to ReLU have been proposed, none have managed to replace it due to inconsistent gains. In this work, we propose to leverage automatic search techniques to discover new activation functions. Using a combination of exhaustive and reinforcement learning-based search, we discover multiple novel activation functions. We verify the effectiveness of the searches by conducting an empirical evaluation with the best discovered activation function. Our experiments show that the best discovered activation function, f(x)=xsigmoid(x), which we name Swish, tends to work better than ReLU on deeper models across a number of challenging datasets. For example, simply replacing ReLUs with Swish units improves top-1 classification accuracy on ImageNet by 0.9\% for Mobile NASNet-A and 0.6\% for Inception-ResNet-v2. The simplicity of Swish and its similarity to ReLU make it easy for practitioners to replace ReLUs with Swish units in any neural network.

___

**(#43) Title:** [A Neural Conversational Model](https://arxiv.org/abs/1506.05869) (added 2018 March 28 04:00PM)

**Meta:** Oriol Vinyals, Quoc Le, (Submitted on 19 Jun 2015 (v1), last revised 22 Jul 2015 (this version, v3))

**Keywords:** `conversation`, `model`, `dataset`, `domain`, `sentence`, `simple`, `find`, `noisy`

**Abstract:** Conversational modeling is an important task in natural language understanding and machine intelligence. Although previous approaches exist, they are often restricted to specific domains (e.g., booking an airline ticket) and require hand-crafted rules. In this paper, we present a simple approach for this task which uses the recently proposed sequence to sequence framework. Our model converses by predicting the next sentence given the previous sentence or sentences in a conversation. The strength of our model is that it can be trained end-to-end and thus requires much fewer hand-crafted rules. We find that this straightforward model can generate simple conversations given a large conversational training dataset. Our preliminary results suggest that, despite optimizing the wrong objective function, the model is able to converse well. It is able extract knowledge from both a domain specific dataset, and from a large, noisy, and general domain dataset of movie subtitles. On a domain-specific IT helpdesk dataset, the model can find a solution to a technical problem via conversations. On a noisy open-domain movie transcript dataset, the model can perform simple forms of common sense reasoning. As expected, we also find that the lack of consistency is a common failure mode of our model.

___

**(#42) Title:** [Neural Models for Key Phrase Detection and Question Generation](https://arxiv.org/abs/1706.04560v2) (added 2018 March 28 04:07PM)

**Meta:** Sandeep Subramanian, Tong Wang, Xingdi Yuan, Saizheng Zhang, Adam Trischler, Yoshua Bengio, (Submitted on 14 Jun 2017 (v1), last revised 14 Sep 2017 (this version, v2))

**Keywords:** `model`, `sequence`, `key phrase`, `approach`, `answer`, `question generated`, `question`, `neural`

**Abstract:** We propose a two-stage neural model to tackle question generation from documents. Our model first estimates the probability that word sequences in a document compose "interesting" answers using a neural model trained on a question-answering corpus. We thus take a data-driven approach to interestingness. Predicted key phrases then act as target answers that condition a sequence-to-sequence question generation model with a copy mechanism. Empirically, our neural key phrase detection model significantly outperforms an entity-tagging baseline system and existing rule-based approaches. We demonstrate that the question generator formulates good quality natural language questions from extracted key phrases, and a human study indicates that our system's generated question-answer pairs are competitive with those of an earlier approach. We foresee our system being used in an educational setting to assess reading comprehension and also as a data augmentation technique for semi-supervised learning.

___

**(#41) Title:** [sense2vec - A Fast and Accurate Method for Word Sense Disambiguation In Neural Word Embeddings](https://arxiv.org/abs/1511.06388) (added 2018 March 28 03:55PM)

**Meta:** Andrew Trask, Phil Michalak, John Liu, (Submitted on 19 Nov 2015)

**Keywords:** `sense`, `word`, `model`, `embedding`, `disambiguate`, `neural`, `multiple`, `process`

**Abstract:** Neural word representations have proven useful in Natural Language Processing (NLP) tasks due to their ability to efficiently model complex semantic and syntactic word relationships. However, most techniques model only one representation per word, despite the fact that a single word can have multiple meanings or "senses". Some techniques model words by using multiple vectors that are clustered based on context. However, recent neural approaches rarely focus on the application to a consuming NLP algorithm. Furthermore, the training process of recent word-sense models is expensive relative to single-sense embedding processes. This paper presents a novel approach which addresses these concerns by modeling multiple embeddings for each word based on supervised disambiguation, which provides a fast and accurate way for a consuming NLP model to select a sense-disambiguated embedding. We demonstrate that these embeddings can disambiguate both contrastive senses such as nominal and verbal senses as well as nuanced senses such as sarcasm. We further evaluate Part-of-Speech disambiguated embeddings on neural dependency parsing, yielding a greater than 8% average error reduction in unlabeled attachment scores across 6 languages.

___

**(#40) Title:** [Visual Attribute Transfer through Deep Image Analogy](https://arxiv.org/abs/1705.01088) (added 2018 March 28 03:54PM)

**Meta:** Jing Liao, Yuan Yao, Lu Yuan, Gang Hua, Sing Bing Kang, (Submitted on 2 May 2017 (v1), last revised 6 Jun 2017 (this version, v2))

**Keywords:** `technique`, `transfer`, `style`, `image`, `semantic`, `texture`, `sketch`, `visual attribute`

**Abstract:** We propose a new technique for visual attribute transfer across images that may have very different appearance but have perceptually similar semantic structure. By visual attribute transfer, we mean transfer of visual information (such as color, tone, texture, and style) from one image to another. For example, one image could be that of a painting or a sketch while the other is a photo of a real scene, and both depict the same type of scene. 
Our technique finds semantically-meaningful dense correspondences between two input images. To accomplish this, it adapts the notion of "image analogy" with features extracted from a Deep Convolutional Neutral Network for matching; we call our technique Deep Image Analogy. A coarse-to-fine strategy is used to compute the nearest-neighbor field for generating the results. We validate the effectiveness of our proposed method in a variety of cases, including style/texture transfer, color/style swap, sketch/painting to photo, and time lapse.

___

**(#39) Title:** [Feynman Machine: The Universal Dynamical Systems Computer](https://arxiv.org/abs/1609.03971) (added 2018 March 28 03:51PM)

**Meta:** Eric Laukien, Richard Crowder, Fergal Byrne, (Submitted on 13 Sep 2016)

**Keywords:** `computation`, `machine`, `dynamical systems`, `intelligence`, `model`, `mammalian`, `interacting dynamical`, `findings`

**Abstract:** Efforts at understanding the computational processes in the brain have met with limited success, despite their importance and potential uses in building intelligent machines. We propose a simple new model which draws on recent findings in Neuroscience and the Applied Mathematics of interacting Dynamical Systems. The Feynman Machine is a Universal Computer for Dynamical Systems, analogous to the Turing Machine for symbolic computing, but with several important differences. We demonstrate that networks and hierarchies of simple interacting Dynamical Systems, each adaptively learning to forecast its evolution, are capable of automatically building sensorimotor models of the external and internal world. We identify such networks in mammalian neocortex, and show how existing theories of cortical computation combine with our model to explain the power and flexibility of mammalian intelligence. These findings lead directly to new architectures for machine intelligence. A suite of software implementations has been built based on these principles, and applied to a number of spatiotemporal learning tasks.

___

**(#38) Title:** [Learning to learn by gradient descent by gradient descent](https://arxiv.org/abs/1606.04474) (added 2018 March 28 03:16PM)

**Meta:** Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W. Hoffman, David Pfau, Tom Schaul, Brendan Shillingford, Nando de Freitas, (Submitted on 14 Jun 2016 (v1), last revised 30 Nov 2016 (this version, v2))

**Keywords:** `learn`, `algorithm`, `tasks`, `problem`, `design`, `neural`, `optimization algorithm`, `trained`

**Abstract:** The move from hand-designed features to learned features in machine learning has been wildly successful. In spite of this, optimization algorithms are still designed by hand. In this paper we show how the design of an optimization algorithm can be cast as a learning problem, allowing the algorithm to learn to exploit structure in the problems of interest in an automatic way. Our learned algorithms, implemented by LSTMs, outperform generic, hand-designed competitors on the tasks for which they are trained, and also generalize well to new tasks with similar structure. We demonstrate this on a number of tasks, including simple convex problems, training neural networks, and styling images with neural art.

___

**(#37) Title:** [Ask the Right Questions: Active Question Reformulation with Reinforcement Learning](https://arxiv.org/abs/1705.07830) (added 2018 March 28 03:15PM)

**Meta:** Christian Buck, Jannis Bulian, Massimiliano Ciaramita, Wojciech Gajewski, Andrea Gesmundo, Neil Houlsby, Wei Wang, (Submitted on 22 May 2017 (v1), last revised 2 Mar 2018 (this version, v3))

**Keywords:** `reformulate`, `question`, `agent`, `answer`, `learned`, `question answer`, `system`, `qa`

**Abstract:** We frame Question Answering (QA) as a Reinforcement Learning task, an approach that we call Active Question Answering. We propose an agent that sits between the user and a black box QA system and learns to reformulate questions to elicit the best possible answers. The agent probes the system with, potentially many, natural language reformulations of an initial question and aggregates the returned evidence to yield the best answer. The reformulation system is trained end-to-end to maximize answer quality using policy gradient. We evaluate on SearchQA, a dataset of complex questions extracted from Jeopardy!. The agent outperforms a state-of-the-art base model, playing the role of the environment, and other benchmarks. We also analyze the language that the agent has learned while interacting with the question answering system. We find that successful question reformulations look quite different from natural language paraphrases. The agent is able to discover non-trivial reformulation strategies that resemble classic information retrieval techniques such as term re-weighting (tf-idf) and stemming.

___

**(#36) Title:** [Learning to reinforcement learn](https://arxiv.org/abs/1611.05763) (added 2018 March 28 03:14PM)

**Meta:** Jane X Wang, Zeb Kurth-Nelson, Dhruva Tirumala, Hubert Soyer, Joel Z Leibo, Remi Munos, Charles Blundell, Dharshan Kumaran, Matt Botvinick, (Submitted on 17 Nov 2016 (v1), last revised 23 Jan 2017 (this version, v3))

**Keywords:** `rl`, `trained`, `learned`, `deep`, `approach`, `recurrent`, `rl algorithm`, `reinforcement learned`

**Abstract:** In recent years deep reinforcement learning (RL) systems have attained superhuman performance in a number of challenging task domains. However, a major limitation of such applications is their demand for massive amounts of training data. A critical present objective is thus to develop deep RL methods that can adapt rapidly to new tasks. In the present work we introduce a novel approach to this challenge, which we refer to as deep meta-reinforcement learning. Previous work has shown that recurrent networks can support meta-learning in a fully supervised context. We extend this approach to the RL setting. What emerges is a system that is trained using one RL algorithm, but whose recurrent dynamics implement a second, quite separate RL procedure. This second, learned RL algorithm can differ from the original one in arbitrary ways. Importantly, because it is learned, it is configured to exploit structure in the training domain. We unpack these points in a series of seven proof-of-concept experiments, each of which examines a key aspect of deep meta-RL. We consider prospects for extending and scaling up the approach, and also point out some potentially important implications for neuroscience.

___

**(#35) Title:** [A Deep Reinforcement Learning Chatbot](https://arxiv.org/abs/1709.02349) (added 2018 March 28 03:13PM)

**Meta:** Iulian V. Serban, Chinnadhurai Sankar, Mathieu Germain, Saizheng Zhang, Zhouhan Lin, Sandeep Subramanian, Taesup Kim, Michael Pieper, Sarath Chandar, Nan Rosemary Ke, Sai Rajeshwar, Alexandre de Brebisson, Jose M. R. Sotelo, Dendi Suhubdy, Vincent Michalski, Alexandre Nguyen, Joelle Pineau, Yoshua Bengio, (Submitted on 7 Sep 2017 (v1), last revised 5 Nov 2017 (this version, v2))

**Keywords:** `models`, `system`, `learning`, `milabot`, `reinforcement learning`, `ensemble`, `neural network`, `sequence`

**Abstract:** We present MILABOT: a deep reinforcement learning chatbot developed by the Montreal Institute for Learning Algorithms (MILA) for the Amazon Alexa Prize competition. MILABOT is capable of conversing with humans on popular small talk topics through both speech and text. The system consists of an ensemble of natural language generation and retrieval models, including template-based models, bag-of-words models, sequence-to-sequence neural network and latent variable neural network models. By applying reinforcement learning to crowdsourced data and real-world user interactions, the system has been trained to select an appropriate response from the models in its ensemble. The system has been evaluated through A/B testing with real-world users, where it performed significantly better than many competing systems. Due to its machine learning architecture, the system is likely to improve with additional data.

___

**(#34) Title:** [Toward Controlled Generation of Text](https://arxiv.org/abs/1703.00955) (added 2018 March 28 05:49AM)

**Meta:** Zhiting Hu, Zichao Yang, Xiaodan Liang, Ruslan Salakhutdinov, Eric P. Xing, (Submitted on 2 Mar 2017 (v1), last revised 23 Jan 2018 (this version, v3))

**Keywords:** `attribute`, `generating`, `learning`, `sentence`, `discriminators`, `semantic`, `representations`, `generating model`

**Abstract:** Generic generation and manipulation of text is challenging and has limited success compared to recent deep generative modeling in visual domain. This paper aims at generating plausible natural language sentences, whose attributes are dynamically controlled by learning disentangled latent representations with designated semantics. We propose a new neural generative model which combines variational auto-encoders and holistic attribute discriminators for effective imposition of semantic structures. With differentiable approximation to discrete text samples, explicit constraints on independent attribute controls, and efficient collaborative learning of generator and discriminators, our model learns highly interpretable representations from even only word annotations, and produces realistic sentences with desired attributes. Quantitative evaluation validates the accuracy of sentence and attribute generation.

___

**(#33) Title:** [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/abs/1703.10135) (added 2018 March 28 05:47AM)

**Meta:** Yuxuan Wang, RJ Skerry-Ryan, Daisy Stanton, Yonghui Wu, Ron J. Weiss, Navdeep Jaitly, Zongheng Yang, Ying Xiao, Zhifeng Chen, Samy Bengio, Quoc Le, Yannis Agiomyrgiannakis, Rob Clark, Rif A. Saurous, (Submitted on 29 Mar 2017 (v1), last revised 6 Apr 2017 (this version, v2))

**Keywords:** `speech`, `text`, `tacotron`, `model`, `generates`, `synthesis`, `sequence`, `audio`

**Abstract:** A text-to-speech synthesis system typically consists of multiple stages, such as a text analysis frontend, an acoustic model and an audio synthesis module. Building these components often requires extensive domain expertise and may contain brittle design choices. In this paper, we present Tacotron, an end-to-end generative text-to-speech model that synthesizes speech directly from characters. Given <text, audio> pairs, the model can be trained completely from scratch with random initialization. We present several key techniques to make the sequence-to-sequence framework perform well for this challenging task. Tacotron achieves a 3.82 subjective 5-scale mean opinion score on US English, outperforming a production parametric system in terms of naturalness. In addition, since Tacotron generates speech at the frame level, it's substantially faster than sample-level autoregressive methods.

___

**(#32) Title:** [Machine Learning on Sequential Data Using a Recurrent Weighted Average](https://arxiv.org/abs/1703.01253) (added 2018 March 28 05:46AM)

**Meta:** Jared Ostmeyer, Lindsay Cowell, (Submitted on 3 Mar 2017 (v1), last revised 4 May 2017 (this version, v5))

**Keywords:** `model`, `symbol`, `rnn`, `rwa`, `processed`, `computational`, `classification`, `rnn architecture`

**Abstract:** Recurrent Neural Networks (RNN) are a type of statistical model designed to handle sequential data. The model reads a sequence one symbol at a time. Each symbol is processed based on information collected from the previous symbols. With existing RNN architectures, each symbol is processed using only information from the previous processing step. To overcome this limitation, we propose a new kind of RNN model that computes a recurrent weighted average (RWA) over every past processing step. Because the RWA can be computed as a running average, the computational overhead scales like that of any other RNN architecture. The approach essentially reformulates the attention mechanism into a stand-alone model. The performance of the RWA model is assessed on the variable copy problem, the adding problem, classification of artificial grammar, classification of sequences by length, and classification of the MNIST images (where the pixels are read sequentially one at a time). On almost every task, the RWA model is found to outperform a standard LSTM model.

___

**(#31) Title:** [Representing Sentences as Low-Rank Subspaces](https://arxiv.org/abs/1704.05358v1) (added 2018 March 28 05:44AM)

**Meta:** Jiaqi Mu, Suma Bhat, Pramod Viswanath, (Submitted on 18 Apr 2017)

**Keywords:** `sentence`, `semantic`, `representation`, `word`, `datasets`, `vectors`, `rank subspace`, `observation`

**Abstract:** Sentences are important semantic units of natural language. A generic, distributional representation of sentences that can capture the latent semantics is beneficial to multiple downstream applications. We observe a simple geometry of sentences -- the word representations of a given sentence (on average 10.23 words in all SemEval datasets with a standard deviation 4.84) roughly lie in a low-rank subspace (roughly, rank 4). Motivated by this observation, we represent a sentence by the low-rank subspace spanned by its word vectors. Such an unsupervised representation is empirically validated via semantic textual similarity tasks on 19 different datasets, where it outperforms the sophisticated neural network models, including skip-thought vectors, by 15% on average.

___

**(#30) Title:** [Affect-LM: A Neural Language Model for Customizable Affective Text Generation](https://arxiv.org/abs/1704.06851) (added 2018 March 28 05:43AM)

**Meta:** Sayan Ghosh, Mathieu Chollet, Eugene Laksana, Louis-Philippe Morency, Stefan Scherer, (Submitted on 22 Apr 2017)

**Keywords:** `affect`, `affect lm`, `emotional`, `generated`, `language model`, `conversational text`, `propose`, `sentences`

**Abstract:** Human verbal communication includes affective messages which are conveyed through use of emotionally colored words. There has been a lot of research in this direction but the problem of integrating state-of-the-art neural language models with affective information remains an area ripe for exploration. In this paper, we propose an extension to an LSTM (Long Short-Term Memory) language model for generating conversational text, conditioned on affect categories. Our proposed model, Affect-LM enables us to customize the degree of emotional content in generated sentences through an additional design parameter. Perception studies conducted using Amazon Mechanical Turk show that Affect-LM generates naturally looking emotional sentences without sacrificing grammatical correctness. Affect-LM also learns affect-discriminative word representations, and perplexity experiments show that additional affective information in conversational text can improve language model prediction.

___

**(#29) Title:** [The More You Know: Using Knowledge Graphs for Image Classification](https://arxiv.org/abs/1612.04844) (added 2018 March 28 05:40AM)

**Meta:** Kenneth Marino, Ruslan Salakhutdinov, Abhinav Gupta, Submitted on 14 Dec 2016 (v1), last revised 22 Apr 2017 (this version, v2)

**Keywords:** `knowledge`, `learn`, `graph`, `classification`, `characteristic`, `neural network`, `knowledge graph`, `vision`

**Abstract:** One characteristic that sets humans apart from modern learning-based computer vision algorithms is the ability to acquire knowledge about the world and use that knowledge to reason about the visual world. Humans can learn about the characteristics of objects and the relationships that occur between them to learn a large variety of visual concepts, often with few examples. This paper investigates the use of structured prior knowledge in the form of knowledge graphs and shows that using this knowledge improves performance on image classification. We build on recent work on end-to-end learning on graphs, introducing the Graph Search Neural Network as a way of efficiently incorporating large knowledge graphs into a vision classification pipeline. We show in a number of experiments that our method outperforms standard neural network baselines for multi-label classification.

___

**(#28) Title:** [Generative Temporal Models with Memory](https://arxiv.org/abs/1702.04649) (added 2018 March 28 05:39AM)

**Meta:** Mevlana Gemici, Chia-Chun Hung, Adam Santoro, Greg Wayne, Shakir Mohamed, Danilo J. Rezende, David Amos, Timothy Lillicrap, Submitted on 15 Feb 2017 (v1), last revised 21 Feb 2017 (this version, v2)

**Keywords:** `model`, `temporal`, `predict`, `elements`, `dependencies`, `unpredictable elements`, `observations`, `temporal model`

**Abstract:** We consider the general problem of modeling temporal data with long-range dependencies, wherein new observations are fully or partially predictable based on temporally-distant, past observations. A sufficiently powerful temporal model should separate predictable elements of the sequence from unpredictable elements, express uncertainty about those unpredictable elements, and rapidly identify novel elements that may help to predict the future. To create such models, we introduce Generative Temporal Models augmented with external memory systems. They are developed within the variational inference framework, which provides both a practical training methodology and methods to gain insight into the models' operation. We show, on a range of problems with sparse, long-term temporal dependencies, that these models store information from early in a sequence, and reuse this stored information efficiently. This allows them to perform substantially better than existing models based on well-known recurrent neural networks, like LSTMs.

___

**(#27) Title:** [Multi-step Reinforcement Learning: A Unifying Algorithm](https://arxiv.org/abs/1703.01327) (added 2018 March 28 05:37AM)

**Meta:** Kristopher De Asis, J. Fernando Hernandez-Garcia, G. Zacharias Holland, Richard S. Sutton, Submitted on 3 Mar 2017

**Keywords:** `algorithm`, `perform`, `step`, `unifies`, `td`, `learning`, `case`, `sarsa`

**Abstract:** Unifying seemingly disparate algorithmic ideas to produce better performing algorithms has been a longstanding goal in reinforcement learning. As a primary example, TD() elegantly unifies one-step TD prediction with Monte Carlo methods through the use of eligibility traces and the trace-decay parameter . Currently, there are a multitude of algorithms that can be used to perform TD control, including Sarsa, Q-learning, and Expected Sarsa. These methods are often studied in the one-step case, but they can be extended across multiple time steps to achieve better performance. Each of these algorithms is seemingly distinct, and no one dominates the others for all problems. In this paper, we study a new multi-step action-value algorithm called Q() which unifies and generalizes these existing algorithms, while subsuming them as special cases. A new parameter, , is introduced to allow the degree of sampling performed by the algorithm at each step during its backup to be continuously varied, with Sarsa existing at one extreme (full sampling), and Expected Sarsa existing at the other (pure expectation). Q() is generally applicable to both on- and off-policy learning, but in this work we focus on experiments in the on-policy case. Our results show that an intermediate value of , which results in a mixture of the existing algorithms, performs better than either extreme. The mixture can also be varied dynamically which can result in even greater performance.

___

**(#26) Title:** [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (added 2018 March 28 05:35AM)

**Meta:** Geoffrey Hinton, Oriol Vinyals, Jeff Dean, Submitted on 9 Mar 2015

**Keywords:** `model`, `ensemble`, `compress`, `deploy`, `predictions`, `learn`, `specialist model`, `improve`

**Abstract:** A very simple way to improve the performance of almost any machine learning algorithm is to train many different models on the same data and then to average their predictions. Unfortunately, making predictions using a whole ensemble of models is cumbersome and may be too computationally expensive to allow deployment to a large number of users, especially if the individual models are large neural nets. Caruana and his collaborators have shown that it is possible to compress the knowledge in an ensemble into a single model which is much easier to deploy and we develop this approach further using a different compression technique. We achieve some surprising results on MNIST and we show that we can significantly improve the acoustic model of a heavily used commercial system by distilling the knowledge in an ensemble of models into a single model. We also introduce a new type of ensemble composed of one or more full models and many specialist models which learn to distinguish fine-grained classes that the full models confuse. Unlike a mixture of experts, these specialist models can be trained rapidly and in parallel.

___

**(#25) Title:** [Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796) (added 2018 March 28 05:32AM)

**Meta:** James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, Raia Hadsell, Submitted on 2 Dec 2016 (v1), last revised 25 Jan 2017 (this version, v2)

**Keywords:** `tasks`, `learn`, `sequential`, `networks`, `approach`, `2600`, `connectionist`, `mnist`

**Abstract:** The ability to learn tasks in a sequential fashion is crucial to the development of artificial intelligence. Neural networks are not, in general, capable of this and it has been widely thought that catastrophic forgetting is an inevitable feature of connectionist models. We show that it is possible to overcome this limitation and train networks that can maintain expertise on tasks which they have not experienced for a long time. Our approach remembers old tasks by selectively slowing down learning on the weights important for those tasks. We demonstrate our approach is scalable and effective by solving a set of classification tasks based on the MNIST hand written digit dataset and by learning several Atari 2600 games sequentially.

___

**(#24) Title:** [PixelCNN Models with Auxiliary Variables for Natural Image Modeling](https://arxiv.org/abs/1612.08185) (added 2018 March 28 05:30AM)

**Meta:** Alexander Kolesnikov, Christoph H. Lampert, Submitted on 24 Dec 2016 (v1), last revised 1 Jul 2017 (this version, v4)

**Keywords:** `image`, `models`, `pixelcnn`, `probabilistic models`, `auxiliary variables`, `image samples`, `proposed models`, `level image`

**Abstract:** We study probabilistic models of natural images and extend the autoregressive family of PixelCNN architectures by incorporating auxiliary variables. Subsequently, we describe two new generative image models that exploit different image transformations as auxiliary variables: a quantized grayscale view of the image or a multi-resolution image pyramid. The proposed models tackle two known shortcomings of existing PixelCNN models: 1) their tendency to focus on low-level image details, while largely ignoring high-level image information, such as object shapes, and 2) their computationally costly procedure for image sampling. We experimentally demonstrate benefits of the proposed models, in particular showing that they produce much more realistically looking image samples than previous state-of-the-art probabilistic models.

___

**(#23) Title:** [Bidirectional Attention Flow for Machine Comprehension](https://arxiv.org/abs/1611.01603) (added 2018 March 28 05:19AM)

**Meta:** Minjoon Seo, Aniruddha Kembhavi, Ali Farhadi, Hannaneh Hajishirzi, Submitted on 5 Nov 2016 (v1), last revised 24 Feb 2017 (this version, v5)

**Keywords:** `context`, `query`, `directional attention`, `attention`, `summarization`, `answering`, `bi directional`, `mc`

**Abstract:** Machine comprehension (MC), answering a query about a given context paragraph, requires modeling complex interactions between the context and the query. Recently, attention mechanisms have been successfully extended to MC. Typically these methods use attention to focus on a small portion of the context and summarize it with a fixed-size vector, couple attentions temporally, and/or often form a uni-directional attention. In this paper we introduce the Bi-Directional Attention Flow (BIDAF) network, a multi-stage hierarchical process that represents the context at different levels of granularity and uses bi-directional attention flow mechanism to obtain a query-aware context representation without early summarization. Our experimental evaluations show that our model achieves the state-of-the-art results in Stanford Question Answering Dataset (SQuAD) and CNN/DailyMail cloze test.

___

**(#22) Title:** [Convolutional Neural Fabrics](https://arxiv.org/abs/1606.02492v4) (added 2018 March 28 04:58AM)

**Meta:** Shreyas Saxena, Jakob Verbeek, Submitted on 8 Jun 2016 (v1), last revised 30 Jan 2017 (this version, v4)

**Keywords:** `fabric`, `architecture`, `connectivity`, `paths`, `scales`, `layers`, `parameters`, `optimal architecture`

**Abstract:** Despite the success of CNNs, selecting the optimal architecture for a given task remains an open problem. Instead of aiming to select a single optimal architecture, we propose a "fabric" that embeds an exponentially large number of architectures. The fabric consists of a 3D trellis that connects response maps at different layers, scales, and channels with a sparse homogeneous local connectivity pattern. The only hyper-parameters of a fabric are the number of channels and layers. While individual architectures can be recovered as paths, the fabric can in addition ensemble all embedded architectures together, sharing their weights where their paths overlap. Parameters can be learned using standard methods based on back-propagation, at a cost that scales linearly in the fabric size. We present benchmark results competitive with the state of the art for image classification on MNIST and CIFAR10, and for semantic segmentation on the Part Labels dataset.

___

**(#21) Title:** [Strategic Attentive Writer for Learning Macro-Actions](https://arxiv.org/abs/1606.04695) (added 2018 March 28 04:53AM)

**Meta:** Alexander (Sasha) Vezhnevets, Volodymyr Mnih, John Agapiou, Simon Osindero, Alex Graves, Oriol Vinyals, Koray Kavukcuoglu, Submitted on 15 Jun 2016

**Keywords:** `learn`, `plan`, `straw`, `macro actions`, `temporally`, `prediction`, `demonstrate`, `end`

**Abstract:** We present a novel deep recurrent neural network architecture that learns to build implicit plans in an end-to-end manner by purely interacting with an environment in reinforcement learning setting. The network builds an internal plan, which is continuously updated upon observation of the next input from the environment. It can also partition this internal representation into contiguous sub- sequences by learning for how long the plan can be committed to - i.e. followed without re-planing. Combining these properties, the proposed model, dubbed STRategic Attentive Writer (STRAW) can learn high-level, temporally abstracted macro- actions of varying lengths that are solely learnt from data without any prior information. These macro-actions enable both structured exploration and economic computation. We experimentally demonstrate that STRAW delivers strong improvements on several ATARI games by employing temporally extended planning strategies (e.g. Ms. Pacman and Frostbite). It is at the same time a general algorithm that can be applied on any sequence data. To that end, we also show that when trained on text prediction task, STRAW naturally predicts frequent n-grams (instead of macro-actions), demonstrating the generality of the approach.

___

**(#20) Title:** [Pointer Networks](https://arxiv.org/abs/1506.03134) (added 2018 March 28 04:28AM)

**Meta:** Oriol Vinyals, Meire Fortunato, Navdeep Jaitly, Submitted on 9 Jun 2015 (v1), last revised 2 Jan 2017 (this version, v2)

**Keywords:** `sequence`, `problem`, `attention`, `neural`, `ptr net`, `input`, `output`, `learn`

**Abstract:** We introduce a new neural architecture to learn the conditional probability of an output sequence with elements that are discrete tokens corresponding to positions in an input sequence. Such problems cannot be trivially addressed by existent approaches such as sequence-to-sequence and Neural Turing Machines, because the number of target classes in each step of the output depends on the length of the input, which is variable. Problems such as sorting variable sized sequences, and various combinatorial optimization problems belong to this class. Our model solves the problem of variable size output dictionaries using a recently proposed mechanism of neural attention. It differs from the previous attention attempts in that, instead of using attention to blend hidden units of an encoder to a context vector at each decoder step, it uses attention as a pointer to select a member of the input sequence as the output. We call this architecture a Pointer Net (Ptr-Net). We show Ptr-Nets can be used to learn approximate solutions to three challenging geometric problems -- finding planar convex hulls, computing Delaunay triangulations, and the planar Travelling Salesman Problem -- using training examples alone. Ptr-Nets not only improve over sequence-to-sequence with input attention, but also allow us to generalize to variable size output dictionaries. We show that the learnt models generalize beyond the maximum lengths they were trained on. We hope our results on these tasks will encourage a broader exploration of neural learning for discrete problems.

___

**(#19) Title:** [On Learning to Think: Algorithmic Information Theory for Novel Combinations of Reinforcement Learning Controllers and Recurrent Neural World Models](https://arxiv.org/abs/1511.09249) (added 2018 March 28 04:23AM)

**Meta:** Submitted on 30 Nov 2015

**Keywords:** `learn`, `rnnai`, `model`, `rnn based`, `rl`, `rnn`, `abstract`, `reasoning`

**Abstract:** This paper addresses the general problem of reinforcement learning (RL) in partially observable environments. In 2013, our large RL recurrent neural networks (RNNs) learned from scratch to drive simulated cars from high-dimensional video input. However, real brains are more powerful in many ways. In particular, they learn a predictive model of their initially unknown environment, and somehow use it for abstract (e.g., hierarchical) planning and reasoning. Guided by algorithmic information theory, we describe RNN-based AIs (RNNAIs) designed to do the same. Such an RNNAI can be trained on never-ending sequences of tasks, some of them provided by the user, others invented by the RNNAI itself in a curious, playful fashion, to improve its RNN-based world model. Unlike our previous model-building RNN-based RL machines dating back to 1990, the RNNAI learns to actively query its model for abstract reasoning and planning and decision making, essentially "learning to think." The basic ideas of this report can be applied to many other cases where one RNN-like system exploits the algorithmic information content of another. They are taken from a grant proposal submitted in Fall 2014, and also explain concepts such as "mirror neurons." Experimental results will be described in separate papers.

___

**(#18) Title:** [On the Expressive Power of Deep Neural Networks](https://arxiv.org/abs/1606.05336v6) (added 2018 March 28 04:22AM)

**Meta:** Submitted on 16 Jun 2016 (v1), last revised 18 Jun 2017 (this version, v6)

**Keywords:** `network`, `expressivity`, `regularization`, `trajectory`, `compute`, `weights`, `trajectory length`, `neural network`

**Abstract:** We propose a new approach to the problem of neural network expressivity, which seeks to characterize how structural properties of a neural network family affect the functions it is able to compute. Our approach is based on an interrelated set of measures of expressivity, unified by the novel notion of trajectory length, which measures how the output of a network changes as the input sweeps along a one-dimensional path. Our findings can be summarized as follows: 
(1) The complexity of the computed function grows exponentially with depth. 
(2) All weights are not equal: trained networks are more sensitive to their lower (initial) layer weights. 
(3) Regularizing on trajectory length (trajectory regularization) is a simpler alternative to batch normalization, with the same performance.

___

**(#17) Title:** [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357) (added 2018 March 28 04:20AM)

**Meta:** Submitted on 7 Oct 2016 (v1), last revised 4 Apr 2017 (this version, v3)

**Keywords:** `convolution`, `inception v3`, `inception`, `depthwise separable convolution`, `inception module`, `architecture`, `outperforms inception`, `xception`

**Abstract:** We present an interpretation of Inception modules in convolutional neural networks as being an intermediate step in-between regular convolution and the depthwise separable convolution operation (a depthwise convolution followed by a pointwise convolution). In this light, a depthwise separable convolution can be understood as an Inception module with a maximally large number of towers. This observation leads us to propose a novel deep convolutional neural network architecture inspired by Inception, where Inception modules have been replaced with depthwise separable convolutions. We show that this architecture, dubbed Xception, slightly outperforms Inception V3 on the ImageNet dataset (which Inception V3 was designed for), and significantly outperforms Inception V3 on a larger image classification dataset comprising 350 million images and 17,000 classes. Since the Xception architecture has the same number of parameters as Inception V3, the performance gains are not due to increased capacity but rather to a more efficient use of model parameters.

___

**(#16) Title:** [Reasoning with Memory Augmented Neural Networks for Language Comprehension](https://arxiv.org/abs/1610.06454v2) (added 2018 March 28 04:18AM)

**Meta:** Submitted on 20 Oct 2016 (v1), last revised 28 Feb 2017 (this version, v2)

**Keywords:** `hypothesis test`, `approach`, `test`, `nse`, `comprehension`, `neural`, `hypothesis`, `previous`

**Abstract:** Hypothesis testing is an important cognitive process that supports human reasoning. In this paper, we introduce a computational hypothesis testing approach based on memory augmented neural networks. Our approach involves a hypothesis testing loop that reconsiders and progressively refines a previously formed hypothesis in order to generate new hypotheses to test. We apply the proposed approach to language comprehension task by using Neural Semantic Encoders (NSE). Our NSE models achieve the state-of-the-art results showing an absolute improvement of 1.2% to 2.6% accuracy over previous results obtained by single and ensemble systems on standard machine comprehension benchmarks such as the Children's Book Test (CBT) and Who-Did-What (WDW) news article datasets.

___

**(#15) Title:** [Neural Networks with Few Multiplications](https://arxiv.org/abs/1510.03009) (added 2018 March 28 04:05AM)

**Meta:** Submitted on 11 Oct 2015 (v1), last revised 26 Feb 2016 (this version, v3)

**Keywords:** `training`, `multiplications`, `binarize`, `stochastic`, `computation`, `weights`, `neural networks`, `convert`

**Abstract:** For most deep learning algorithms training is notoriously time consuming. Since most of the computation in training neural networks is typically spent on floating point multiplications, we investigate an approach to training that eliminates the need for most of these. Our method consists of two parts: First we stochastically binarize weights to convert multiplications involved in computing hidden states to sign changes. Second, while back-propagating error derivatives, in addition to binarizing the weights, we quantize the representations at each layer to convert the remaining multiplications into binary shifts. Experimental results across 3 popular datasets (MNIST, CIFAR10, SVHN) show that this approach not only does not hurt classification performance but can result in even better performance than standard stochastic gradient descent training, paving the way to fast, hardware-friendly training of neural networks.

___

**(#14) Title:** [Memory Networks](https://arxiv.org/abs/1410.3916) (added 2018 March 28 04:04AM)

**Meta:** Submitted on 15 Oct 2014 (v1), last revised 29 Nov 2015 (this version, v11)

**Keywords:** `models`, `long term memory`, `qa`, `component`, `learn`, `memory networks`, `task`, `memory`

**Abstract:** We describe a new class of learning models called memory networks. Memory networks reason with inference components combined with a long-term memory component; they learn how to use these jointly. The long-term memory can be read and written to, with the goal of using it for prediction. We investigate these models in the context of question answering (QA) where the long-term memory effectively acts as a (dynamic) knowledge base, and the output is a textual response. We evaluate them on a large-scale QA task, and a smaller, but more complex, toy task generated from a simulated world. In the latter, we show the reasoning power of such models by chaining multiple supporting sentences to answer questions that require understanding the intension of verbs.

___

**(#13) Title:** [InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets](https://arxiv.org/abs/1606.03657) (added 2018 March 28 04:03AM)

**Meta:** Submitted on 12 Jun 2016

**Keywords:** `infogan`, `dataset`, `representations`, `digit`, `learn`, `disentangled`, `interpretable`, `generative adversarial`

**Abstract:** This paper describes InfoGAN, an information-theoretic extension to the Generative Adversarial Network that is able to learn disentangled representations in a completely unsupervised manner. InfoGAN is a generative adversarial network that also maximizes the mutual information between a small subset of the latent variables and the observation. We derive a lower bound to the mutual information objective that can be optimized efficiently, and show that our training procedure can be interpreted as a variation of the Wake-Sleep algorithm. Specifically, InfoGAN successfully disentangles writing styles from digit shapes on the MNIST dataset, pose from lighting of 3D rendered images, and background digits from the central digit on the SVHN dataset. It also discovers visual concepts that include hair styles, presence/absence of eyeglasses, and emotions on the CelebA face dataset. Experiments show that InfoGAN learns interpretable representations that are competitive with representations learned by existing fully supervised methods.

___

**(#12) Title:** [On Multiplicative Integration with Recurrent Neural Networks](https://arxiv.org/abs/1606.06630) (added 2018 March 28 03:59AM)

**Meta:** Submitted on 21 Jun 2016 (v1), last revised 12 Nov 2016 (this version, v2)

**Keywords:** `rnn models`, `rnn`, `multiplicative integrated`, `introduce`, `structural`, `integrated`, `mi`, `difference`

**Abstract:** We introduce a general and simple structural design called Multiplicative Integration (MI) to improve recurrent neural networks (RNNs). MI changes the way in which information from difference sources flows and is integrated in the computational building block of an RNN, while introducing almost no extra parameters. The new structure can be easily embedded into many popular RNN models, including LSTMs and GRUs. We empirically analyze its learning behaviour and conduct evaluations on several tasks using different RNN models. Our experimental results demonstrate that Multiplicative Integration can provide a substantial performance boost over many of the existing RNN models.

___

**(#11) Title:** [Stacked Hourglass Networks for Human Pose Estimation](https://arxiv.org/abs/1603.06937v2) (added 2018 March 28 03:55AM)

**Meta:** Submitted on 22 Mar 2016 (v1), last revised 26 Jul 2016 (this version, v2)

**Keywords:** `network`, `processed`, `architecture`, `mpii`, `outcompeting`, `convolutional`, `upsampling`, `flic`

**Abstract:** This work introduces a novel convolutional network architecture for the task of human pose estimation. Features are processed across all scales and consolidated to best capture the various spatial relationships associated with the body. We show how repeated bottom-up, top-down processing used in conjunction with intermediate supervision is critical to improving the performance of the network. We refer to the architecture as a "stacked hourglass" network based on the successive steps of pooling and upsampling that are done to produce a final set of predictions. State-of-the-art results are achieved on the FLIC and MPII benchmarks outcompeting all recent methods.

___

**(#10) Title:** [Learning to Understand Phrases by Embedding the Dictionary](https://arxiv.org/abs/1504.00548) (added 2018 March 28 03:50AM)

**Meta:** Submitted on 2 Apr 2015 (v1), last revised 22 Mar 2016 (this version, v4)

**Keywords:** `definition`, `lexical`, `dictionaries`, `representations`, `phrases`, `trained`, `models`, `architectures`

**Abstract:** Distributional models that learn rich semantic word representations are a success story of recent NLP research. However, developing models that learn useful representations of phrases and sentences has proved far harder. We propose using the definitions found in everyday dictionaries as a means of bridging this gap between lexical and phrasal semantics. Neural language embedding models can be effectively trained to map dictionary definitions (phrases) to (lexical) representations of the words defined by those definitions. We present two applications of these architectures: "reverse dictionaries" that return the name of a concept given a definition or description and general-knowledge crossword question answerers. On both tasks, neural language embedding models trained on definitions from a handful of freely-available lexical resources perform as well or better than existing commercial systems that rely on significant task-specific engineering. The results highlight the effectiveness of both neural embedding architectures and definition-based training for developing models that understand phrases and sentences.

___

**(#9) Title:** [End-To-End Memory Networks](https://arxiv.org/abs/1503.08895) (added 2018 March 28 03:49AM)

**Meta:** Submitted on 31 Mar 2015 (v1), last revised 24 Nov 2015 (this version, v5)

**Keywords:** `model`, `hops`, `multiple computational`, `trained`, `less supervision`, `memory`, `approach`, `memory network`

**Abstract:** We introduce a neural network with a recurrent attention model over a possibly large external memory. The architecture is a form of Memory Network (Weston et al., 2015) but unlike the model in that work, it is trained end-to-end, and hence requires significantly less supervision during training, making it more generally applicable in realistic settings. It can also be seen as an extension of RNNsearch to the case where multiple computational steps (hops) are performed per output symbol. The flexibility of the model allows us to apply it to tasks as diverse as (synthetic) question answering and to language modeling. For the former our approach is competitive with Memory Networks, but with less supervision. For the latter, on the Penn TreeBank and Text8 datasets our approach demonstrates comparable performance to RNNs and LSTMs. In both cases we show that the key concept of multiple computational hops yields improved results.

___

**(#8) Title:** [Neural Language Correction with Character-Based Attention](https://arxiv.org/abs/1603.09727v1) (added 2018 March 28 03:46AM)

**Meta:** Submitted on 31 Mar 2016

**Keywords:** `error`, `approach`, `method`, `network`, `language`, `learner`, `flexibility`, `neural`

**Abstract:** Natural language correction has the potential to help language learners improve their writing skills. While approaches with separate classifiers for different error types have high precision, they do not flexibly handle errors such as redundancy or non-idiomatic phrasing. On the other hand, word and phrase-based machine translation methods are not designed to cope with orthographic errors, and have recently been outpaced by neural models. Motivated by these issues, we present a neural network-based approach to language correction. The core component of our method is an encoder-decoder recurrent neural network with an attention mechanism. By operating at the character level, the network avoids the problem of out-of-vocabulary words. We illustrate the flexibility of our approach on dataset of noisy, user-generated text collected from an English learner forum. When combined with a language model, our method achieves a state-of-the-art F0.5-score on the CoNLL 2014 Shared Task. We further demonstrate that training the network on additional data with synthesized errors can improve performance.

___

**(#7) Title:** [Masked Autoregressive Flow for Density Estimation](https://arxiv.org/abs/1705.07057) (added 2018 March 28 03:40AM)

**Meta:** last revised 11 Jan 2018 (this version, v3)

**Keywords:** `model`, `autoregressive model`, `autoregressive flow`, `density estimation`, `flow`, `masked autoregressive`, `stack`, `random numbers`

**Abstract:** Autoregressive models are among the best performing neural density estimators. We describe an approach for increasing the flexibility of an autoregressive model, based on modelling the random numbers that the model uses internally when generating data. By constructing a stack of autoregressive models, each modelling the random numbers of the next model in the stack, we obtain a type of normalizing flow suitable for density estimation, which we call Masked Autoregressive Flow. This type of flow is closely related to Inverse Autoregressive Flow and is a generalization of Real NVP. Masked Autoregressive Flow achieves state-of-the-art performance in a range of general-purpose density estimation tasks.

___

**(#6) Title:** [Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937) (added 2018 March 28 03:37AM)

**Meta:** Submitted on 2 Nov 2017

**Keywords:** `representation`, `learn`, `model`, `vae`, `vq`, `discrete`, `vector quantisation`, `autoregressive`

**Abstract:** Learning useful representations without supervision remains a key challenge in machine learning. In this paper, we propose a simple yet powerful generative model that learns such discrete representations. Our model, the Vector Quantised-Variational AutoEncoder (VQ-VAE), differs from VAEs in two key ways: the encoder network outputs discrete, rather than continuous, codes; and the prior is learnt rather than static. In order to learn a discrete latent representation, we incorporate ideas from vector quantisation (VQ). Using the VQ method allows the model to circumvent issues of "posterior collapse" -- where the latents are ignored when they are paired with a powerful autoregressive decoder -- typically observed in the VAE framework. Pairing these representations with an autoregressive prior, the model can generate high quality images, videos, and speech as well as doing high quality speaker conversion and unsupervised learning of phonemes, providing further evidence of the utility of the learnt representations.

___

**(#5) Title:** [Deep Voice 3: Scaling Text-to-Speech with Convolutional Sequence Learning](https://arxiv.org/abs/1710.07654v3) (added 2018 March 28 03:36AM)

**Meta:** last revised 22 Feb 2018 (this version, v3)

**Keywords:** `deep voice 3`, `tts`, `neural`, `synthesis`, `speech synthesis`, `speech`, `scale`, `ten`

**Abstract:** We present Deep Voice 3, a fully-convolutional attention-based neural text-to-speech (TTS) system. Deep Voice 3 matches state-of-the-art neural speech synthesis systems in naturalness while training ten times faster. We scale Deep Voice 3 to data set sizes unprecedented for TTS, training on more than eight hundred hours of audio from over two thousand speakers. In addition, we identify common error modes of attention-based speech synthesis networks, demonstrate how to mitigate them, and compare several different waveform synthesis methods. We also describe how to scale inference to ten million queries per day on one single-GPU server.

___

**(#4) Title:** [From neural PCA to deep unsupervised learning](https://arxiv.org/abs/1411.7783) (added 2018 March 28 03:29AM)

**Meta:** Submitted on 28 Nov 2014 (v1), last revised 2 Feb 2015 (this version, v2)

**Keywords:** `network`, `learn`, `autoencoder`, `hierarchy`, `layer`, `level`, `denoising`, `encoder`

**Abstract:** A network supporting deep unsupervised learning is presented. The network is an autoencoder with lateral shortcut connections from the encoder to decoder at each level of the hierarchy. The lateral shortcut connections allow the higher levels of the hierarchy to focus on abstract invariant features. While standard autoencoders are analogous to latent variable models with a single layer of stochastic variables, the proposed network is analogous to hierarchical latent variables models. Learning combines denoising autoencoder and denoising sources separation frameworks. Each layer of the network contributes to the cost function a term which measures the distance of the representations produced by the encoder and the decoder. Since training signals originate from all levels of the network, all layers can learn efficiently even in deep networks. The speedup offered by cost terms from higher levels of the hierarchy and the ability to learn invariant features are demonstrated in experiments.

___

**(#3) Title:** [A Convolutional Neural Network for Modelling Sentences](https://arxiv.org/abs/1404.2188v1) (added 2018 March 28 03:27AM)

**Meta:** Submitted on 8 Apr 2014

**Keywords:** `network`, `sentence`, `convolutional`, `dcnn`, `pooling`, `sentiment prediction`, `dynamic`, `task`

**Abstract:** The ability to accurately represent sentences is central to language understanding. We describe a convolutional architecture dubbed the Dynamic Convolutional Neural Network (DCNN) that we adopt for the semantic modelling of sentences. The network uses Dynamic k-Max Pooling, a global pooling operation over linear sequences. The network handles input sentences of varying length and induces a feature graph over the sentence that is capable of explicitly capturing short and long-range relations. The network does not rely on a parse tree and is easily applicable to any language. We test the DCNN in four experiments: small scale binary and multi-class sentiment prediction, six-way question classification and Twitter sentiment prediction by distant supervision. The network achieves excellent performance in the first three tasks and a greater than 25% error reduction in the last task with respect to the strongest baseline.

___

**(#2) Title:** [A Hierarchical Neural Autoencoder for Paragraphs and Documents](https://arxiv.org/abs/1506.01057) (added 2018 March 28 03:21AM)

**Meta:** 6 Jun 2015

**Keywords:** `paragraph`, `model`, `embedding`, `coherence`, `reconstruct`, `generating`, `text`, `lstm`

**Abstract:** Natural language generation of coherent long texts like paragraphs or longer documents is a challenging problem for recurrent networks models. In this paper, we explore an important step toward this generation task: training an LSTM (Long-short term memory) auto-encoder to preserve and reconstruct multi-sentence paragraphs. We introduce an LSTM model that hierarchically builds an embedding for a paragraph from embeddings for sentences and words, then decodes this embedding to reconstruct the original paragraph. We evaluate the reconstructed paragraph using standard metrics like ROUGE and Entity Grid, showing that neural models are able to encode texts in a way that preserve syntactic, semantic, and discourse coherence. While only a first step toward generating coherent text units from neural models, our work has the potential to significantly impact natural language generation and summarization\footnote{Code for the three models described in this paper can be found at www.stanford.edu/~jiweil/ .

___

**(#1) Title:** [Hierarchical Imitation and Reinforcement Learning](https://arxiv.org/abs/1803.00590) (added 2018 March 28 02:31AM)

**Keywords:** `learn`, `hierarchical`, `framework`, `different`, `rl`, `utilize`, `horizon`, `demonstrate`

**Abstract:** We study the problem of learning policies over long time horizons. We present a framework that leverages and integrates two key concepts. First, we utilize hierarchical policy classes that enable planning over different time scales, i.e., the high level planner proposes a sequence of subgoals for the low level planner to achieve. Second, we utilize expert demonstrations within the hierarchical action space to dramatically reduce cost of exploration. Our framework is flexible and can incorporate different combinations of imitation learning (IL) and reinforcement learning (RL) at different levels of the hierarchy. Using long-horizon benchmarks, including Montezuma's Revenge, we empirically demonstrate that our approach can learn significantly faster compared to hierarchical RL, and can be significantly more label- and sample-efficient compared to flat IL. We also provide theoretical analysis of the labeling cost for certain instantiations of our framework.

**Notes:**



- a hierarchical imitation learning framework that exploits two levels of hierarchy to effectively learn over long time horizons
---
layout: page
comments: true
title:  "PaperSaver"
permalink: /papersaver/
---
**Top keywords:** **`different`** (1), **`utilize`** (1), **`framework`** (1), **`hierarchical`** (1), **`horizon`** (1), **`learn`** (1), **`rl`** (1), **`demonstrate`** (1)

___

2018 March 28 02:31AM

**Title**: [Hierarchical Imitation and Reinforcement Learning](https://arxiv.org/abs/1803.00590)

**Keywords**: `learn`, `hierarchical`, `framework`, `different`, `rl`, `utilize`, `horizon`, `demonstrate`

**Abstract**:
We study the problem of learning policies over long time horizons. We present a framework that leverages and integrates two key concepts. First, we utilize hierarchical policy classes that enable planning over different time scales, i.e., the high level planner proposes a sequence of subgoals for the low level planner to achieve. Second, we utilize expert demonstrations within the hierarchical action space to dramatically reduce cost of exploration. Our framework is flexible and can incorporate different combinations of imitation learning (IL) and reinforcement learning (RL) at different levels of the hierarchy. Using long-horizon benchmarks, including Montezuma's Revenge, we empirically demonstrate that our approach can learn significantly faster compared to hierarchical RL, and can be significantly more label- and sample-efficient compared to flat IL. We also provide theoretical analysis of the labeling cost for certain instantiations of our framework.

**Notes:**



- Several reinforcement learning approaches to learning hierarchical policies have been explored, foremost among them the options framework (Sutton et al., 1998; 1999; Fruit & Lazaric, 2017)

- The total number of primitive actions in a trajectory is thus at most HFULL := HHIHLO

- We consider a natural extension of behavioral cloning to the hierarchical setting (Algorithm 1)

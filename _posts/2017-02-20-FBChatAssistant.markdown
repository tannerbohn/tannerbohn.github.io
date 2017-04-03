---
layout: post
comments: true
title:  "Facebook Chat Personal Assistant"
excerpt: "An overview of one of my personal assistant projects"
date:   2017-02-20 14:00:00
---

<a href="https://youtu.be/KBm4l_H2w2Q" target="_blank"><img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/TABAISEC_youtube_2.png" alt="github" width="490" height="320" border="2" /></a>

<a href="https://youtu.be/FaXwIe6RNyg" target="_blank"><img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/TABAISEC_youtube_1.png" alt="github" width="490" height="320" border="2" /></a>



### Outline of Main Aspects

1. Facebook Integration
2. Parsing Algorithm
3. Context Management
4. Specific Features

### 1. Facebook Integration

The program connects to facebook with the [fbchat](https://github.com/carpedm20/fbchat) library. Provided with a Facebook ID and password, it allows for recieving and sending messages (and many other features).

### 2. Parsing Algorithm

This is perhaps the most important aspect of the project. While good solutions for this exist (see [smartly.ai](https://smartly.ai), [api.ai](https://api.ai), or [wit.ai](https://wit.ai)), I wanted to see if I could build an even better one.

The central algorithm I came up with relies on a stochastic optimisation.

#### 2.1 Usage

Example: if the pattern we are currently matching against is:

`"the {entity} in [, a, the] {loc_1} {action} to [a, the] {loc_2} at [, about] {time}"`,

and the user provides:

`"the very large cat in the store ran to a small tree at noon"`,

then the algorithm will return:

```python
{
    'content':{
        'action': 'ran',
        'loc_1': 'store',
        'loc_2': 'small tree',
        'time': 'noon',
        'entity': 'very large cat'},
    'score': 1.6666666666666665,
    'fillers': ['the', 'a', '']
}
```

#### 2.2 Speed Improvements

This code was originally intended to run on a Raspberry Pi, so code speed is important to improve. On my usual computer, a parsing might take 0.1s, but on the Pi, it will take about 1s (a 10x increase).

The type of optimisation used for finding the best parsing is a stochastic random-restart [hill climb](https://en.wikipedia.org/wiki/Hill_climbing). Several tweaks are applied to improve speed for this particular application:

1. pre-testing
    * word intersection and string similarity
2. "give up" thresholds
3. score hashing
4. solution modification biases
5. solution space limitation
6. pattern prioritization

### 3. Context Management

Context management helps the assistant follow more natural and complex language which often includes ambiguity.

Example:


Without context management/ambiguity resolution, a section of dialog from the user might look like this:

1. Question, how large is Toronto?
2. find a couple pictures of Toronto
3. show me a couple pictures of a spire
4. define spire
5. how's the weather in Toronto?
6. add Toronto to the list of places to visit
7. add Berlin to the list of place to visit
8. remind me soon to make supper
9. remind me soon to close the windows

However, with these capabilities, the dialog can take a much more natural form:

1. Question, how large is **Toronto**?
2. find **a couple** pictures of *it*
3. show me *that many* pictures of a **spire**
4. *define*
5. how's the weather *there*?
6. add *it* to the list of **places to visit**
7. add **Berlin** to *the list*
8. remind me **soon** to **make supper**
9. at *that time* remind me to **close the windows**

\* things in **bold** are incorporated into the context, and things in *italics* require disambiguation to understand


### 2. Specific Features

Many features are currently integrated into the assistant, with more being constantly added.

#### 2.1 List of Features

1. Reminders
    * ex. "remind me about that important task in an hour"
2. Factual Questions
    * ex. "tell me, how big is Toronto?"
3. Image Finding
    * ex. "show me a couple pictures of super cute baby turtles"
4. Lists
    * ex. "add 2% milk to the shopping list"
    * ex. "what's on the shopping list?"
    * ex. "remove milk from the shopping list"
    * ex. "delete shopping list"
5. Weather
    * ex. "get weather in London Ontario"
6. Status Tracking
    * ex. "update: went to gym"
    * ex. "getting on a plane at 5:30pm"
    * ex. "what did I do last week?"

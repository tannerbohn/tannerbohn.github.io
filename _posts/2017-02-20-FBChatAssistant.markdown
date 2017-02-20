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

Example: if the pattern we are currently matching against is:

`"the {entity} in [, a, the] {loc_1} {action} to [a, the] {loc_2} at [, about] {time}"`,

and the user provides:

`"the very large cat in the store ran to a small tree at noon"`,

then the algorithm will return:

```
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

### 3. Context Management

Context management helps the assistant follow more natural and complex language which often includes ambiguity.


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

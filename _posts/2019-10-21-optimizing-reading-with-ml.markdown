---
layout: post
comments: false
title:  "How to Optimize Human Reading with Machine Learning (Part II)"
excerpt: "We consider how the various processes involved in reading can be optimized."
date:   2019-10-21 05:00:00
---


<!---
Part 1: introduction, establishing pseudocode, identify processes to improve
Part 2: for each critical process, discuss possible ways of improving them, group together improvements
Part 3: discuss the four main improvement areas, literature
---> 

Our goal in this article is to determine what parts of the reading process can be improved.
We have previously broken down the reading process into simpler processes. 
Now, we want to examine those processed with the intent of determining how they can be optimized.

## 1. What does it mean to optimize reading?

For a given action involved in the reading process, we want to either do it faster or reap greater benefit from doing it. In other words, with a given amount of time and a target understanding level, we want to minimize how much effort is required. This gives us the curve seen in the following diagram.


<a href="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/read_opt_speed_understanding_curve.png" target="_blank"><img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/read_opt_speed_understanding_curve.png" alt="example steps" width="600" height="600" border="0" /></a>

Although we previously discussed three main functions involved in reading, we will skip analysis of `seek_information` and focus only on `read_item` and `estimate_value`. This is simply a result of the decision to focus on the optimization of reading materials after they have been found.

## 2. Processes from `read_item`

Recall the `read_item` function:

~~~~python
def read_item(item):
    
    study_effort   := #estimate effort required to study item
    item_value     := estimate_value(item) # should have already been calculated
    triage_cost    := #estimate cost of locating sub-items
    triage_savings := #estimate effort saved by locating sub-items
    
    if (study_effort < item_value) and (triage_savings < triage_cost):
        study item
        return

    while item_value > triage_cost:
        sub_item := locate_sub_item(item)
        sub_item_value = estimate_value(sub_item)
        sub_item_read_effort := #estimate effort required to read sub-item
        if sub_item_value > sub_item_read_effort:
            read_item(sub_item)

    return
~~~~

To determine how we speed it up...
Every time we call this function (ignoring the recursive call), the following must be done:


To determine how can increase its effectiveness...


Important questions: how many times do we need to call this function? What influences how long a single (non-recursing) call takes?

Branching factor?
    - affected by item values (more higher = more branches), triage cost, sub-item read efforts

Recursion depth?
    - affected by study effort, item values, triage savings and costs



## 3. Processes from `estimate_value`

~~~~python
def estimate_value(item):

    confidence := 0
    confidence_threshold := #minimum value estimate confidence where we are satisfied

    effort_expended := 0
    effort_threshold := #how much effort we are willing to expend to estimate value

    while (confidence < confidence_threshold) and (effort_expended < effort_threshold):
        sub_item := locate_sub_item()

        item_knowledge := #estimate knowledge contained in item given sub-items so far

        # calculate the knowledge value of the sub_item with
        #   respect to existing relevant knowledge
        value := item_knowledge - current_knowledge

        confidence := estimate confidence
        effort_expended += #effort from locating sub-item and updating knowledge estimate
    
    return value

~~~~


Loop count:
    - affected by confidence threshold (fixed), rate of confidence increase, effort threshold (fixed), rate of effort expending

<!---
REFERENCE DEFINITIONS
---> 
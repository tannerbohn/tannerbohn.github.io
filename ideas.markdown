---
layout: page
comments: false
title:  "Ideas"
permalink: /ideas/
---
- **Machine Learning**
  - Reinforcement Learning
    - how to learn sub-policies -- infinitely nestable?
  - Text/Language
    - test out SQuAD dataset (paragraphs, questions, and answer ranges)
    - choose minimal set of sentences form article needed to answer questions about text
    - calculate doc sentence importance scores
    - how does word sound relate to sentiment? can you predict the sentiment of an arbitrary word?
    - convert between text and music
    - word web
    - analyse large list of wiki pages for certain characteristics
    - use autoencoder for text summarization
  - Images
    - train CNN to find shortest path in some environment/maze -- need to be recurrent?
    - what space do artistic styles reside in?
    - ~~train autoencoder on lots of random chunks from image, and create demo where you can "black out" pieces and have it inpaint~~
    - ~~generate image based on topic (colour, texture, etc.)~~
    - multiscale image generator
  - Neuroscience/Meta
    - how to avoid catastrophic learning?
    - evolve strategy for neurons modifying their connections
    - self-optimizing program/AI
    - what function would "brain waves" have in an ANN?
    - running memories in reverse during sleep is like creating explanative model instead of predictive one
  - pattern recognition
    - feed instances of pattern(s) through autoencoder, then use clustering algorithm to detect unique families of patterns
  - Math
    - learn optimal function interpolator
    - predict continued fraction limits (possible?)
  - Generative Adversarial Networks
    - apply to text?
    - try generate more of my art
    - alternative to GANs? (VAEs? -> use idea of learning distribution)
  - ~~train a clustering algorithm with autoencoder~~
  - use idea of ant chemical trains for NN memory augmentation
  - train decorrelated NNs
    - consecutively train sub-nets to both maximize variance between sub-net predictions and performance of each sub-net
  - design game where solution requires agents to posess characteristics of self-awareness and ability to communicate
    - put coloured mark on agents have they have to ask other agents what colour their own dot is (or use mirror?)
  - learn entity motivations/needs as predictive/explanative model
  - implement NN that works and learns in real time
    - fully recursive?
    - might need low cycles/sec when initially learning
    - need gating mechanisms?
    - learning how to learn -- given response from env., learn how to use it to improve future performance
    - use "small world" type of connection dist'n

___

- **Idea Management**
  - MindMap
    - write program to automatically convert links or ideas file to mindmap?
    - be able to create groups and subgroups
    - when saving, make sure every edge is captured
    - move around in 3 dimensions? (perfect application for VR)
    - have separate file for mindmap text and other text
    - suggest links between notes? common terms?
    - use #url to denote that a note is a url, and can be opened (how?)
  - summarize all thoughts in 4 words or less (automate?)
  - have main ideas.txt and automatically convert to webpage like linksaver
    - allow linking between areas?

___

- **Fermi**
  - basic drives, morals, and emotions
  - learning "pet" algorithm/program
  - convert words to notes/freqs
  - how do you impart love?
    - how do you get a human to form an attachment to someone or something? or convince them that it has thoughts and feelings
  - search "communication space" to make program that seems to show intention/human-ness/sentience
  - convert between mood and line shape
  - start Ada (successor to Fermi)

___

- **Math**
  - Image multiplier (Encryption?) Prime images?
  - Interpolation/extrapolation with ASMD
    - what functions do the ASMD produce?
  - closed forms of general continued fractions
  - geometrically motivated number system (baseless?)
  - make recursive ASMD algorithm more flexible
    - loosen bounds to approximately match sequences (apply to fuzzier data)
  - function modifier for numerical integration accuracy
    - transform curve to smooth bumps -- converge to more smooth or uniform curve?
  - improve image multiscale entropy algorithm
    - normalize to max/min possible
    - more rigorous definition
  - ~~moving guess~~
    - ~~You find someone in a state at time t0. You observe them in the state for duration t. Given the person has been in there for (t + x), what is the most likely total time they have been in the state?~~
  - sequences are metaphors are mappings

___

- **Images**
  - convert image to algorithm, recursively apply
    - how to ensure fixed point existence? -- if none, can view time series
  - convert simulation to image
    - represent state as a position in image as well as colour
    - for each position in image, convert to state alpha, see what state alpha goes to (beta), and colour the position of alpha as beta's colour
  - use symmetry & asymmetry rules to generate image
  - algorithm image isomorphism/conversions
    - come up with extended set of cellular automata rules to use and combine to create images
    - image encodes a particle behaviour
  - ~~for generating images, limit number of shapes available to use~~

___

- **Philosophy**
  - What does it mean for a pattern/identity to exist?

___

- **Art**
  - new letter->wave/shape conversion
    - still aesthetic, but easier to understand
  - create map of sense conversions
    - list all forms of synaesthesia and use transitivity to convert from one sense to another not directly connected
  - given colour palette -> construct piece of music
  - what does it mean to "add", "subtract", or "multiply" short pieces of music
    - create pieces of music based on smaller pieces -- able to create structure?
  - have grid of all genres and generate heat map based on how often I listen to each one
  - ~~music classification program that uses my system~~
    - ~~also caluclated average spectrograms of songs in each genre~~

___

- **Optimization**
  - road crossing problem
    - If you want to cross the road to get from A to B, what is the optimal path to take?
    - To minimize total time, go alone diagonal from A to B.
  - design *optimal* comparative sorting algorithm
    - best method for overall accuracy (of three tested) is to split all choices into groups of 4, then choose best from each group, then put each of the winners in a new group.
    - repeatedly show user subset of data and have them approximately rank them, then use PageRank-like algorithm
    - Is the purpose to actually sort or for a group of people/person to choose a single best item?
  - design new keyboard method/type
  - write program to find optimal shortenings of words (for a given corpus) while maintaining uniqueness
  - at the highest level of an optimized system, behaviour should appear random
  - simulation to test optimal exploration policies
    - extension of Levy flights? (non-straight paths?)
  - design optimal character sets
    - in terms of writing speed
    - ~~use word2vec skipgram algo to find encodings for characters and base char set off of it~~

___

- **Simulations**
  - design simulation to study communication
    - evolve creatures when it is to their benefit to communicate
  - create artificial organisms which exhibit pink noise
  - design sim where subsytems act autonomously, but sync up every once in a while to achieve something
  - socio-emotional model
    - person Pa has emotion a, person Pb has emotion b -- how do they interact?
    - already done? -- http://personality-project.org/r/simulating-personality.html
  - ~~fully cts version of Game of Life~~
    - ~~use to generate music~~
  - "social interactions are represented by a theoretical game played by an individual and other individuals it is connected to"
  - agents are avg. of N closest friends
    - randomly like or dislike people
    - want to be dissimilar from people you don't like

___

- **Uncategorized**
  - ~~plot academic studies in subject space -- use word2vec~~
  - "closing the gap"
    - buy eeg and train for typing

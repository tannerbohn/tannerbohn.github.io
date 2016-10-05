---
layout: page
comments: false
title:  "Ideas"
permalink: /ideas/
---
- **Machine Learning**
  - Reinforcement Learning
    - how to learn sub-policies -- infinitely nestable?
      - similar to options idea
  - Text/Language
    - test out SQuAD dataset (paragraphs, questions, and answer ranges)
    - choose minimal set of sentences form article needed to answer questions about text
      - to create questions, remove word from sentence, and get network to guess it
    - calculate doc sentence importance scores
      - extract keywords and for each sentence, calculate prob that it is a def'n of a keyword
        - for large texts, can probably use simple method and represent sentences with histogram
    - how does word sound relate to sentiment? can you predict the sentiment of an arbitrary word?
    - convert between text and music
      - usewavenet and train/initialize with musical voices
    - word web
      - improve connection strength algorithm
      - add support for n-grams
    - analyse large list of wiki pages for certain characteristics
      - rate pages by some important sclaes (intelligence, science, politics, etc.)
    - use autoencoder for text summarization
      - ~~RNN?~~
      - what does it mean if a sentence has a large reconstruction error?
  - Images
    - train CNN to find shortest path in some environment/maze -- need to be recurrent?
    - what space do artistic styles reside in?
      - correlations between conv. filter activations? (at multiple scales -- and between scales)
      - train NN to learn to create new painting styles
    - ~~train autoencoder on lots of random chunks from image, and create demo where you can "black out" pieces and have it inpaint~~
    - ~~generate image based on topic (colour, texture, etc.)~~
      - ~~has already been done - neural network mapping sentence/words to image~~
    - multiscale image generator
      - similar to RL idea, learn multi-scale policies for drawing image
      - convert img to alg (cellular automata) and apply at multiple scales (by increasing resolution?)
  - Neuroscience/Meta
    - how to avoid catastrophic learning?
      - how does the brain do it? store info in both hippocampus and cortex
      - each neuron or connection has its own learning rate -- older memories change less?
    - evolve strategy for neurons modifying their connections
    - self-optimizing program/AI
    - what function would "brain waves" have in an ANN?
      - "communication through synchronization"
      - duing deep sleep, signals sent from hippocampus -> thalamus -> cortex hundreds of times
    - running memories in reverse during sleep is like creating explanative model instead of predictive one
      - humans are compelled to solve credit assignment problem
  - pattern recognition
    - feed instances of pattern(s) through autoencoder, then use clustering algorithm to detect unique families of patterns
      - use to study contagion dynamics - recognize distinct behaviours
      - train autoencoder on prev data, and whenever reconstruction error is high, there is a potential outlier
  - Math
    - learn optimal function interpolator
    - predict continued fraction limits (possible?)
      - find closed forms
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
      - what reward function do humans start with?
        - hunger, safety -> later in life we learn proxies for these (i.e. do well at job -> money -> food)
        - mind-body connection provides reward interface
          - how do humans know to interpret signals from body as positive or negative? (if a person didn't know hunger -> death, would they eat?)
            - humans likely carried over ability to interpret signals from evolutionary ancestors (i.e. specified in DNA)
        - another primative reward: variation is better than nothing (leads to creativity and curiosity?)
      - evolutionary opt is *perfect* for creating creatures that "learn to learn"
        - continued existence is the ultimate reward function (agents/creatures/DNA required to avoid death/extermination)
        - give neurons ability to differentiate themselves
          - differentiation depends on signals from nearby neurons?
    - use "small world" type of connection dist'n
      - what does weight matrix look like?
      - is this what human connectome looks like?

___

- **Idea Management**
  - MindMap
    - write program to automatically convert links or ideas file to mindmap?
    - be able to create groups and subgroups
      - expand a node into multiple nodes?
    - when saving, make sure every edge is captured
    - move around in 3 dimensions? (perfect application for VR)
    - have separate file for mindmap text and other text
      - special tiles linked to external files?
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
      - anthropomorphization
      - eye contact -> oxytocin
      - dogs, shared intentionality (pointing)
      - study attachment theory
      - make mistakes
      - reliance on human/user
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
      - interpret as a cellular automata definition
      - convert to lower resolution and parse into cellular automata rules
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
      - come up with lots of aesthetic short tunes and analyse to try find patterns
      - function to measure devotion to a single key?
  - have grid of all genres and generate heat map based on how often I listen to each one
  - ~~music classification program that uses my system~~
    - ~~also caluclated average spectrograms of songs in each genre~~

___

- **Optimization**
  - road crossing problem
    - If you want to cross the road to get from A to B, what is the optimal path to take?
    - To minimize total time, go alone diagonal from A to B.
      - What does the path look like for partial weighting?
  - design *optimal* comparative sorting algorithm
    - best method for overall accuracy (of three tested) is to split all choices into groups of 4, then choose best from each group, then put each of the winners in a new group.
      - easily generalizable -- but how do you sort all items (instead of just finding the single best)?
    - repeatedly show user subset of data and have them approximately rank them, then use PageRank-like algorithm
    - Is the purpose to actually sort or for a group of people/person to choose a single best item?
  - design new keyboard method/type
  - write program to find optimal shortenings of words (for a given corpus) while maintaining uniqueness
  - at the highest level of an optimized system, behaviour should appear random
  - simulation to test optimal exploration policies
    - extension of Levy flights? (non-straight paths?)
  - design optimal character sets
    - in terms of writing speed
      - ~~limited to aesthetic characters with phonetic grouping~~
      - evolve curves that are distinct and fast to write
    - ~~use word2vec skipgram algo to find encodings for characters and base char set off of it~~

___

- **Simulations**
  - design simulation to study communication
    - evolve creatures when it is to their benefit to communicate
  - create artificial organisms which exhibit pink noise
  - design sim where subsytems act autonomously, but sync up every once in a while to achieve something
  - socio-emotional model
    - person Pa has emotion a, person Pb has emotion b -- how do they interact?
      - use OCEAN vector?
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

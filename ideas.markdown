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
      - to create questions, remove word from sentence, and get network to guess it (imputation)
    - calculate doc sentence importance scores
      - extract keywords and for each sentence, calculate prob that it is a def'n of a keyword
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
      - what do GANs and VAEs have in common? both generate distributions? another way?
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
      - evolutionary opt is *perfect* for creating creatures that "learn to learn"
    - use "small world" type of connection dist'n
      - what does weight matrix look like?
      - is this what human connectome looks like?
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/B2.png" width="15"> learning to learn to learn ... to learn
    - this is essentially how human intelligence came about and acts -> how can this process be implemented at the limit case?
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/C2.png" width="15"> evolve recursive neural grid to maximise entropy of states over time
    - this will have the effect of "prolonging life"
    - use multiscale entropy (in both time and space?)
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/C2.png" width="15"> use "multisensory" autoencoder to find shared encoding for many streams
    - allows for interpretation of one stream as any other
    - this has already been done with universal langueage translator?
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/B2.png" width="15"> design a "cell" that when combined with others can adapt and learn
    - undergoes period of differentiation?
    - use optimization to determin structure of cell?
      - specifics of cell are fine-tunes during lifetime (learning)
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/B2.png" width="15"> classify windows of stock market by MSE curves

___

- **Idea Management**
  - MindMap
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/B2.png" width="15"> write program to automatically convert links or ideas file to mindmap?
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/C2.png" width="15"> be able to create groups and subgroups
      - expand a node into multiple nodes?
    - when saving, make sure every edge is captured
    - move around in 3 dimensions? (perfect application for VR)
    - have separate file for mindmap text and other text
      - special tiles linked to external files?
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/B2.png" width="15"> suggest links between notes? common terms?
    - use #url to denote that a note is a url, and can be opened (how?)
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/A2.png" width="15"> summarize all thoughts in 4 words or less (automate?)
  - ~~have main ideas.txt and automatically convert to webpage like linksaver~~
    - ~~allow linking between areas?~~
  - how to deal with different types of notes?
    - ex. project ideas, half-ideas, questions, misc. notes?
    - add tags, change colour

___

- **Human Intelligence/Psychology**
  - what are indicators of only* intelligence?
    - things that might be correlated with it include: reaction time, vocabulary, spatial reasoning
    - make use of analogies of increasing complexity (see evernote pages about reasoning behind this...)
  - generate bounded sequences of arbitrary complexity to test intelligence/pattern recognition
  - what is the difference in maximum "capacity" of brains that can and cannot alter structure/synapse strength?
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
  - branching structure and geometry of neurons hints at the algorithms they run
  - hypothesis: short term memory stores filters (pattern recognizers), which at night are transferred to neocortex
    - it creates filters there which respond to the same things
  - where does Maslow's hierarchy of needs come from?
    - does it always appear for complex conscious beings?
    - love & belonging and esteem seem unique to humans (provided by evolution), however the following may apply generally to intelligent entities:
      - physiological needs, safety -> without these, continued existence is not guaranteed
      - self-actualization -> maximize efficiency of goal-attainment
  - design experiment to test long-term memory recall speed when moving and not moving eyes
  - estimate the rate of time passage during various mental activities
    - need to only see true durations afterward to avoid consciously counteracting biases
    - uniformly generate time durations in (0, 10] seconds
    - plot curve of guess vs. real duration
  - how do functional modules form in brain?
    - result of speed and energy optimisation?

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
  - represent image as histogram in pattern-space (similar to filter activations?)
    - what would a path through the pattern-space look like?

___

- **Philosophy**
  - What does it mean for a pattern/identity to exist?
  - calculate parameters of hedonic adaptation
    - maximize happiness by balancing positive and negative experiences of certain magnitudes

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
  - why do birds sing?
    - how are those signals better than random series of notes?
      - it could be that since they are repeated, it has low enough large scale entropy to resemble non-randomness
      - music could be culturally defined, as opposed to satisfying some universal criterion
  - music generation with multiscale entropy
    - ~~apply entropy curve fitting to both notes and derivatives~~
    - ~~train model to predict rating given entropy curves~~
      - ~~can then generate songs which which try to maximize this~~
      - ~~to start model training, perform blinded test to see which MSE curves are the most aesthetic~~
    - ~~perform note-level fine-tuning after global optimization~~
    - ~~use self-optimizing optimizer~~
      - ~~keep track of which changes/actions work well and treat them like bandit arms~~
    - augment kNN regressor with local linear extrapolation/interpolation
      - ~~take average of many calculations done with many nearby pairs~~
      - this idea needs some refining... if there is noise, then predictions near two points can diverge
    - manually compose a bunch of random melodies and track multiscale entropy
  - why do humans enjoy non-utilitous things?
    - ex. art (depictive and abstract)
    - because it displays concepts and patterns which we have learned to find good?
    - why do we enjoy wordplay?
      - because we are able to undergo being confused/lacking understanding to understanding, a process we have learned to enjoy (survival)
  - why do we enjoy certain artistic styles independent of their specific content?
    - activation of lower level patterns which we enjoy?
  - generate a music playlist that acts a path through emotion-space
    - this may help in changing listeners emotion because it first gains traction by relating, and then slowly shifts to target emotion

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
    - nestable characters
  - generate langauge with as much structure as possible?
  - ~~make MSE curve generation program with exponential scaling~~

___

- **Simulations**
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/A2.png" width="15"> design simulation to study communication
    - evolve creatures when it is to their benefit to communicate
  - create artificial organisms which exhibit pink noise
  - design sim where subsytems act autonomously, but sync up every once in a while to achieve something
  - socio-emotional model
    - person Pa has emotion a, person Pb has emotion b -- how do they interact?
      - use OCEAN vector?
    - already done? -- http://personality-project.org/r/simulating-personality.html
  - ~~fully cts version of Game of Life~~
    - ~~use to generate music~~
  - what happens when you can fix cells in GOL?
    - use fixable cells as input to system?
  - generate automata which generates images with specific multiscale entropy curves
  - "social interactions are represented by a theoretical game played by an individual and other individuals it is connected to"
  - agents are avg. of N closest friends
    - randomly like or dislike people
    - want to be dissimilar from people you don't like
  - what forces promote and prevent formation of social structures of different levels?
    - family -> clan -> city -> country -> global
  - simulate multilevel cooperation evolution (ex cells -> ... ->bodies -> communities)
  - dynamics of agents with different degrees of common knowledge
    - "momentum trades" of stocks have lower level
  - ~~government substructure optimization~~
    - ~~see https://www.evernote.com/shard/s267/nl/34201306/9002cf9d-1968-4af4-be2f-2a5909d9c758?title=Government%20Substructure%20Optimization~~

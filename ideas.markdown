---
layout: page
comments: false
title:  "Ideas"
permalink: /ideas/
---

___

- **Machine Learning**
  - Reinforcement Learning
    - how to learn sub-policies -- infinitely nestable?
  - Text/Language
    - test out SQuAD dataset (paragraphs, questions, and answer ranges)
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> choose minimal set of sentences form article needed to answer questions about text
    - calculate doc sentence importance scores
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> how does word sound relate to sentiment? can you predict the sentiment of an arbitrary word?
    - convert between text and music
    - create word web generator
    - analyse large list of wiki pages for certain characteristics
    - use autoencoder for text summarization
    - ~~automated knowledge finder~~
    - ~~create sentence parsing algorithm~~
    - ~~create text compression so that any subset of lyrics is approximation of whole~~
  - Art/Images
    - train CNN to find shortest path in some environment/maze -- need to be recurrent?
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> what space do artistic styles reside in?
    - ~~train autoencoder on lots of random chunks from image, and create demo where you can "black out" pieces and have it inpaint~~
    - ~~generate image based on topic (colour, texture, etc.)~~
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> multiscale image generator
  - pattern recognition
    - feed instances of pattern(s) through autoencoder, then use clustering algorithm to detect unique families of patterns
  - Math
    - learn optimal function interpolator/extrapolator
    - predict continued fraction limits (possible?)
  - Generative Adversarial Networks
    - apply to text?
    - try generate more of my art
    - alternative to GANs? (VAEs? -> use idea of learning distribution)
  - ~~train a clustering algorithm with autoencoder~~
  - use idea of ant chemical trains for NN memory augmentation
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> train decorrelated NNs
    - consecutively train sub-nets to both maximize variance between sub-net predictions and performance of each sub-net
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> design game where solution requires agents to posess characteristics of self-awareness and ability to communicate
    - put coloured mark on agents have they have to ask other agents what colour their own dot is (or use mirror?)
  - learn entity motivations/needs as predictive/explanative model
  - implement NN that works and learns in real time
    - fully recursive?
    - might need low cycles/sec when initially learning
    - need gating mechanisms?
    - learning how to learn -- given response from env., learn how to use it to improve future performance
    - use "small world" type of connection dist'n
  - learning to learn to learn ... to learn
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> create system which simultaneously optimizes itself on every possible level
    - this is essentially how human intelligence came about and acts -> how can this process be implemented at the limit case?
  - evolve recursive neural grid to maximise entropy of states over time
    - this will have the effect of "prolonging life"
    - use multiscale entropy (in both time and space?)
  - use "multisensory" autoencoder to find shared encoding for many streams
    - allows for interpretation of one stream as any other
    - this has already been done with universal langueage translator?
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> design a "cell" that when combined with others can adapt and learn
    - how to represent structure and dynamics?
    - undergoes period of differentiation?
    - use optimization to determine structure of cell?
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15">  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> classify windows of stock market by MSE curves
  - ~~instead of true recursive or or forward neural network, have a set jump-back length~~
    - ~~allows fixed length computation time but offers more complexity~~
    - ~~does this give any benefit?~~
    - ~~what are the benefits of recursive over feed forward?~~

___

- **Idea Management**
  - MindMap
    - ~~create notes, connect them, edit, delete, be able to zoom in and out, pan~~
    - write program to automatically convert links or ideas file to mindmap?
    - be able to create groups and subgroups
    - ~~when saving, make sure every edge is captured~~
    - move around in 3 dimensions? (perfect application for VR)
    - have separate file for mindmap text and other text
    - suggest links between notes? common terms?
    - use #url to denote that a note is a url, and can be opened (how?)
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> summarize all thoughts in 4 words or less (automate?)
  - ~~have main ideas.txt and automatically convert to webpage like linksaver~~
    - todo: allow linking between areas?
  - how to deal with different types of notes?
    - ex. project ideas, half-ideas, questions, misc. notes?
    - add tags, change colour
  - ~~in linksaver, should specific hashtags have their own icons? (or the hashtag text replaced with something?)~~
    - todo: is there a better way to have one note with multiple parents?

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
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15">  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> design experiment to test long-term memory recall speed when moving and not moving eyes
  - estimate the rate of time passage during various mental activities
    - need to only see true durations afterward to avoid consciously counteracting biases
    - uniformly generate time durations in (0, 10] seconds
  - how do functional modules form in brain?
    - result of speed and energy optimisation?
  - ~~find where the psychological experience of day transition comes from~~
    - ~~Where does the transition between days occur?~~
    - ~~What's the minimum length of time you can sleep to experience the shift?~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/23dca9b2-d700-4038-9b95-085730d8847e?title=Day%20transition%20experiment)~~
  - what correlation is there between the rate at which someone can manually generate random numbers and their intelligence?
    - also include a measure of the sequene randomness in the correlation calculations
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> it would be fun to analyse the random sequences people produce and see how predictable different people are
    - measure concentration level over time
    - as the amount of information memorized increased in one sitting (or over a single day), how does the time required to memorize something increase

___

- **Personal Assistants**
  - Fermi
    - basic drives, morals, and emotions
    - learning "pet" algorithm/program
    - convert words to notes/freqs
    - how do you impart love?
    - search "communication space" to make program that seems to show intention/human-ness/sentience
    - convert between mood and line shape
  - start Ada (successor to Fermi)
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> create assistant with email as interface
    - be able to send queries for various programs
    - put program on raspberry pi to be always-on
    - host various experiments

___

- **Math**
  - Image multiplier (Encryption?) Prime images?
  - Interpolation/extrapolation with ASMD
    - what functions do the ASMD produce?
    - modify algorithm to allows for small amount of noise in data
  - closed form finding
    - ~~recursive closed form finder for arbitrary numbers~~
    - closed forms of general continued fractions
  - geometrically motivated number system (baseless?)
  - make recursive ASMD algorithm more flexible
    - loosen bounds to approximately match sequences (apply to fuzzier data)
  - function modifier for numerical integration accuracy
    - transform curve to smooth bumps -- converge to more smooth or uniform curve?
    - look for volume preserving operation that can be applied to continuous data
  - ~~improve image multiscale entropy algorithm~~
    - ~~normalize to max/min possible~~
    - ~~more rigorous definition~~
  - ~~moving guess~~
    - ~~You find someone in a state at time t0. You observe them in the state for duration t. Given the person has been in there for (t + x), what is the most likely total time they have been in the state?~~
  - sequences are metaphors are mappings
  - ~~leaning line problem~~
    - ~~see [wordpress](https://tannerbohn.wordpress.com/2015/04/03/leaning-line-problem/) or [evernote](https://www.evernote.com/shard/s267/nl/34201306/0aa75294-4d1b-4c03-99ce-21f5d4339a5f?title=Leaning%20line%20problem)~~
  - ~~observe distribution of eigenvalues of various types of matrices~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/bd64d36f-f488-40d2-99be-ec5fe1e8f332?title=distribution%20of%20eigenvalues%20of%20various%20matrices)~~
  - ~~calculate deflection of bar~~
    - ~~What is the equation for the deflection by gravity of a bar fixed at one end?~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/c545b220-2b2f-4d6f-bb53-246c34db972c?title=Deflection%20of%20Bar) for resources~~
  - ~~calculate density of prime powers~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/e2a01499-3995-4332-a33e-faad62549307?title=Prime%20Power%20Density)~~
  - ~~create math pattern puzzle game~~
    - ~~conceptually simple, but possibly difficult~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/5b878294-7211-4780-924d-022296c958d2?title=Math%20Pattern%20Puzzle)~~

___

- **Images**
  - convert image to algorithm, recursively apply
    - how to ensure fixed point existence? -- if none, can view time series
  - convert simulation to image
    - represent state as a position in image as well as colour
    - for each position in image, convert to state alpha, see what state alpha goes to (beta), and colour the position of alpha as beta's colour
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15">  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> use symmetry & asymmetry rules to generate image
  - algorithm image isomorphism/conversions
    - come up with extended set of cellular automata rules to use and combine to create images
    - image encodes a particle behaviour
  - ~~for generating images, limit number of shapes available to use~~
  - represent image as histogram in pattern-space (similar to filter activations?)
    - what would a path through the pattern-space look like?

___

- **Philosophy**
  - What does it mean for a pattern/identity to exist?
  - calculate parameters of hedonic adaptation
    - maximize happiness by balancing positive and negative experiences of certain magnitudes
  - origins of consciousness, sentience, existence of goals:
    - see [evernote: Project Lithium](https://www.evernote.com/shard/s267/nl/34201306/005833c4-3e05-4159-b064-57a121b2e800?title=PrLi%3A%20About%20%26%20Outline)

___

- **Art**
  - new letter->wave/shape conversion
    - still aesthetic, but easier to understand
  - create map of sense conversions
    - list all forms of synaesthesia and use transitivity to convert from one sense to another not directly connected
  - given colour palette -> construct piece of music
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> the inverse might be more interesting, and easier
  - what does it mean to "add", "subtract", or "multiply" short pieces of music
    - create pieces of music based on smaller pieces -- able to create structure?
  - have grid of all genres and generate heat map based on how often I listen to each one
    - changes over time, so you could instead chart a path through genre-space over time
  - ~~music classification program that uses my system~~
    - ~~also caluclated average spectrograms of songs in each genre~~
  - why do birds sing?
    - how are those signals better than random series of notes?
  - music generation with multiscale entropy
    - ~~apply entropy curve fitting to both notes and derivatives~~
    - ~~train model to predict rating given entropy curves~~
    - ~~perform note-level fine-tuning after global optimization~~
    - ~~use self-optimizing optimizer~~
    - augment kNN regressor with local linear extrapolation/interpolation
    - manually compose a bunch of random melodies and track multiscale entropy
  - why do humans enjoy non-utilitous things?
    - ex. art (depictive and abstract)
    - because it displays concepts and patterns which we have learned to find good?
    - why do we enjoy wordplay?
    - why do we enjoy certain artistic styles independent of their specific content?
  - playlist generation
    - ~~Playlist generation using genre&band similarity rating (2012.5)~~
    - generate a music playlist that acts a path through emotion-space
  - possible to metric for image aesthetics?
    - possible factors may be density, repetition, nesting, balance of pattern and chaos
    - Karpathy already did something similar to this with instagram photos or people
  - ~~create mapping from personal relationship type to colours~~
  - ~~create program which calculate multiscale entropy of images, and generate images with specific MSE curves~~
    - ~~see [evernote](https://tannerbohn.wordpress.com/2015/12/17/multiscale-image-entropy/)~~
    - ~~also try using exponentially scaled entropy curves (faster to calculate and easier to satisfy when generating images)~~

___

- **Optimization**
  - ~~road crossing problem~~
    - ~~If you want to cross the road to get from A to B, what is the optimal path to take?~~
    - ~~To minimize total time, go alone diagonal from A to B.~~
    - ~~solution: see snell's law~~
  - design *optimal* comparative sorting algorithm
    - best method for overall accuracy (of three tested) is to split all choices into groups of 4, then choose best from each group, then put each of the winners in a new group.
    - repeatedly show user subset of data and have them approximately rank them, then use PageRank-like algorithm
    - Is the purpose to actually sort or for a group of people/person to choose a single best item?
    - ~~create algorithm which asks used to compare many elements to eachother, and then uses iterative algorithm to find ordering for elements which satisies the criterion~~
  - design new keyboard method/type
    - ~~write program to find optimal arrangement of keys~~
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15">  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> write program to find optimal shortenings of words (for a given corpus) while maintaining uniqueness
    - need to figure out how to shorten words (can just remove unnecessary vowels)
    - balance between marking it hard to remember meaning of shortening and overall length of text
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/insight1.png" height="15"> at the highest level of an optimized system, behaviour should appear random
  - simulation to test optimal exploration policies
    - extension of Levy flights? (non-straight paths?)
  - design optimal character sets
    - in terms of writing speed
    - ~~use word2vec skipgram algo to find encodings for characters and base char set off of it~~
    - nestable characters
    - a successful char set seems to require "landmark" characters which provide visual variation that assists in learning
    - combination of edges in a possible graph (try different graphs)
    - one attempt: [evernote](https://www.evernote.com/shard/s267/nl/34201306/ef3aee2d-647f-43c8-ae59-a2badfcd72bc?title=character%20set%2Fwriting%20system%20optimization)
    - ~~create an aesthetic character set which can be written without lifting pen~~
  - generate langauge with as much structure as possible?
  - ~~make MSE curve generation program with exponential scaling~~
  - ~~find optimal locations on field to sample soil data from in consecutive years~~
    - ~~if you assume that data from previous years is not entirely different from the next years, you can sample in new spots to accumulate data over time~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/29829134-0227-42ad-bdf8-8bc9323f35cc?title=Field%20Problem)~~
  - ~~find optimal parameters for spaced repetition~~
    - ~~want to minimize total time spend practicing, but maximize amount remembered~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/8326d96d-4ec3-439d-a256-d6b119ffe1c3?title=Optimal%20Spaced%20Repetition)~~
  - ~~given the average colour of each row and column of an image, create a new one which has similar values (2012.12)~~
  - ~~write task scheduling program~~
    - ~~given a set of tasks which each have an expected duration, difficulty, importance, etc., come up with the optimal schedule for achieving all of them~~
    - ~~while there is an easier solution using dynamic program, my solution functions are more of a prediction of what someone would actually do (i.e. wait until something is of sufficient immediacy)~~
  - ~~write program to calculate various statistics of existing songs, and generate new ones with similar properties~~
    - ~~can use average note, std. dev of notes, avgerage nth derivative, std. dev of nth derivative~~

___

- **Simulations**
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/good3.png" width="15"> design simulation to study communication
    - evolve creatures when it is to their benefit to communicate
  - create artificial organisms which exhibit pink noise
  - design sim where subsytems act autonomously, but sync up every once in a while to achieve something
  - socio-emotional model
    - person Pa has emotion a, person Pb has emotion b -- how do they interact?
    - already done? -- http://personality-project.org/r/simulating-personality.html
  - ~~fully cts version of Game of Life~~
    - ~~use to generate music~~
  - ~~what happens when you can fix cells in GOL?~~
    - ~~use fixable cells as input to system?~~
  - generate automata which generates images with specific multiscale entropy curves
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> can just try tweaking initial condition in fixed-GOL simulation to achieve curve
  -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/insight1.png" height="15"> "social interactions are represented by a theoretical game played by an individual and other individuals it is connected to"
  - agents are avg. of N closest friends
    - randomly like or dislike people
    - want to be dissimilar from people you don't like
  - what forces promote and prevent formation of social structures of different levels?
    - family -> clan -> city -> country -> global
  - simulate multilevel cooperation evolution (ex cells -> ... ->bodies -> communities)
  - dynamics of agents with different degrees of common knowledge
    - "momentum trades" of stocks have lower level
  - ~~government substructure optimization~~
    - ~~see [evernote](https://www.evernote.com/shard/s267/nl/34201306/9002cf9d-1968-4af4-be2f-2a5909d9c758?title=Government%20Substructure%20Optimization), also [wordpress](https://tannerbohn.wordpress.com/2015/05/30/abstract-government-substructure-optimization/)~~
  - ~~wealthy inequality simulation~~
    - ~~what causes inequality to occur?~~
    - ~~in some society, what does the distribution of wealth tend towards?~~
    - ~~done by others -- lognormal distribution of wealth?~~
  - ~~social particle simulation~~
    - ~~simulate abstract people with social/antisocial properties. After spending time around other people, they become antisocial and move away from people. After being alone for a while, they want to socialize again.~~
    - ~~see [wordpress](https://tannerbohn.wordpress.com/2015/04/03/socialparticlesimulation/) and [evernote](https://www.evernote.com/shard/s267/nl/34201306/caba1d23-f82c-48cd-b8a7-c5463c5538ad?title=Social%20Particle%20Simulation)~~
  - ~~simulate two competing infections~~
    - ~~agents have an infection value from -1 (disease A) to +1 (disease B)~~
  - ~~simulate relationships between agents~~
    - ~~agents move towards they are "attracted" to and away from others?~~
    - ~~agents randomly change who they are attracted to~~
    -  <img src="https://raw.githubusercontent.com/tannerbohn/tannerbohn.github.io/master/assets/easy2.png" height="15"> todo: add "genders", so that each agent is attracted to some subset of other types

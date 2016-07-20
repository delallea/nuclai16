If UNICODE error type this in the Docker image:
	export LC_ALL=C
	export LC_ALL=en_US.UTF-8
	export LC_ALL=C.UTF-8

(NB: does not seem to really work...)

There is a MemoryError when trying to train the model. One option could be to figure out how to increase Docker memory.
Another is to just reduce the size of tweets78k.txt, e.g. with:
	cat tweets78k.txt | grep robotics > new_data.txt
(then rename new_data.txt into tweets78k.txt)

- Preprocessing is very important: add a "START" and "STOP" characters, removing hash, filtering duplicates, replacing characters with <0.05% frequency with UNK
- Sliding window: seqlen = 40, seqstep = 3 means we use sliding windows of 40 characters every 3 characters
- Network predicts the 41th character
- Vectorization = turn each character into a one-hot vector => memory-hungry
- See paper by Alex Graves http://arxiv.org/abs/1308.0850
- The "temperature" is used to introduce randomness: near-zero => pick highest probability character, higher => can pick less likely characters
- Can set seed to always pick same sentences in order to compare results
- Works better with few symbols in your grammar
- Use 0-padding to work around the fixed-size length constraint, but block gradient to prevent 0's from affecting training
- Hack for upper / lowercase: convert to lowercase but add a special character to indicate that next one is uppercase


2nd part of the workshop:
- See paper "A neural conversational model" http://arxiv.org/abs/1506.05869
- Ex. of implementation: seq2seq
- The example in the workshop is very basic: it learns to map an 8-bit sequence to itself. Note that it does not even manage to do that perfectly!
- Tweaking the batch size may help
- See examples: https://github.com/nicolas-ivanov/seq2seq_chatbot_links
- Overall this tech is still not working that great, and takes a very long time to train
- Insight from Alex: on images the network blurs the output to minimize the MSE. On text it does somewhat of the same, i.e. tends to go with short answers that are the "average" answers. On images recent work introduced an extra network that computes the error instead of using MSE, which gives better results ("perceptual loss").
- Roelof Pieters says that currently doing clustering on the middle layer does not work so well, because of the constraints

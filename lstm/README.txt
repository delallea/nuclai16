If UNICODE error type this in the Docker image:
	export LC_ALL=C
	export LC_ALL=en_US.UTF-8

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
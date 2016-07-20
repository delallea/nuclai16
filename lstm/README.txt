If UNICODE error type this in the Docker image:
	export LC_ALL=C

There is a MemoryError when trying to train the model. One option could be to figure out how to increase Docker memory.
Another is to just reduce the size of tweets78k.txt, e.g. with:
	cat tweets78k.txt | grep robotics > new_data.txt
(then rename new_data.txt into tweets78k.txt)

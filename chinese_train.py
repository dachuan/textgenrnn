from textgenrnn import textgenrnn
textgen = textgenrnn(name="poem")

textgen.reset()
textgen.train_from_file(
	file_path = './datasets/c_poem.txt',
	new_model = True,
	num_epochs = 30,
	word_level = False,
	rnn_bidirectional = True,
	max_length = 10,
	train_size = 0.8,
	dropout = 0.2
)

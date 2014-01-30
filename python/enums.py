def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

CLASSIFIER_NAMES = enum('NAIVE_BAYES', 'SUPPORT_VECTOR_MACHINES')
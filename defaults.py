# Data parameters
LANGUAGE_PAIR = ("en", "de")
D_MODEL = 512

# Optimizer configuration
LEARNING_RATE = 1e-5
BETA1 = 0.9
BETA2 = 0.98
EPS = 1e-9

# Scheduler params
LR_REDUCTION_FACTOR = 0.5

# Training parameters
BATCH_SIZE = 256
NUM_WARMUP = 40
NUM_EPOCHS = 100

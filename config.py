KB_PATH = './data/kb.txt'
ENTITY_VOCABULARY_PATH = './data/entity_vocab.pickle'
RELATION_VOCABULARY_PATH = './data/relation_vocab.pickle'


# training configs

TEST_SPLIT = 0.1
VALIDATION_SPLIT = 0.001
TRAIN_LOG_ITERATIONS = 25
EPOCHS = 100
BATCH_SIZE = 128
TEST_BATCH_SIZE = 1000


# model configs

HIDDEN_DIMENSION = 200
SAVED_MODELS_PATH = 'data/saved_models'

# evaluation configs
PREDICTION_THRESHOLD = 0.2
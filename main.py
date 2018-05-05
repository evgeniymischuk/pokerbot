import config
from api.modes.gaming_mode import GamingMode
from api.modes.learning_mode import LearningMode
from api.modes.predicting_mode import PredictingMode

if __name__ == '__main__':
    if config.PLAYING_MODE:
        GamingMode()
    elif config.LEARNING_MODE:
        LearningMode()
    elif config.PREDICTING_MODE:
        PredictingMode()

import numpy as np
from smt.surrogate_models import RBF


ctarr = np.array([[0.44378727, 0.39780505, 0.36492063, 0.34594835, 0.3396722,  0.34594835, 0.36492063, 0.39780505, 0.44378727],
    [0.39932019, 0.35311678, 0.32064848, 0.30098334, 0.29438502, 0.30098334, 0.32064848, 0.35311678, 0.39932019],
    [0.36758215, 0.32161359, 0.28733314, 0.26653243, 0.26000165, 0.26653243, 0.28733314, 0.32161359, 0.36758215],
    [0.34915371, 0.302356,   0.26694568, 0.24719677, 0.24107487, 0.24719677, 0.26694568, 0.302356,   0.34915371],
    [0.34362491, 0.29646818, 0.26162671, 0.24395124, 0.24127203, 0.24395124, 0.26162671, 0.29646818, 0.34362491],
    [0.35093121, 0.30455996, 0.27016854, 0.25233624, 0.24730365, 0.25233624, 0.27016854, 0.30455996, 0.35093121],
    [0.37112818, 0.32568599, 0.2924081,  0.27273809, 0.26669545, 0.27273809, 0.2924081,  0.32568599, 0.37112818],
    [0.40423353, 0.35873613, 0.32695655, 0.30772598, 0.30124198, 0.30772598, 0.32695655, 0.35873613, 0.40423353],
    [0.44986711, 0.4047771,  0.37241641, 0.35345569, 0.34720372, 0.35345569, 0.37241641, 0.4047771,  0.44986711]])

cparr = np.array([[0.38916783, 0.33762982, 0.30071029, 0.2787971,  0.27156899, 0.2787971, 0.30071029, 0.33762982, 0.38916783],
    [0.34174776, 0.29118858, 0.25548598, 0.23020456, 0.22114822, 0.23020456, 0.25548598, 0.29118858, 0.34174776],
    [0.30894789, 0.26005615, 0.21853485, 0.19303051, 0.18483138, 0.19303051, 0.21853485, 0.26005615, 0.30894789],
    [0.29067532, 0.23945315, 0.19879707, 0.17699394, 0.17056872, 0.17699394, 0.19879707, 0.23945315, 0.29067532],
    [0.28558827, 0.23334922, 0.19459788, 0.17535239, 0.170538,   0.17535239, 0.19459788, 0.23334922, 0.28558827],
    [0.29299708, 0.2421695,  0.20252804, 0.1824143,  0.17676598, 0.1824143, 0.20252804, 0.2421695,  0.29299708],
    [0.31348364, 0.26504093, 0.2249794,  0.20161817, 0.1945959,  0.20161817, 0.2249794,  0.26504093, 0.31348364],
    [0.34827829, 0.29825734, 0.2633885,  0.23960818, 0.23134359, 0.23960818, 0.2633885,  0.29825734, 0.34827829],
    [0.39757264, 0.34663548, 0.31036403, 0.28914374, 0.2822016,  0.28914374, 0.31036403, 0.34663548, 0.39757264]])
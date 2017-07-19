from Bio import SeqIO
import numpy as np
import csv
from collections import Counter
from string import ascii_uppercase
from Bio.SeqUtils import molecular_weight
from Bio.Alphabet import generic_protein
from Bio.Seq import Seq
from Bio.SeqUtils import IsoelectricPoint
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.preprocessing import normalize, scale, StandardScaler
from sklearn.metrics import f1_score, make_scorer, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.externals import joblib
import pickle
from matplotlib import pyplot as plt
import itertools
from collections import OrderedDict


exec(open('./helpers/plot_confusion_matrix.py').read())
exec(open('./helpers/features.py').read())
exec(open('./helpers/merge_dicts.py').read())
exec(open('./code/type_encoding.py').read())
exec(open('./code/prepare.py').read())

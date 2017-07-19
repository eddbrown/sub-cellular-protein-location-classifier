exec(open('require.py').read())

# Parameters
test_fraction = 0.2
CV_search_parameters = {'kernel':['linear','rbf'], 'C':[0.7,0.75,0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.20]}
CV_fold_number = 3

kernel = 'rbf'
numpy_random_seed = np.random.seed(0)
sklearn_test_split_random_state = 42

# Seed random generator
np.random.seed(numpy_random_seed)

# Load data
data = np.loadtxt('csvs/data.csv', delimiter=',', skiprows=1)
blind_data = np.loadtxt('csvs/blind_data.csv', delimiter=',', skiprows=1)

# Shuffle data
data = shuffle(data)

# Separate labelled data into features and labels
X = data[:, 1:]
y = data[:, 0]

# Split data in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction, random_state=sklearn_test_split_random_state)

joblib.dump(X_train, './pickles/x_train.pkl')
joblib.dump(X_test, './pickles/x_test.pkl')
joblib.dump(y_train, './pickles/y_train.pkl')
joblib.dump(y_test, './pickles/y_test.pkl')

# Fit transformation of data
scaler = StandardScaler().fit(X_train)

# Transform Training data
X_train = scaler.transform(X_train)

# Define Scorer
f1_scorer = make_scorer(f1_score, average='weighted')

# Create Grid search of parameters of k-fold validation
svc = SVC(probability=True)
clf = GridSearchCV(svc, CV_search_parameters, cv=CV_fold_number, scoring=f1_scorer)
clf.fit(X_train, y_train)

# Best Parameters
C_best = clf.best_params_['C']
kernel_best = clf.best_params_['kernel']
print('Cross Validation Kernel: {}'.format(kernel_best))
print('Cross Validation C Parameter: {}'.format(C_best))

# Create scaler and SVC pipline
pipeline = make_pipeline(scaler, clf)

# Save model and scaler
joblib.dump(pipeline, './pickles/model.pkl')

# Predict on test set
y_pred = pipeline.predict(X_test)
test_f1_score = f1_score(y_test, y_pred, average='weighted')
test_accuracy= accuracy_score(y_test, y_pred)

print('Test F1 Score: {0:.4f}'.format(test_f1_score))
print('Accuracy: {0:.4f}'.format(test_accuracy))

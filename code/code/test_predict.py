exec(open('require.py').read())

classifier = joblib.load('./pickles/model.pkl')
X_test = joblib.load('./pickles/x_test.pkl')
y_test = joblib.load('./pickles/y_test.pkl')

# Predict on test set
y_pred = classifier.predict(X_test)

# Performance Metrics
test_f1_score = f1_score(y_test, y_pred, average='weighted')
test_accuracy= accuracy_score(y_test, y_pred)
classification_report = classification_report(y_test, y_pred, target_names=LABELS)

# Confusion Matrix
confusion = np.array(confusion_matrix(y_test,y_pred)).astype(float)

plot_confusion_matrix(confusion, LABELS, normalize=True)
plt.savefig('images/confusion.png')

print('Test F1 Score: {0:.4f}'.format(test_f1_score))
print('Test Accuracy: {0:.4f}'.format(test_accuracy))

print(classification_report)

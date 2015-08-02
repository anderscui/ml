# the data set was downloaded from UCI repository:
# https://archive.ics.uci.edu/ml/datasets/Internet+Advertisements

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV


if __name__ == '__main__':
    df = pd.read_csv('../../data/ad.data', header=None)
    explanatory_vars = set(df.columns.values)
    response_var = df[len(df.columns.values)-1]
    explanatory_vars.remove(len(df.columns.values)-1)

    y = [1 if e == 'ad.' else 0 for e in response_var]
    X = df[list(explanatory_vars)]

    # deal with missing values
    X.replace(to_replace=' *\?', value=-1, regex=True, inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # print(len(X_train))
    # print(len(X_test))

    pipeline = Pipeline([
        ('clf', RandomForestClassifier(criterion='entropy'))
    ])

    parameters = {
        'clf__n_estimators': (5, 10, 20, 50),
        'clf__max_depth': (50, 150, 250),
        'clf__min_samples_split': (1, 2, 3),
        'clf__min_samples_leaf': (1, 2, 3)
    }

    grid_searcher = GridSearchCV(pipeline, parameters, n_jobs=1, verbose=1, scoring='f1')
    grid_searcher.fit(X_train, y_train)
    print('Best score: %0.3f' % grid_searcher.best_score_)
    print('Best parameters set: ')
    best_parameters = grid_searcher.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print('\t%s: %r' % (param_name, best_parameters[param_name]))

    predictions = grid_searcher.predict(X_test)
    print(classification_report(y_test, predictions))
from collections import defaultdict
from numpy import test
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import GridSearchCV


def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    param_grid = {
        'n_estimators' : [50, 100],
        'max_features' : ['auto', 'sqrt'],
        'max_depth': [20, 50, 100],
        'criterion': ['gini', 'entropy']
    }

    rfc = RFC()
   
    cv_rfc = GridSearchCV(
        estimator=rfc, 
        param_grid=param_grid,
        cv=5
        )

    cv_rfc.fit(X_train, y_train)

    return cv_rfc.best_estimator_


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


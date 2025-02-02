"""Module contain custom transformers to use them in pipeline."""

import numpy as np
# import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class DropColumn(BaseEstimator, TransformerMixin):
    """Class for dropping specified columns from DataFrame."""

    def __init__(self, variables: list[str]):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X = X.drop(self.variables, axis=1)
        return X


class LogTransformer(BaseEstimator, TransformerMixin):
    """Class for applying logarithmic transformation to specified columns."""

    def __init__(self, variables: list[str]):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for variable in self.variables:
            X[variable] = np.log(1 + X[variable])
        return X


class IsZeroIndicator(BaseEstimator, TransformerMixin):
    """Class for creating a binary indicator for zero values in specified columns."""

    def __init__(self, variables: list[str]):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for variable in self.variables:
            X[f'{variable}_is_0'] = np.nan
            X.loc[X[variable] == 0, f'{variable}_is_0'] = 1
            X.loc[X[variable] != 0, f'{variable}_is_0'] = 0
        return X



class Mapper(BaseEstimator, TransformerMixin):
    """Class for mapping values in specified columns using a dictionary."""

    def __init__(self, variables: list[str], mappings: dict[str, str]):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables
        self.mappings = mappings

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)
        return X


class SelectColumn(BaseEstimator, TransformerMixin):
    """Class for selecting specific columns from the DataFrame."""

    def __init__(self, variables: list[str]):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X[self.variables]
        return X
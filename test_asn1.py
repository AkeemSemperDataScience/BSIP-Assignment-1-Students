from asn1_function_sheet import age_splitter, effectSizer, cohortCompare
import pandas as pd
import numpy as np
import pytest

def test_age_splitter_1():
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    })
    df_below, df_above_equal = age_splitter(df, 'age', 40)
    assert df_below.shape[0] == 3
    assert df_above_equal.shape[0] == 2

def test_age_splitter_2():
    df = pd.DataFrame({
        'age': [18, 22, 27, 29, 31, 35],
        'name': ['A', 'B', 'C', 'D', 'E', 'F']
    })
    df_below, df_above_equal = age_splitter(df, 'age', 30)
    assert all(df_below['age'] < 30)
    assert all(df_above_equal['age'] >= 30)

def test_effectSizer_1():
    df = pd.DataFrame({
        'score': [10, 12, 14, 16, 18, 20],
        'group': ['A', 'A', 'A', 'B', 'B', 'B']
    })
    d = effectSizer(df, 'score', 'group')
    assert isinstance(d, float)
    assert d > 0  # Group B has higher scores

def test_effectSizer_2():
    df = pd.DataFrame({
        'value': [5, 7, 9, 11, 13, 15],
        'category': ['X', 'X', 'X', 'Y', 'Y', 'Y']
    })
    d = effectSizer(df, 'value', 'category')
    assert isinstance(d, float)
    assert d > 0  # Category Y has higher values

def test_cohortCompare_1():
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45, 50],
        'height': [160, 165, 170, 175, 180, 185],
        'hair': ['brown', 'blonde', 'blonde', 'red', 'brown', 'blonde']
    })
    cohorts = ["hair"]
    result = cohortCompare(df, cohorts)
    result_set = {}
    for cohort_name, metrics in result.items():
        result_set[cohort_name] = metrics
    #assert isinstance(result, pd.DataFrame)
    #assert result.shape[0] == len(cohorts)
    test_1 = result_set["hair_blonde"].getStats()
    test_1_mean = test_1["mean"]
    print(test_1_mean)


def test_cohortCompare_2():
    df = pd.DataFrame({
        'age': [18, 22, 27, 29, 31, 35, 40, 45],
        'weight': [50, 55, 60, 65, 70, 75, 80, 85],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
    })
    cohorts = ["gender"]
    result = cohortCompare(df, cohorts)
    result_set = {}
    for cohort_name, metrics in result.items():
        result_set[cohort_name] = metrics
    #for cohort_name, metrics in result.items():
    #    print(cohort_name + ": " + str(metrics) + "\n")
    #assert isinstance(result, pd.DataFrame)
    #assert result.shape[0] == len(cohorts)
    test_1 = result_set["gender_F"].getStats()

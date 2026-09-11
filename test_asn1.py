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
        'score': [10, 12, 14, 16, 18, 20, 17, 19, 21, 23, 11, 21],
        'group': ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A']
    })
    eff_size = -.93
    d = effectSizer(df, 'score', 'group')
    abs_eff_size = abs(eff_size)
    abs_d = abs(d)
    assert (np.isclose(abs_d, abs_eff_size, atol=0.3) & (isinstance(d, float)))

def test_effectSizer_2():
    df = pd.DataFrame({
        'value': [5, 7, 9, 10, 11, 9, 10, 11, 12, 13, 12, 11],
        'category': ['X', 'X', 'X', 'X','Y', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y']
    })
    eff_size = -.64
    d = effectSizer(df, 'value', 'category')
    abs_eff_size = abs(eff_size)
    abs_d = abs(d)
    assert (np.isclose(abs_d, abs_eff_size, atol=0.3) & (isinstance(d, float)))

def test_cohortCompare_1():
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45, 50],
        'height': [160, 165, 170, 175, 180, 185],
        'hair': ['brown', 'blonde', 'blonde', 'red', 'brown', 'blonde']
    })
    blonde_height = 173.3
    blonde_age = 38.3
    cohorts = ["hair"]
    result = cohortCompare(df, cohorts)
    result_set = {}
    for cohort_name, metrics in result.items():
        result_set[cohort_name] = metrics
    #assert isinstance(result, pd.DataFrame)
    #assert result.shape[0] == len(cohorts)
    test_1 = result_set["hair_blonde"].getStats()
    test_1_mean = test_1["mean"]
    t1_age = test_1_mean["age"]
    t1_height = test_1_mean["height"]
    #assert isinstance(test_1_mean, pd.Series)
    #assert (t1_age == blonde_age) & (t1_height == blonde_height)
    assert np.isclose(t1_age, blonde_age, .3) & np.isclose(t1_height, blonde_height, .3)


def test_cohortCompare_2():
    df = pd.DataFrame({
        'age': [18, 22, 27, 29, 31, 35, 40, 45, 38, 42],
        'weight': [50, 55, 60, 65, 70, 75, 80, 85, 61, 74],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'F']
    })
    f_weight_std = 10.8
    f_age_std = 8.5
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
    test_1_std = test_1["std"]
    t1_age_std = test_1_std["age"]
    t1_weight_std = test_1_std["weight"]
    assert np.isclose(t1_age_std, f_age_std, .3) & np.isclose(t1_weight_std, f_weight_std, .3)
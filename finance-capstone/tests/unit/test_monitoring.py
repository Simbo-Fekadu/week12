import pandas as pd
from finance_capstone.models.monitoring import population_stability_index

def test_population_stability_index_shift():
    baseline = pd.Series([1,2,3,4,5,6,7,8,9,10])
    shifted = pd.Series([5,6,7,8,9,10,11,12,13,14])
    psi = population_stability_index(baseline, shifted, bins=5)
    assert psi > 0  # shift should produce positive PSI

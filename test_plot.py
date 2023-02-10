"""unit tests for plot submodule"""

import pytest
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from testdata import dates10, dates11, waterLevel10, baddates10, badWaterLevel10, place1

def test_plot_water_levels():
    plot_water_levels(place1, dates10, waterLevel10, show=False)

    with pytest.raises(TypeError):
        plot_water_levels("a", "", "", show = False)
    with pytest.raises(ValueError):
        plot_water_levels(place1, dates11, waterLevel10, show = False)
    with pytest.raises(TypeError):
        plot_water_levels(place1, baddates10, waterLevel10, show = False)
    with pytest.raises(TypeError):
        plot_water_levels(place1, dates10, badWaterLevel10, show = False)

def test_plot_water_level_with_fit():
    
    plot_water_level_with_fit(place1, dates10, waterLevel10, 5, show=False)

    with pytest.raises(TypeError):
        plot_water_level_with_fit("a", "", "", 5, show = False)
    with pytest.raises(ValueError):
        plot_water_level_with_fit(place1, dates11, waterLevel10, 5, show = False)
    with pytest.raises(TypeError):
        plot_water_level_with_fit(place1, baddates10, waterLevel10, 5, show = False)
    with pytest.raises(TypeError):
        plot_water_level_with_fit(place1, dates10, badWaterLevel10, 5, show = False)
    

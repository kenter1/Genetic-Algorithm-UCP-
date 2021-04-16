#!/usr/bin/env python3
"""
There are 2 data inputs to the GA:
    
1. demand: should be a .txt file with the demand profile. Can be any length.
2. gen_info: a .csv file with the following variables:
    - min_output: minimum generation (MW)
    - max_output: maximum generation (MW)
    - status: generator's initial status (integer-encoded)
    - a, b, c: coefficients for quadratic fuel cost curve of the form 
    cost = a*E^2 + b*E + c, where E is the energy delivered by the generator in 
    the time period (E = power if periods are 1 hour). 
    - t_min_down: minimum number of periods that generator must spend offline 
    before being turned on
    - t_min_up: minimum number of periods that generator must spend online before 
    being turned off.
    - hot_cost: cost for a hot start ($)
    - cold_cost: cost for a cold start ($)
    - cold_hrs: hot start if downtime (in *periods*) <= cold_hrs, otherwise
    a cold start.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from fitness import calculate_constraint_costs
from economic_dispatch import economic_dispatch


# Change demand profile here
demand = np.genfromtxt(r"C:\Users\ranad\Desktop\Courses\CAP5512\Project\Code\ps_model\data.txt")

# Change gen_info here
gen_info = pd.read_csv(r"C:\Users\ranad\Desktop\Courses\CAP5512\Project\Code\ps_model\data.csv")

# Supply the kwargs
all_kwargs = {'demand': demand,
              'gen_info': gen_info,
              'init_status': gen_info['status'],
              'voll': 1e3,
              'constraint_penalty': 1e4,
              'reserve_margin': 0.1,
              'schedule': np.random.choice(2, size = (24, 10))}

# Calculate ED for the best schedule
ed = economic_dispatch(gen_info, all_kwargs["schedule"], demand+0.01)

# Plot schedule data frame 
df = pd.DataFrame(ed[0])
df.plot(kind='bar', stacked=True)
plt.show()



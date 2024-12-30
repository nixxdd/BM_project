# -*- coding: utf-8 -*-
#
# network_params.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""PyNEST Microcircuit: Network Parameters
---------------------------------------------

A dictionary with base network and neuron parameters is enhanced with derived
parameters.

"""

import numpy as np


def get_exc_inh_matrix(val_exc, val_inh, num_pops):
    """Creates a matrix for excitatory and inhibitory values.

    Parameters
    ----------
    val_exc
        Excitatory value.
    val_inh
        Inhibitory value.
    num_pops
        Number of populations.

    Returns
    -------
    matrix
        A matrix of of size (num_pops x num_pops).

    """
    matrix = np.zeros((num_pops, num_pops))
    matrix[:, 0:num_pops:2] = val_exc
    matrix[:, 1:num_pops:2] = val_inh
    return matrix


net_dict = {
    # factor to scale the number of neurons
    "N_scaling": 0.1,
    "K_scaling": 0.1,
    "neuron_model": "iaf_psc_exp",
    # Names of the simulated neuronal populations (ONLY Layer 4)
    "populations": ["L4E", "L4I"],
    # Number of neurons for these populations
    "full_num_neurons": np.array([21915, 5479]),
    # Mean rates (adjust to match the populations included)
    "full_mean_rates": np.array([4.414, 5.876]),
    # Connection probabilities (2x2 matrix for Layer 4 only)
    "conn_probs": np.array(
        [
            [0.0497, 0.135],  # L4E to L4E and L4I
            [0.0794, 0.1597],  # L4I to L4E and L4I
        ]
    ),
    # Mean amplitude of PSPs
    "PSP_exc_mean": 0.15,
    "weight_rel_std": 0.1,
    "g": -4,
    "delay_exc_mean": 1.5,
    "delay_inh_mean": 0.75,
    "delay_rel_std": 0.5,
    "poisson_input": True,
    "K_ext": np.array([2100, 1900]),
    "bg_rate": 8.0,
    "delay_poisson": 1.5,
    "V0_type": "optimized",
    "neuron_params": {
        "V0_mean": {"original": -58.0, "optimized": [-63.33, -63.45]},
        "V0_std": {"original": 10.0, "optimized": [4.74, 4.94]},
        "E_L": -65.0,
        "V_th": -50.0,
        "V_reset": -65.0,
        "C_m": 250.0,
        "tau_m": 10.0,
        "tau_syn": 0.5,
        "t_ref": 2.0,
    },
}


# derive matrix of mean PSPs,
# the mean PSP of the connection from L4E to L23E is doubled
PSP_matrix_mean = get_exc_inh_matrix(
    net_dict["PSP_exc_mean"], net_dict["PSP_exc_mean"] * net_dict["g"], len(net_dict["populations"])
)
PSP_matrix_mean[0, 1] = 2.0 * net_dict["PSP_exc_mean"]

updated_dict = {
    # matrix of mean PSPs
    "PSP_matrix_mean": PSP_matrix_mean,
    # matrix of mean delays
    "delay_matrix_mean": get_exc_inh_matrix(
        net_dict["delay_exc_mean"], net_dict["delay_inh_mean"], len(net_dict["populations"])
    ),
}

net_dict.update(updated_dict)

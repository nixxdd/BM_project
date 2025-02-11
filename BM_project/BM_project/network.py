import nest
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_positions(neurons) -> np.ndarray:
    """
    Get the positions of a list of neurons.
    (Assumes that nest.GetStatus(neurons, 'positions') returns a list of positions.)
    """
    return np.array(nest.GetStatus(neurons, 'positions'))

def get_positions_dict(layer_e, layer_i):
    """
    Returns dictionaries mapping neuron id -> position for excitatory and inhibitory populations.
    """
    positions_exc = {
        neuron: pos for neuron, pos in zip(layer_e, nest.GetStatus(layer_e, 'positions'))
    }
    positions_inh = {
        neuron: pos for neuron, pos in zip(layer_i, nest.GetStatus(layer_i, 'positions'))
    }
    return positions_exc, positions_inh


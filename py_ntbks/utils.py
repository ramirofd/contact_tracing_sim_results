import os

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def load_dataframe(node, broadcast_time, log_position_time, window_time_threshold, sim_time, path, type_, header):
    filename_node = f"{path}/n{node}_{window_time_threshold:.2f}wt-{broadcast_time:.2f}bt-{log_position_time:.2f}lp_{type_}.csv"
    try:
        df = pd.read_csv(filename_node, names=header)
        df['broadcast_time'] = broadcast_time
        df['frequency'] = 1/broadcast_time
        df['log_position_time'] = log_position_time
        df['sim_time'] = sim_time*60
        return df

    except FileNotFoundError:
        print("File Not Found")


def load_results_dataframe(node, broadcast_time, log_position_time, window_time_threshold, sim_time, path):
    header = ["node", "broadcast_time", "seen_id", "told_by", "hop", "start", "end"]
    type_ = 'results'

    df = load_dataframe(node, broadcast_time, log_position_time, window_time_threshold, sim_time, path, type_, header)
    df['window_duration'] = df['end']-df['start']
    return df


def delete_file(node, broadcast_time, log_position_time, window_time_threshold, path, type_):
    filename_node = f"{path}/n{node}_{window_time_threshold:.2f}wt-{broadcast_time:.2f}bt-{log_position_time:.2f}lp_{type_}.csv"
    try:
        os.remove(filename_node)
    except FileNotFoundError as err:
        print(err)


def load_position_dataframe(node, broadcast_time, log_position_time, window_time_threshold, sim_time, path):
    header = [f'node_{node}', f'timestamp', f'x_pos_{node}', f'y_pos_{node}']
    type_ = 'position'
    return load_dataframe(node, broadcast_time, log_position_time, window_time_threshold, sim_time, path, type_, header)

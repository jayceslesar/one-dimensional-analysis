import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from typing import Union


class DataGen:
    """Generate simulated data on one dimension."""
    def __init__(self, num_points: int = 1000, seed: Union[int, None] = None):
        if seed is not None:
            np.random.seed(seed)

        self.num_points = num_points

    def generate(self):
        """Generate some time series data for use."""
        out = np.zeros(self.num_points)

        self.num_sections = np.random.randint(3, 8)

        done = False
        points_left_to_generate = self.num_points
        index = 0
        while not done:
            for i, section in enumerate(range(self.num_sections)):
                if i == self.num_sections - 1:
                    points_in_this_section = points_left_to_generate
                else:
                    points_in_this_section = np.random.randint(1, points_left_to_generate)

                points_left_to_generate -= points_in_this_section

                section_change_per_point = np.random.randint(0, 100)

                for point in range(points_in_this_section):
                    posneg = np.random.randint(2)
                    # posneg = 1

                    if posneg == 0:
                        generated_point = out[index - 1] - section_change_per_point
                    if posneg == 1:
                        generated_point = out[index - 1] + section_change_per_point

                    print(posneg, generated_point)
                    out[index] = generated_point
                    index += 1

            if points_left_to_generate == 0:
                done = True

        self.data = out

    def plot(self):
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=np.arange(len(self.data)), y=self.data, mode='lines'))
        fig.update_xaxes(title='Timestamp (index)')
        fig.update_yaxes(title='Value')
        fig.update_layout(title=f'Data of size {self.num_points} and {self.num_sections} sections.')
        fig.show()

    def analyze(self):
        diffs = np.abs(np.diff(self.data))
        number_of_rates = set(diffs)
        print(number_of_rates)
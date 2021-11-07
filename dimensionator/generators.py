import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from typing import Union
import os
import webbrowser


def figures_to_html(figs, filename="dashboard.html"):
    dashboard = open(filename, 'w')
    dashboard.write("<html><head></head><body>" + "\n")
    for fig in figs:
        inner_html = fig.to_html().split('<body>')[1].split('</body>')[0]
        dashboard.write(inner_html)
    dashboard.write("</body></html>" + "\n")


class DataGen:
    """Generate simulated data on one dimension."""
    def __init__(self, num_points: int = 1000, seed: Union[int, None] = None):
        if seed is not None:
            np.random.seed(seed)

        self.num_points = num_points
        self.plot = None
        self.rate_plot = None

    def generate(self):
        """Generate some time series data for use."""
        out = np.zeros(self.num_points)

        self.num_sections = np.random.randint(3, 10)

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

                    out[index] = generated_point
                    index += 1

            if points_left_to_generate == 0:
                done = True

        self.data = out

    def normal_plot(self):
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=np.arange(len(self.data)), y=self.data, mode='lines'))
        fig.update_xaxes(title='Timestamp (index)')
        fig.update_yaxes(title='Value')
        fig.update_layout(title=f'Data of size {self.num_points:,} and {self.num_sections} sections.')

        self.plot = fig

    def find_rates_by_diff(self):
        data_index_by_rate = {}
        diffs = np.abs(np.diff(self.data))
        rates = list(set(diffs))

        for rate in rates:
            indexes_at_rate = np.where(np.abs(np.diff(self.data)) == rate)[0]
            data_index_by_rate[rate] = (indexes_at_rate[0], indexes_at_rate[-1])

        bounds = [data_index_by_rate[bound] for bound in data_index_by_rate.keys()]
        sorted_bounds = sorted(bounds, key=lambda x: x[0])

        inv_data_index_by_rate = {v: k for k, v in data_index_by_rate.items()}
        sorted_rates = []
        for bound in sorted_bounds:
            sorted_rates.append(inv_data_index_by_rate[bound])

        fig = go.Figure()
        for i, bound in enumerate(sorted_bounds):
            start = bound[0]
            end = bound[1]
            x = np.arange(start, end)
            y = self.data[start:end]

            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'Average Change of {sorted_rates[i]}'))

        fig.update_xaxes(title='Timestamp (index)')
        fig.update_yaxes(title='Value')
        fig.update_layout(title=f'Data of size {self.num_points:,} and {self.num_sections} sections.')

        self.rate_plot = fig

    def explore(self):
        if self.plot is None:
            self.normal_plot()
        if self.rate_plot is None:
            self.find_rates_by_diff()

        to_plot = [self.plot, self.rate_plot]
        path = os.path.join('explorable.html')
        figures_to_html(to_plot, path)
        webbrowser.open_new_tab(f'file://{os.path.join(os.getcwd(), path)}')

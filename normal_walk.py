import random
import plotly.graph_objs as go
import plotly.express as px
import numpy as np


def gen_normal_walk(num_steps, step_size):
    out = [0]
    for _ in range(num_steps):
        positive = random.random()
        if positive > 0.5:
            step_size = -1 * step_size

        out.append(out[-1] + step_size)

    return out


num_steps = 5000
step_size = 1
plot = gen_normal_walk(num_steps, step_size)

fig = go.Figure()

fig.add_trace(go.Scatter(x=np.arange(len(plot)), y=plot, mode='lines'))
fig.update_xaxes(title='Timestamp (index)')
fig.update_yaxes(title='Value')
fig.update_layout(font_size=20)
fig.update_layout(title=f'Random Walk {num_steps:,} Steps and Step Size of {step_size}.')
fig.show()
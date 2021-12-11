from numpy import number
from networks import erdos_renyi, rw, draw, sub_graph, comparison_graph, run_multiple_runners, plt, random, watts_strogatz
from dimensionator.generators import DataGen, DDDRandomWalk, figures_to_html
import plotly.express as px


def main():
    # my_data = DataGen(num_points=500_000)

    # my_data.generate()

    # my_data.explore()
    dims = [49, 499, 999, 1499]
    dims = [1499]
    times = 100
    for dim in dims:
        print(dim)
        shape = dim
        curr = []
        my_cube = DDDRandomWalk(shape, shape, shape)
        my_cube.walk()
    #     # for step in range(times):
    #     #     print(step)
        #     curr.append(my_cube.walk(unique_path=True))
    #     # fig = px.histogram(x=curr)
    #     # fig.update_layout(font_size=20)
    #     # fig.show()



def networks():
    G = erdos_renyi(50, 0.2, directed=True)
    # G = watts_strogatz(50, 30, 0.5)
    #draw(G)
   # plt.show()
    # running single walker

    # length_of_walk = 100
    # # random walk will start at 0
    # start = random.randrange(0, G.number_of_nodes())
    # visited = rw(G, length_of_walk, start)
    # draw(G)
    # plt.show()

    # H = sub_graph(G, visited)
    # draw(H)
    # plt.show()
    # comparison_graph(G, H, 1)
    
    # running more than one walker
    number_of_runners = 3
    visited = run_multiple_runners(G, number_of_runners, walk_length=50)
    H = sub_graph(G, visited)
    draw(G) 
    plt.show()
    draw(H)
    plt.show()

    comparison_graph(G, H, number_of_runners)

if __name__ == '__main__':
    main()
    # networks()
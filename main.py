from numpy import number
from dimensionator.generators import DataGen, DDDRandomWalk
from networks import erdos_renyi, rw, draw, sub_graph, comparison_graph, run_multiple_runners, plt, random

def main():
    # my_data = DataGen(num_points=500_000)

    # my_data.generate()

    # my_data.explore()
    dims = [9, 49, 99, 499]
    for dim in dims:
        shape = dim
        my_cube = DDDRandomWalk(shape, shape, shape)
        my_cube.walk(unique_path=False)

def networks():
    G = erdos_renyi(50, 0.2, directed=True)
    
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
    # comparison_graph(G, H)
    
    #running more than one walker
    number_of_runners = 5
    visited = run_multiple_runners(G, number_of_runners, walk_length=50)
    H = sub_graph(G, visited)
    draw(G) 
    plt.show()
    draw(H)
    plt.show()

    comparison_graph(G, H, number_of_runners)

if __name__ == '__main__':
    #main()
    networks()
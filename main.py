from dimensionator.generators import DataGen, DDDRandomWalk
from networks import erdos_renyi, rw, draw, sub_graph, comparison_graph, plt

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
    visited = rw(G, 1000, 0)
    draw(G)
    plt.show()

    H = sub_graph(G, visited)
    draw(H)
    plt.show()

    comparison_graph(G, H)

if __name__ == '__main__':
    #main()
    networks()
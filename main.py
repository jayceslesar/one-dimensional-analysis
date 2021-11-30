from dimensionator.generators import DataGen, DDDRandomWalk
from networks import *

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
    F = erdos_renyi(50, 0.6, directed=True)
    visited = rw(F, 25, 0)
    draw(F)
    plt.show()

    H = sub_graph(F, visited)
    draw(H)
    plt.show()

    metrics(F)
    metrics(H)

if __name__ == '__main__':
    main()
    #networks()
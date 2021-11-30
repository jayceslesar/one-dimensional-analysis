from dimensionator.generators import DataGen, DDDRandomWalk


def main():
    # my_data = DataGen(num_points=500_000)

    # my_data.generate()

    # my_data.explore()
    dims = [9, 49, 99, 499]
    for dim in dims:
        shape = dim
        my_cube = DDDRandomWalk(shape, shape, shape)
        my_cube.walk(unique_path=False)


if __name__ == '__main__':
    main()
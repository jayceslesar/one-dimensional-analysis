from dimensionator.generators import DataGen, DDDRandomWalk


def main():
    # my_data = DataGen(num_points=500_000)

    # my_data.generate()

    # my_data.explore()

    my_cube = DDDRandomWalk(5, 5, 5)
    my_cube.walk(unique_path=True)
    my_cube.walk(num_steps = 100, unique_path=True)


if __name__ == '__main__':
    main()
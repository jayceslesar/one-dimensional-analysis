from dimensionator.generators import DataGen


def main():
    my_data = DataGen(num_points=500_000)

    my_data.generate()

    my_data.explore()


if __name__ == '__main__':
    main()
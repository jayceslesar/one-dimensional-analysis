from dimensionator.generators import DataGen


def main():
    my_data = DataGen(num_points=2000)

    my_data.generate()

    print(len(my_data.data))

    my_data.plot()

    my_data.analyze()


if __name__ == '__main__':
    main()
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values,
               rw.y_values,
               c=point_numbers,
               cmap=plt.cm.Blues,
               edgecolors='none',
               s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1],
               rw.y_values[-1],
               c='red',
               edgecolors='none',
               s=100)

    # plt.show()
    plt.savefig('随机漫游图.png', bbox_inches='tight')

    keep_running = input('Make another walk?(y/n):')

    if keep_running == 'n':
        break
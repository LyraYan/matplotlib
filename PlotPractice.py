import matplotlib.pyplot as plt
import numpy as np


def Figure_base() -> None:
    """
    brief: plot a base figure

        annotation:
            x_points = np.array([1,3,5,7,9])
                            x:   | | | | |
                                 | | | | |
                            y:   V V V V V
            y_points = np.array([2,5,6,8,10])
            coordinate:(1,2)、(3,5)、(5,6)、···、(9,10)

    :param: None
    :return: None
    """
    x_points = np.array([1, 3, 5, 7, 9])
    y_points = np.array([2, 6, 6, 8, 10])
    plt.title('Figure_base')
    plt.plot(x_points, y_points, 'r--o')  # 一条杠是实线，两条是虚线
    plt.show()


def Figure_subplots() -> None:
    """
    brief: plot several subplots in a figure

    :param: None
    :return: None
    """
    x_points_1 = x_points_2 = np.random.randint(0, 10, [1, 10])
    y_points_1 = y_points_2 = np.random.randint(0, 10, [1, 10])
    # x_points_2 = np.random.randint(0, 10, [1, 10])
    # y_points_2 = np.random.randint(0, 10, [1, 10])

    plt.subplot(1, 2, 1)
    """
            plt.subplot(rows, cols, index):
            rows:行数            例: plt.subplot(2,2,3) --> 0   1 
            cols:列数                分成2×2区域，绘制3号位    2   3*
            index:子图位置
    """
    plt.plot(x_points_1, y_points_1, 'r--o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('subplot_1')

    plt.subplot(1, 2, 2)
    plt.plot(x_points_2, y_points_2, 'b--o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('subplot_2')

    plt.show()


def Figure_subplots_axes():
    """
    brief: configure some axes in a figure,picture same as Figure_subplots()

    :param: str
    :return: None
    """

    x_points_1 = x_points_2 = np.random.randint(0, 10, [1, 10])
    y_points_1 = y_points_2 = np.random.randint(0, 10, [1, 10])

    '''setting font to show Chinese normally'''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    fig = plt.figure(figsize=(5, 5), facecolor='w', dpi=200)

    '''can divide a figure to different shape   note:illustration'''
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(5, 1, 3)
    ax3 = fig.add_subplot(5, 1, 5)

    # ax[0].plot(x_points_1, y_points_1, color='b', marker='.', label='sin(x)')
    # ax[1].plot(x_points_2, y_points_2, color='orange', marker='')

    # plt.plot(x_points_1, y_points_1, color='lime', marker='+')

    plt.show()


def function(type: str) -> list:
    """
    brief: generate arrays to plot

        Parameters
        ----------
        type : type that will be plotted,such as: sin、cos、tan、···

        Returns
        -------
        array : an array contains x and y

    :return: an array contains x and y
    """

    if type == 'sin' or 'cos' or 'tan' or 'arcsin' or 'arccos' or 'arctan' or 'sec' or 'csc' or 'cot':
        '''triangle function'''
        x_tri_range = np.arange(-2 * np.pi, 2 * np.pi, 0.1, dtype='float64')
        y_tri_range = []

        if type == 'sin':
            y_tri_range = np.sin(x_tri_range)
        if type == 'cos':
            y_tri_range = np.cos(x_tri_range)
        if type == 'tan':
            y_tri_range = np.tan(x_tri_range)
        if type == 'arcsin':
            y_tri_range = np.arcsin(x_tri_range)
        if type == 'arccos':
            y_tri_range = np.arccos(x_tri_range)
        if type == 'arctan':
            y_tri_range = np.arctan(x_tri_range)
        if type == 'sec':
            y_range = np.sin(x_tri_range)
            y_tri_range = []
            for var in y_range:
                y_tri_range.append(1 / var)
        if type == 'csc':
            y_range = np.cos(x_tri_range)
            y_tri_range = []
            for var in y_range:
                y_tri_range.append(1 / var)
        if type == 'cot':
            y_range1 = np.sin(x_tri_range)
            y_range2 = np.cos(x_tri_range)
            y_tri_range = []
            for i in range(len(y_range1)):
                y_tri_range.append(y_range2[i] / y_range1[i])
                print(i)

    '''linear function'''
    x_linear_range = np.array(range(-20, 20), dtype='float64')

    arr = [x_tri_range, y_tri_range]

    print(y_tri_range)

    return arr


def Plot_tri_function() -> None:
    type = input("输入要画的三角函数类型：sin cos ...etc")
    arr = function(type)

    plt.figure(figsize=(6, 6))
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title('三角函数')
    '''plt.text(x, y, 'text', alpha[diaphaneity], rotation, color, size)'''
    plt.text(0.5, 0.5, 'Tri', alpha=0.9, rotation=0, color='y', size=30)

    plt.plot(arr[0], arr[1], label=type)
    '''
        plt.legend(handle[object of figure/axe], label, loc[location])
        location: ['upper left' , 'upper center', 'upper right',
                   'center left', 'center', 'center right',
                   'lower left', 'lower center', 'lower right']
    '''
    plt.legend(loc='center')

    plt.show()


# Figure_base()
# Figure_subplots()
# Figure_subplots_axes()

Plot_tri_function()

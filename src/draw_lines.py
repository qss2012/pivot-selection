import matplotlib.pyplot as plt

def collector(method,lookfor_pair):
    new_list = []
    input_file = open("../work/sim/Sim.%s.csv"%method,'r')
    next(input_file)
    for line in input_file:
        p = line.strip('\n').split(', ')
        src = p[0][0].capitalize()
        tgt = p[1][0].capitalize()
        pair = "%s-%s"%(src,tgt)
        if lookfor_pair == pair:    
            jaccard = float(p[3])
            n_pivots = int(float(p[5]))
            new_list.append((jaccard,n_pivots))   
    # print new_list
    return new_list
    pass


def drawer(draw_lists,lookfor_pair,methods):
    plt.figure(figsize=(8,6))
    x = [tmp[1] for tmp in draw_lists[0]]
    ys = []
    for draw_list in draw_lists:
        ys.append([tmp[0] for tmp in draw_list])
    opacity = 0.4
    i = 0
    for y in ys:
        plt.plot(x,y, marker="o",alpha=opacity, label=convert(methods[i]))
        i +=1

    plt.title(lookfor_pair)
    plt.xlabel('#pivots')
    plt.ylabel('Jaccard$_{L,U}$')
    plt.legend()

    plt.show()
    pass


def constructer(methods,lookfor_pair):
    new_list = []
    for method in methods:
        new_list.append(collector(method,lookfor_pair))
    return new_list
    pass

def convert(method):
    return method.upper()

# x = [1, 2.0, 3.0, 4.0, 5.0, 6.0]
# y = [3.14159, 503, 28.27431, 50.26544, 78.53975, 113.09724]
# y2 = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
# plt.plot(x, y, label='y')
# plt.plot(x, y2, marker='o', linestyle='--', color='r', label='y2')
# plt.xlabel('#pivots')
# plt.ylabel('JC')
# plt.title('$E \\rightarrow K$')
# plt.legend()
# plt.show()


if __name__ == "__main__":
    methods = ["mi","pmi"]
    lookfor_pair = "K-E"
    drawer(constructer(methods,lookfor_pair),lookfor_pair,methods)
from collections import defaultdict


example = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def p1():
    network = defaultdict(list)
    for line in open("input/23.txt").read().strip().split("\n"):
        p1 = line.split("-")[0]
        p2 = line.split("-")[1]

        network[p1].append(p2)
        network[p2].append(p1)

    groups = set()
    for k, con in network.items():
        for i in range(len(con) - 1):
            for j in range(i + 1, len(con)):
                group = tuple(sorted((k, con[i], con[j])))
                contains_t = False
                for g in group:
                    if g[0] == "t":
                        contains_t = True
                        break
                if con[i] in network[con[j]] and contains_t:
                    groups.add(group)
    print("p1:", len(groups))


def p2():
    network = defaultdict(list)
    for line in open("input/23.txt").read().strip().split("\n"):
        p1 = line.split("-")[0]
        p2 = line.split("-")[1]

        network[p1].append(p2)
        network[p2].append(p1)

    largest_lan = []
    for key, con in network.items():
        for i in range(len(con) - 1):
            lan = []
            lan.append(key)
            lan.append(con[i])
            for j in range(i + 1, len(con)):
                included = True
                for k in lan:
                    if con[j] not in network[k]:
                        included = False
                        break
                if included:
                    lan.append(con[j])
            if len(lan) > len(largest_lan):
                largest_lan = lan
    print("p2:", ",".join(sorted(largest_lan)))


p1()
p2()

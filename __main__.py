import assignment
import demand
import __init__
import network
if __name__ == "__main__":
    od = demand.ODMatrix()
    od.make_example(__init__.eg1['lis'])
    ne = network.Network()
    ne.make_example(__init__.eg1)
    co = demand.Connector(ne.nodes())
    bundle = assignment.all_or_nothing_assignment(ne,od,co)
    x = input('请输入起始地点：')
    y = input('请输入目的地：')
    for i in bundle.flows:
        a,b = i
        if a[0] == x and a[-1] == y:
            m = ''
            for n in a:
                m = m + ',' + n
                m = m.strip(',')
            print("最短路径：",m)
            print("总流量：",b)
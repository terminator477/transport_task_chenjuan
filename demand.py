import __init__
class ODMatrix:#用邻接矩阵存储结点间的流量信息
    def __init__(self, n=4, default_flow=0.0):
        self.od_flows = []
        for i in range(n):
            self.od_flows.append([default_flow]*n)

    def flow(self, index):#查找flow
        row, col = index
        return self.od_flows[row][col]

    def make_example(self,lis):
        self.od_flows = lis    

class Connector:
    def __init__(self, nodeids):
        self.nodeids = list(nodeids)

    def get_ods_and_indices(self):
        result = []
        for row, fromnode in enumerate(self.nodeids):
            for col, tonode in enumerate(self.nodeids):
                index = (row, col)
                od = (fromnode, tonode)
                result.append((index, od))

        return result



 
 
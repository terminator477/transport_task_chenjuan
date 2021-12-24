from heapq import heappush, heappop
import __init__

class Network:
    def __init__(self):
        self._neighbours = {}
        self._attributes = {}

    def make_example(self,eg1):
        self._neighbours = eg1["neighbours"]
        self._attributes = {"cost" : eg1["attributes"]["cost"],
                         "distance": eg1["attributes"]["distance"]}   

    # 1. 增删查改
    def add_node(self, nodeid):
        assert nodeid not in self._neighbours

        self._neighbours[nodeid] = []

    def remove_node(self, nodeid):#删除作为起始结点和终止结点的nodeid
        assert nodeid in self._neighbours
        del self._neighbours[nodeid]
        for key in self._neighbours.keys():
            for value in self._neighbours[key]:
                if value==nodeid:
                    self._neighbours[key].remove(value)

    def add_link(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid not in self._neighbours[from_nodeid]

        self._neighbours[from_nodeid].append(to_nodeid)

    def remove_link(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        assert to_nodeid in self._neighbours[from_nodeid]
        
        self._neighbours[from_nodeid].remove(to_nodeid)
        for attribute in self._attributes.values():
            del attribute[(from_nodeid, to_nodeid)]

    # 2. 查询
    def next_nodes(self, nodeid):
        return self._neighbours[nodeid]

    def prev_nodes(self, nodeid):
        prev_nodes=[]
        for key in self._neighbours.keys():
            for value in self._neighbours[key]:
                if value==nodeid:
                    prev_nodes.append(key)
        return prev_nodes            

    def is_connected(self, from_nodeid, to_nodeid):
        assert from_nodeid in self._neighbours
        assert to_nodeid in self._neighbours
        for value in self._neighbours[from_nodeid]:
            if value==to_nodeid:
                return True
        return False

    def nodes(self):
        nodes=[]
        for key in self._neighbours.keys():
            nodes.append(key)
        return nodes    

    def links(self):
        links = []

        for cur_node, next_nodes in self._neighbours.items():
            for next_node in next_nodes:
                links.append((cur_node, next_node))

        return links

    # 3. 属性
    def attributes(self, from_nodeid, to_nodeid):
        assert self.is_connected(from_nodeid,to_nodeid)
        return {'cost':self._attributes['cost'][(from_nodeid,to_nodeid)], 'distance':self._attributes['distance'][(from_nodeid,to_nodeid)]}   

    def cost(self, from_nodeid, to_nodeid):
        self.attributes(from_nodeid, to_nodeid)["distance"]

    def shortest_route(self, od):
        origin, destination = od
        costs, routes = self.shortest_routes_from(origin)

        for route in routes:
            if routes[-1] == destination:
                return route
                
    # 4. 最短路径搜索
    def shortest_routes_from(self, nodeid):
        known = []
        unknow = []
        boundary = []
        prevs = {}#找node的前一个结点
        costs = {}#nodeid到node的最短距离

        # 初始化
        for node in self.nodes():
            unknow.append(node)
            prevs[node] = None
            costs[node] = 10000000

        heappush(boundary, (0, nodeid))

        # 搜索循环
        while(boundary):
            cost, current_node = heappop(boundary)
            if current_node in known:
                continue
            known.append(current_node)
            costs[current_node] = cost

            for next_node in  self.next_nodes(current_node):
                new_cost = cost + self.cost(current_node, next_node)
                if new_cost<costs[next_node]:
                    prevs[next_node] = current_node
                    costs[next_node] = cost

                    heappush(boundary, (new_cost, next_node))

        # 重构路径
        routes = {}
        for node in self.nodes():
            routes[node] = None

        routes[nodeid] = [nodeid]

        while None in routes.values():
            for end_node, route in routes.items():
                if route is not None:
                    continue
                prev = prevs[end_node]
                if routes[prev] is not None:
                    routes[end_node] = routes[prev].extend([end_node])


        return costs, routes


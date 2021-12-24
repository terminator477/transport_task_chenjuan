import __init__ 
from network import Network

ne = Network()
ne.make_example(__init__.eg1)
print({'distance':ne._attributes['distance'][("C","A")]})
print(ne.attributes("C","A"))
x = 'E'
print(type(x))
#print(ne.shortest_routes_from(x))
print(ne.shortest_route(('A','E')))
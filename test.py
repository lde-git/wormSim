import json
import tensorflow as tf
import networkx as nx
import matplotlib.pyplot as plt



def readWeights(path):
    with open (path) as f:
        connectome = json.load(f)
    return connectome

json_weights = readWeights('weights.json')

#visualizing the network as directed graph
G = nx.DiGraph()

# add nodes amd edges based on the weights
count = 1
for neuron, connections in json_weights.items():
    print(count)
    count += 1 
    G.add_node(neuron) #add neuron as node
    for traget_neuron, weight in connections.items():
        G.add_edge(neuron, traget_neuron, weight=weight)

#visualize
pos = nx.spring_layout(G)
#pos = nx.kamada_kawai_layout(G) 
#pos = nx.spectral_layout(G)




nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=8, arrowsize=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)
plt.show()


#print(json_weights.items())


# model = tf.keras.Sequential()

# for layer_name, layer_weights in tf_weights.items():
#     model.add(tf.keras.layers.Dense (
#         units=layer_weights['weights'].shape[0], #number of output neurons
#         input_shape=(layer_weights['weights'].shape[1],) if layer_name == list(tf_weights.keys())[0] else None, #Input shape for first layer only 
#         activation = 'relu' #activation function 
#     ))
#     model.layers[-1].set_weights([layer_weights['weights'], layer_weights['biases']])

# model.compile(optimizer='adam', loss='mse')

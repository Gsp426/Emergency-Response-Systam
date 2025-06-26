class Dispatcher:
    def __init__(self, graph):
        self.graph = graph

    def dispatch(self, ambulance, patient_loc):
        path = self.graph.dijkstra(ambulance.location, patient_loc)
        if path:
            ambulance.move_to(patient_loc)
        return path

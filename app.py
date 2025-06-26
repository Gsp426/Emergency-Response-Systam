from flask import Flask, render_template, request
from graph import Graph
from ambulance import Ambulance
from dispatcher import Dispatcher

app = Flask(__name__)
graph = Graph()
ambulance = None
dispatcher = None
edges = []  # Store user-entered edges


@app.route("/", methods=["GET", "POST"])
def index():
    global ambulance, dispatcher

    message = ""
    path = []
    amb_loc = None
    pat_loc = None

    if request.method == "POST":
        form_type = request.form.get("form_type")

        if form_type == "add_edge":
            try:
                u = int(request.form["u"])
                v = int(request.form["v"])
                wt = int(request.form["wt"])
                graph.add_edge(u, v, wt)
                edges.append((u, v, wt))
                message = f"✅ Edge added: {u} ↔ {v} (weight {wt})"
            except:
                message = "❌ Invalid edge input."

        elif form_type == "dispatch":
            try:
                amb_loc = int(request.form["ambulance"])
                pat_loc = int(request.form["patient"])
                ambulance = Ambulance(amb_loc)
                dispatcher = Dispatcher(graph)
                path = dispatcher.dispatch(ambulance, pat_loc)
                if not path:
                    message = "❌ No path found."
            except:
                message = "❌ Invalid locations."

    return render_template("index.html", message=message, path=path, edges=edges,
                           amb_loc=amb_loc, pat_loc=pat_loc)



if __name__ == "__main__":
    app.run(debug=True)

from graphviz import Digraph


class Visualizer:

    @staticmethod
    def generate_graph(chain):
        dot = Digraph()
        for i in range(len(chain)):
            dot.node(chain[i])
            if i > 0:
                dot.edge(chain[i - 1], chain[i])

        dot.render("output/attack_chain", format="png", cleanup=True)

    @staticmethod
    def generate_report(chain, kill_map, remediation):
        with open("output/report.md", "w") as f:
            f.write("# Attack Chain Report\n\n")

            f.write("## Attack Chain Path\n")
            f.write(" → ".join(chain) + "\n\n")

            f.write("## Kill Chain Mapping\n")
            for entry in kill_map:
                f.write(f"- {entry['vulnerability']} → {entry['kill_chain_stage']}\n")

            f.write("\n## Remediation Steps\n")
            for fix in remediation:
                f.write(f"- {fix['vulnerability']}: {fix['fix']}\n")

import networkx as nx


CHAIN_RULES = {
    "XSS": ["Session Hijack"],
    "Session Hijack": ["Broken Authentication"],
    "Broken Authentication": ["Privilege Escalation"],
    "Privilege Escalation": ["Data Exfiltration"],
    "SQL Injection": ["Data Exfiltration"],
}


class AttackChainEngine:
    def __init__(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
        self.graph = nx.DiGraph()

    def build_attack_chain(self):
        types = [v["type"] for v in self.vulnerabilities]

        for vuln_type in types:
            self.graph.add_node(vuln_type)

        for vuln_type in types:
            if vuln_type in CHAIN_RULES:
                for next_stage in CHAIN_RULES[vuln_type]:
                    if next_stage in types:
                        self.graph.add_edge(vuln_type, next_stage)

        # Find longest path
        longest_chain = []
        for node in self.graph.nodes:
            for target in self.graph.nodes:
                if node != target:
                    try:
                        path = nx.shortest_path(self.graph, node, target)
                        if len(path) > len(longest_chain):
                            longest_chain = path
                    except:
                        continue

        return longest_chain if longest_chain else types

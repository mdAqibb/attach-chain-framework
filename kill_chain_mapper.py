class KillChainMapper:

    KILL_CHAIN_STAGES = {
        "XSS": "Initial Access",
        "SQL Injection": "Initial Access",
        "Session Hijack": "Credential Access",
        "Broken Authentication": "Persistence",
        "Privilege Escalation": "Privilege Escalation",
        "Data Exfiltration": "Impact"
    }

    @staticmethod
    def map_chain(chain):
        mapped = []
        for stage in chain:
            mapped.append({
                "vulnerability": stage,
                "kill_chain_stage": KillChainMapper.KILL_CHAIN_STAGES.get(stage, "Unknown")
            })
        return mapped

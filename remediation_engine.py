class RemediationEngine:

    FIXES = {
        "XSS": "Implement input validation and output encoding.",
        "SQL Injection": "Use parameterized queries and ORM frameworks.",
        "Session Hijack": "Enable HttpOnly & Secure flags for cookies.",
        "Broken Authentication": "Implement MFA and proper session invalidation.",
        "Privilege Escalation": "Apply least privilege principle.",
        "Data Exfiltration": "Monitor logs and implement DLP controls."
    }

    @staticmethod
    def generate_remediation(chain):
        remediation_steps = []
        for vuln in chain:
            remediation_steps.append({
                "vulnerability": vuln,
                "fix": RemediationEngine.FIXES.get(vuln, "No fix defined.")
            })
        return remediation_steps

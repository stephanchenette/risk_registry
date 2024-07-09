"""
Summary:
Risk Class Definition: Defines a Risk class to structure risk data.

Initial Risk Registry: Creates an initial list of risks and converts it into a Pandas DataFrame.
Bayesian Inference Function: Defines an update_likelihood function to update risk likelihoods using Bayesian Inference.
New Evidence Data: Provides new evidence data for updating the likelihoods of each risk.
Update Likelihoods: Updates the likelihoods of risks based on the new evidence.
Add New Risk Function: Defines an add_risk function to add new risks to the registry and update the DataFrame.
Example Usage: Updates the registry with new evidence and prints the updated registry, then adds a new risk and prints the registry with the new risk added.
"""

import pandas as pd

# Define the structure of the risk registry
class Risk:
    def __init__(self, risk_id, description, threat_source, potential_impact, prior_likelihood, risk_owner, current_controls):
        self.risk_id = risk_id
        self.description = description
        self.threat_source = threat_source
        self.potential_impact = potential_impact
        self.prior_likelihood = prior_likelihood
        self.updated_likelihood = prior_likelihood
        self.risk_owner = risk_owner
        self.current_controls = current_controls

# Create a list to hold the risks
risk_registry = []

# Add initial risks
risk_registry.append(Risk(1, "Phishing Attack", "External", "High", 0.3, "IT Security", ["Email Filtering", "Training"]))
risk_registry.append(Risk(2, "Data Breach", "External/Internal", "Critical", 0.4, "IT Security", ["Access Controls", "Encryption"]))
risk_registry.append(Risk(3, "Ransomware", "External", "Critical", 0.2, "IT Security", ["Anti-Malware", "Backups"]))

# Convert to DataFrame for easier manipulation
risk_df = pd.DataFrame([vars(risk) for risk in risk_registry])

# Function for Bayesian Inference
def update_likelihood(prior, likelihood_given_evidence, evidence_probability):
    """
    Update the likelihood using Bayesian Inference.
    P(A|B) = (P(B|A) * P(A)) / P(B)
    """
    return (likelihood_given_evidence * prior) / evidence_probability

# Example evidence data
# This should come from actual evidence or data in a real-world scenario
new_evidence = {
    1: {"likelihood_given_evidence": 0.7, "evidence_probability": 0.5},  # Phishing Attack
    2: {"likelihood_given_evidence": 0.6, "evidence_probability": 0.4},  # Data Breach
    3: {"likelihood_given_evidence": 0.8, "evidence_probability": 0.3}   # Ransomware
}

# Update likelihoods based on new evidence
for risk_id, evidence in new_evidence.items():
    risk_index = risk_df[risk_df['risk_id'] == risk_id].index[0]
    prior = risk_df.at[risk_index, 'prior_likelihood']
    likelihood_given_evidence = evidence['likelihood_given_evidence']
    evidence_probability = evidence['evidence_probability']
    updated_likelihood = update_likelihood(prior, likelihood_given_evidence, evidence_probability)
    risk_df.at[risk_index, 'updated_likelihood'] = updated_likelihood

print("Updated Risk Registry with Bayesian Inference:")
print(risk_df)

# Function to add a new risk
def add_risk(risk_registry, risk_id, description, threat_source, potential_impact, prior_likelihood, risk_owner, current_controls):
    new_risk = Risk(risk_id, description, threat_source, potential_impact, prior_likelihood, risk_owner, current_controls)
    risk_registry.append(new_risk)
    return pd.DataFrame([vars(risk) for risk in risk_registry])

# Example of adding a new risk
risk_df = add_risk(risk_registry, 4, "Insider Threat", "Internal", "High", 0.15, "HR Security", ["Background Checks", "Monitoring"])
print("Risk Registry after Adding New Risk:")
print(risk_df)

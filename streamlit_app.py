import streamlit as st
import pandas as pd

def multi_criteria_analysis(criteria_weights, alternatives):
    # Normalize criteria weights
    total_weight = sum(criteria_weights.values())
    normalized_weights = {key: value / total_weight for key, value in criteria_weights.items()}

    # Calculate scores for alternatives
    scores = {}
    for alt in alternatives:
        alt_score = sum([normalized_weights[criteria] * alternatives[alt][criteria] for criteria in criteria_weights])
        scores[alt] = alt_score

    return scores

def main():
    st.title("Weighted overlay analysis - CITYAM ")
    
    # Define criteria and alternatives
    criteria = ['Population density', 'Wind speed', 'Noise level']
    alternatives = {
        'Option 1': {'Population density': 5, 'Wind speed': 8, 'Noise level': 7},
        'Option 2': {'Population density': 7, 'Wind speed': 6, 'Noise level': 9},
        'Option 3': {'Population density': 4, 'Wind speed': 9, 'Noise level': 6}
    }
    
    # Collect user input for criteria weights
    st.sidebar.header('Criteria Weights')
    criteria_weights = {}
    for crit in criteria:
        weight = st.sidebar.slider(f"Weight for {crit}", 0, 10, 5)
        criteria_weights[crit] = weight
    
    st.write("Selected Criteria Weights:", criteria_weights)
    
    # Perform multi-criteria analysis
    scores = multi_criteria_analysis(criteria_weights, alternatives)
    
    # Display results
    st.subheader("Scores for Alternatives")
    df = pd.DataFrame.from_dict(scores, orient='index', columns=['Score'])
    st.write(df)

if __name__ == "__main__":
    main()

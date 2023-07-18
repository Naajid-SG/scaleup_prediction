import streamlit as st
import pandas as pd
import joblib

# Load your trained machine learning model
model = joblib.load('modelForPrediction_viz.sav')

# Create a Streamlit web app
st.title('Machine Learning Model')

# Add input widgets for the variables your model needs
mixed = st.checkbox('Mixed:')
b2c = st.checkbox('B2C:')
b2b = st.checkbox('B2B:')
ftenr_total = st.number_input('FTENr_Total:')
founder_age = st.number_input('FounderAge:')
advisor_nr = st.number_input('AdvisorNr:')
globally_leading_product = st.checkbox('GloballyLeadingProduct')
dna_high_ambition_usp = st.checkbox('DNA_HighAmbition_USP')
founders_undergrad = st.checkbox('FoundersUndergrad:')
founders_grad = st.checkbox('FoundersGrad:')
female_founders = st.number_input('FemaleFounders:')
immigrant_founders = st.checkbox('ImmigrantFounders:')
company_move = st.checkbox('CompanyMove')
global_startup_attraction = st.checkbox('GlobalStartupAttraction')
fte_engineer_nr = st.number_input('FTEEngineerNr:')
company_intent_to_move = st.checkbox('CompanyIntentToMove')
entrepreneur_move = st.checkbox('EntrepreneurMove')
global_entrepreneur_attraction_personal = st.checkbox('GlobalEntrepreneurAttractionPersonal')
global_entrepreneur_attraction = st.checkbox('GlobalEntrepreneurAttraction')
stock_policy_all_employees = st.checkbox('StockPolicy_AllEmployees')
startups_with_2_or_3_founders = st.checkbox('StartupsWith2or3Founders')
founder_team_nr = st.number_input('FounderTeamNr:')
founder_team_business = st.number_input('FounderTeamBusiness:')
targeting_global_market_first = st.checkbox('TargetingGlobalMarketFirst')
biz_tech_founder_teams = st.checkbox('BizTechFounderTeams')
founder_team_technical = st.number_input('FounderTeamTechnical:')
# BusinessFounderTeams = st.checkbox('BusinessFounderTeams')
# Founders30 = st.checkbox('Founders30')
# GlobalStartupAttractionEU = st.checkbox('GlobalStartupAttractionEU')
# RespondentImmigrant = st.checkbox('RespondentImmigrant')


 

# Create a button to trigger the model prediction
if st.button('Get Prediction'):
    # Prepare the input data
    data = pd.DataFrame({
        'Mixed': [mixed],
        'B2C': [b2c],
        'B2B': [b2b],
        'FTENr_Total': [ftenr_total],
        'FounderAge': [founder_age],
        'AdvisorNr': [advisor_nr],
        'GloballyLeadingProduct': [globally_leading_product],
        'DNA_HighAmbition_USP': [dna_high_ambition_usp],
        'FoundersUndergrad': [founders_undergrad],
        'FoundersGrad': [founders_grad],
        'FemaleFounders': [female_founders],
        'ImmigrantFounders': [immigrant_founders],
        'CompanyMove': [company_move],
        'GlobalStartupAttraction': [global_startup_attraction],
        'FTEEngineerNr': [fte_engineer_nr],
        'CompanyIntentToMove': [company_intent_to_move],
        'EntrepreneurMove': [entrepreneur_move],
        'GlobalEntrepreneurAttractionPersonal': [global_entrepreneur_attraction_personal],
        'GlobalEntrepreneurAttraction': [global_entrepreneur_attraction],
        'StockPolicy_AllEmployees': [stock_policy_all_employees],
        'StartupsWith2or3Founders': [startups_with_2_or_3_founders],
        'FounderTeamNr': [founder_team_nr],
        'FounderTeamBusiness': [founder_team_business],
        'TargetingGlobalMarketFirst': [targeting_global_market_first],
        'BizTechFounderTeams': [biz_tech_founder_teams],
        'FounderTeamTechnical': [founder_team_technical]
        # 'BusinessFounderTeams': [BusinessFounderTeams],
        # 'Founders30': [Founders30],
        # 'GlobalStartupAttractionEU': [GlobalStartupAttractionEU],
        # 'RespondentImmigrant': [RespondentImmigrant]
    })

    # Make predictions using the model
    prediction = model.predict(data)[0]
    
    # Display the prediction
    st.write('Prediction:', prediction)

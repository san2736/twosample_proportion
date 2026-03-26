import streamlit as st
import numpy as np
from scipy import stats

def san():
    n1 = 400
    n2 = 380
    p1 = 166 / 400
    p2 = 205 / 380
    alpha = 0.01

    phat = (n1*p1 + n2*p2) / (n1 + n2)
    se = np.sqrt((phat * (1 - phat)) * (1/n1 + 1/n2))
    zcal = ((p1 - p2) - 0) / se

    z_table_negative = -(stats.norm.ppf(1 - alpha))
    p_value = stats.norm.cdf(zcal)

    return zcal, p_value, z_table_negative, se, (p1 - p2)

# UI
st.title("Two Proportion Z-Test")

if st.button("Calculate"):
    zcal, p_value, zcrit, se, diff = san()

    st.subheader("Results")
    st.write("Z calculated:", zcal)
    st.write("P-value:", p_value)
    st.write("Z critical (negative):", zcrit)
    st.write("Standard Error:", se)
    st.write("Difference (p1 - p2):", diff)

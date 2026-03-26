import streamlit as st
import numpy as np
from scipy import stats

def san(n1, n2, x1, x2, alpha):
    p1 = x1 / n1
    p2 = x2 / n2

    phat = (x1 + x2) / (n1 + n2)
    se = np.sqrt((phat * (1 - phat)) * (1/n1 + 1/n2))

    zcal = (p1 - p2) / se
    z_critical = stats.norm.ppf(1 - alpha)
    p_value = stats.norm.cdf(zcal)

    return zcal, p_value, z_critical, se, (p1 - p2)

# UI
st.title("Two Proportion Z-Test Calculator")

st.subheader("Enter Inputs")

n1 = st.number_input("Sample Size n1", min_value=1, value=400)
x1 = st.number_input("Successes in Sample 1", min_value=0, value=166)

n2 = st.number_input("Sample Size n2", min_value=1, value=380)
x2 = st.number_input("Successes in Sample 2", min_value=0, value=205)

alpha = st.number_input("Significance Level (alpha)", min_value=0.001, max_value=0.1, value=0.01)

if st.button("Calculate"):
    if x1 > n1 or x2 > n2:
        st.error("Successes cannot be greater than sample size")
    else:
        zcal, p_value, zcrit, se, diff = san(n1, n2, x1, x2, alpha)

        st.subheader("Results")
        st.write("Z calculated:", zcal)
        st.write("P-value:", p_value)
        st.write("Z critical (+):", zcrit)
        st.write("Z critical (-):", -zcrit)
        st.write("Standard Error:", se)
        st.write("Difference (p1 - p2):", diff)

        # Decision
        if p_value < alpha:
            st.success("Reject Null Hypothesis")
        else:
            st.info("Fail to Reject Null Hypothesis")

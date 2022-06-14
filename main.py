import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats

header = st.container()
content1 = st.container()
dist1 = st.container()
dist2 = st.container()
Ttest = st.container()

with header:
    st.title("Interactive Normal Distribution and T-test Page")

with content1:
    st.subheader("What affects a T-test?")
    st.text("The T-test result is affected by mean, standard deviation, and number of samples.")
    st.text("Play with these hyperparameters to see what happens to the T-test!")

with dist1:
    st.subheader("Control the hyperparameters of distribution 1:")
    mean = st.slider("what is the mean?", min_value = -3.0, max_value = 3.0, value=1.0, step=.1)
    stanDev = st.slider("What is the standard deviation?", min_value=0.1, max_value=3.0, step=.1, value=0.1)
    numSamps = st.slider("What is the number of samples?", min_value=10, max_value=1000, step=20, value=30)
    fig = plt.figure(figsize=(10,4))
    x = np.linspace(-5,5, 1000)
    y = (1/math.sqrt(2*math.pi*(stanDev**2))) * math.e ** (-.5 * (((x-mean)/stanDev)**2))
    plt.plot(x, y)
    st.pyplot(fig)


with dist2:
    st.subheader("Control the hyperparameters of distribution 2:")
    mean1 = st.slider("what is the mean?", min_value=-3.0, max_value=3.0, value=0.0, step=.1)
    stanDev1 = st.slider("What is the standard deviation?", min_value=0.1, max_value=3.0, step=.1, value=.3)
    numSamps1 = st.slider("What is the number of samples?", min_value=10, max_value=1000, step=20, value=10)
    fig = plt.figure(figsize=(10, 4))
    x = np.linspace(-5, 5, 1000)
    y = (1 / math.sqrt(2 * math.pi * (stanDev1 ** 2))) * math.e ** (-.5 * (((x - mean1) / stanDev1) ** 2))
    plt.plot(x, y)
    st.pyplot(fig)

with Ttest:
    st.subheader("Calculate the T-test")
    result = st.button("Calculate T-test")
    if result:
        df = numSamps + numSamps1 - 2
        tVal = (mean - mean1)/(math.sqrt((stanDev/numSamps)+(stanDev1/numSamps1)))
        PVal = scipy.stats.t.sf(abs(tVal), df=df) * 2
        st.text(f"The P-value is: {PVal}")

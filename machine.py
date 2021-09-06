import pickle
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

with open('machine_classifier.pickle', "rb") as f:
    clf = pickle.load(f)


def main():
    st.title("Machine classifier")
    air_t = st.number_input("air_temp")
    pro_t = st.number_input("process_temp")
    speed = st.number_input("rotate_speed")
    torque = st.number_input("torque")
    wear = st.number_input("tool_wear")

    if st.button("predict"):
        result = clf.predict([[air_t, pro_t, speed, torque, wear]])

        if result == 0:
            st.success("no fail :)")

        else:
            st.error("Fail!")


if __name__ == "__main__":
    main()

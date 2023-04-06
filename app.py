import pandas as pd
import streamlit as st


def parse(input_string: str) -> list[str]:
    return [s.strip() for s in input_string.split("\n")]


def main():
    st.write("# XLOOKUP App")

    col1, col2, col3 = st.columns(3)
    with col1:
        reference_names = st.text_input("Reference names go here.")
    with col2:
        reference_ids = st.text_input("Values for those reference names go here.")
    with col3:
        lookup_names = st.text_input(
            "Names for which you want to look up information go here."
        )

    list_reference_names = parse(reference_names)
    list_reference_ids = parse(reference_ids)
    if len(list_reference_ids) != len(list_reference_names):
        st.warning(
            "The Names and Values fields need to have the same number of inputs. Not continuing."
        )
    else:
        reference_dict = dict(zip(list_reference_names, list_reference_ids))
        lookup_ids = [
            reference_dict[name] if name in reference_dict else ""
            for name in lookup_names
        ]

        df = pd.DataFrame({"Names": lookup_names, "Value": lookup_ids})
        col4, col5 = st.columns(2)
        with col4:
            st.write(df)
        with col5:
            st.write(lookup_ids)


if __name__ == "__main__":
    main()

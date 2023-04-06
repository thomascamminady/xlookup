import streamlit as st


def parse(input_string: str) -> list[str]:
    parsed_input = []
    for s in input_string.split("\n"):
        s = s.strip()
        if s == "":
            continue
        if s[-1] == "," or s[-1] == ";":
            s = s[:-1]
        parsed_input.append(s)
    return parsed_input


def main():
    st.write("# XLOOKUP App")
    height = 400
    col1, col2, col3 = st.columns(3)
    with col1:
        reference_names = st.text_area("Reference names go here.", height=height)
    with col2:
        reference_ids = st.text_area(
            "Values for those reference go here.", height=height
        )
    with col3:
        lookup_names = st.text_area("Names to xlookup.", height=height)
    not_found_value = st.text_input("What do use when not present?", "#NAME?")
    if st.button("XLOOKUP"):
        list_reference_names = parse(reference_names)
        list_reference_ids = parse(reference_ids)
        list_lookup_names = parse(lookup_names)
        if len(list_reference_ids) != len(list_reference_names):
            st.warning(
                "The Names and Values fields need to have the same number of inputs. Not continuing."
            )
        else:
            reference_dict = dict(zip(list_reference_names, list_reference_ids))  # noqa
            list_lookup_ids = [
                reference_dict[name] if name in reference_dict else not_found_value
                for name in list_lookup_names
            ]

            col4, col5 = st.columns(2)
            with col4:
                st.write("Looked up values.")
                st.code("\n".join(list_lookup_ids))
            with col5:
                list_combined = [
                    f"{name},{id}"
                    for name, id in zip(list_lookup_names, list_lookup_ids)  # noqa
                ]
                st.write("Names and looked up values.")
                st.code("\n".join(list_combined))


if __name__ == "__main__":
    main()

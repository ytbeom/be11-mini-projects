import streamlit as st
from api import fetch_product_list


st.title("상품 가격 비교")
product = st.text_input("상품명을 입력하세요")

if product:
    item_list = fetch_product_list(product)
    for item in item_list:
        st.image(item.image)
        st.markdown(f"[{item.title}]({item.link})")
        st.write(f"가격: {item.lprice}, 쇼핑몰: {item.mall_name}")

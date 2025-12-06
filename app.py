import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = pd.DataFrame({
    "user_id": [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5],
    "item_id": [101,102,103,101,104,105,102,103,106,101,103,104,105,106,107],
    "rating" : [5,4,3,4,5,4,5,4,5,2,4,4,5,4,5]
})

st.title("🛒 Product Recommendation System")

pivot = data.pivot_table(index="user_id", columns="item_id", values="rating", aggfunc="mean").fillna(0)
similarity = cosine_similarity(pivot.values)
user_ids = pivot.index.tolist()
item_ids = pivot.columns.tolist()

user = st.selectbox("Choose User ID", user_ids)

if st.button("Get Recommendations"):
    idx = user_ids.index(user)
    scores = similarity[idx] @ pivot.values
    rated = pivot.iloc[idx] > 0
    scores[rated] = -1
    top_items = scores.argsort()[::-1][:5]
    recs = [item_ids[i] for i in top_items]
    st.write("Recommended Item IDs:", recs)

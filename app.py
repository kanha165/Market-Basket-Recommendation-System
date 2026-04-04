import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import networkx as nx

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Recommender", layout="wide")

# ---------------- CSS (NEXT LEVEL UI) ----------------
st.markdown("""
<style>

/* BACKGROUND */
body {
    background: linear-gradient(120deg, #eef2ff, #f8fafc);
}

/* HEADER */
.header {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 45px;
    border-radius: 18px;
    text-align: center;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 30px;
    animation: fadeIn 1s ease-in-out;
}

.header h1 {
    font-size: 40px;
}

.header p {
    font-size: 18px;
    opacity: 0.9;
}

/* GLASS CARD */
.card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.07);
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}

/* PRODUCT CARD */
.product-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.product-card:hover {
    transform: translateY(-8px);
}

/* PILLS */
.pill {
    display: inline-block;
    background: linear-gradient(90deg, #c7d2fe, #e0e7ff);
    padding: 8px 18px;
    border-radius: 50px;
    margin: 6px;
    font-weight: 500;
}

/* BADGES */
.badge {
    display: inline-block;
    background: linear-gradient(90deg, #fde68a, #fcd34d);
    padding: 8px 14px;
    border-radius: 10px;
    margin: 5px;
    font-weight: 600;
}

/* ANIMATION */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(10px);}
    to {opacity:1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>🛒 Market Basket Recommendation System</h1>
    <p>AI-powered recommendations using Apriori Algorithm</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("association_rules.csv")

df['antecedents'] = df['antecedents'].apply(eval)
df['consequents'] = df['consequents'].apply(eval)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Filters")

min_conf = st.sidebar.slider("Minimum Confidence", 0.0, 1.0, 0.3)
min_support = st.sidebar.slider("Minimum Support", 0.0, 1.0, 0.01)

# ---------------- ITEMS ----------------
all_items = list(set(item for sublist in df['antecedents'] for item in sublist))

# ---------------- INPUT ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

selected_items = st.multiselect(
    "🛒 Select Products",
    all_items,
    help="Choose multiple items"
)

get_btn = st.button("🚀 Get Recommendations")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RECOMMENDATION ----------------
if get_btn:

    st.subheader("🎯 Recommended Products")

    results = df[
        (df['confidence'] >= min_conf) &
        (df['support'] >= min_support) &
        (df['antecedents'].apply(lambda x: set(x).issubset(set(selected_items))))
    ]

    if not results.empty:
        cols = st.columns(3)

        for i, row in results.iterrows():
            with cols[i % 3]:
                st.markdown(f"""
                <div class="product-card">
                    <h4>🛍️ {list(row['consequents'])[0]}</h4>
                    <p>Confidence: {round(row['confidence'], 2)}</p>
                    <p>Support: {round(row['support'], 2)}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("❌ No recommendations found")

# ---------------- COMBOS ----------------
st.subheader("🛒 Frequently Bought Together")

top_combos = df.sort_values(by="support", ascending=False).head(6)

for _, row in top_combos.iterrows():
    combo = list(row['antecedents']) + list(row['consequents'])
    st.markdown(f"<span class='pill'>{' + '.join(combo)}</span>", unsafe_allow_html=True)

# ---------------- POPULAR ----------------
st.subheader("🔥 Most Popular Items")

item_freq = {}

for items in df['antecedents']:
    for item in items:
        item_freq[item] = item_freq.get(item, 0) + 1

top_items = sorted(item_freq.items(), key=lambda x: x[1], reverse=True)[:10]

for item, _ in top_items:
    st.markdown(f"<span class='badge'>{item}</span>", unsafe_allow_html=True)

# ---------------- GRAPH ----------------
st.subheader("📊 Product Relationship Graph")

G = nx.Graph()

for _, row in df.head(20).iterrows():
    for a in row['antecedents']:
        for b in row['consequents']:
            G.add_edge(a, b, weight=row['confidence'])

pos = nx.spring_layout(G)

edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

node_x, node_y = [], []
labels = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    labels.append(node)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=edge_x, y=edge_y,
    mode='lines',
    line=dict(width=1),
    hoverinfo='none'
))

fig.add_trace(go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=labels,
    textposition="top center",
    marker=dict(size=12)
))

fig.update_layout(showlegend=False)

st.plotly_chart(fig, use_container_width=True)
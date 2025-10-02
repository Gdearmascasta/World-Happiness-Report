import plotly.graph_objects as go

# Factores
factores = [
    "Explained by: Log GDP per capita",
    "Explained by: Social support",
    "Explained by: Healthy life expectancy",
    "Explained by: Freedom to make life choices",
    "Explained by: Generosity",
    "Explained by: Perceptions of corruption"
]

# Datos de ejemplo (resumen de tu HTML)
data = {
    "Colombia": {
        2019: [0.955, 0.891, 0.684, 0.562, 0.127, 0.084],
        2024: [0.965, 0.893, 0.728, 0.570, 0.125, 0.100]
    },
    "Finland": {
        2019: [1.340, 1.592, 0.986, 0.691, 0.153, 0.186],
        2024: [1.360, 1.605, 1.030, 0.725, 0.165, 0.178]
    },
    "Israel": {
        2019: [1.270, 1.220, 0.940, 0.635, 0.132, 0.084],
        2024: [1.295, 1.250, 0.990, 0.660, 0.142, 0.093]
    }
}

# Años disponibles
years = [2019, 2024]

# --- Gráfico inicial (primer año) ---
init_year = years[0]
fig = go.Figure()

for pais, valores in data.items():
    fig.add_trace(go.Scatterpolar(
        r=valores[init_year],
        theta=factores,
        fill='toself',
        name=pais
    ))

# --- Frames (para animar entre años) ---
frames = []
for y in years:
    frame_data = []
    for pais, valores in data.items():
        frame_data.append(go.Scatterpolar(
            r=valores[y],
            theta=factores,
            fill='toself',
            name=pais
        ))
    frames.append(go.Frame(data=frame_data, name=str(y)))

fig.frames = frames

# --- Layout con slider y botones ---
fig.update_layout(
    title="Comparación Normalizada de Factores (2019-2024)",
    polar=dict(radialaxis=dict(visible=True)),
    showlegend=True,
    sliders=[{
        "steps": [
            {
                "args": [[str(y)], {"frame": {"duration": 800, "redraw": True}, "mode": "immediate"}],
                "label": str(y),
                "method": "animate"
            } for y in years
        ],
        "x": 0.1,
        "len": 0.9
    }],
    updatemenus=[{
        "type": "buttons",
        "showactive": False,
        "x": 1.1,
        "y": 0,
        "buttons": [
            {"label": "▶ Play", "method": "animate", "args": [None, {"frame": {"duration": 1000}, "fromcurrent": True}]},
            {"label": "⏸ Pause", "method": "animate", "args": [[None], {"frame": {"duration": 0}, "mode": "immediate"}]}
        ]
    }]
)

# --- Guardar como HTML ---
fig.write_html("radar_chart.html")

print("✅ Archivo 'radar_chart.html' generado. Ábrelo en tu navegador para ver el radar interactivo.")

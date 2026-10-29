import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Conversor de temperatura",
    page_icon="🌡️",
    layout="centered"
)

# Título
st.title("🌡️ Conversor de temperatura")
st.write("Convierte fácilmente entre Celsius, Fahrenheit y Kelvin.")

# Entrada de temperatura
temperatura = st.number_input(
    "Ingresa la temperatura:",
    value=0.0,
    step=1.0
)

# Selección de unidades
col1, col2 = st.columns(2)

with col1:
    origen = st.selectbox(
        "Convertir desde:",
        ["Celsius", "Fahrenheit", "Kelvin"]
    )

with col2:
    destino = st.selectbox(
        "Convertir a:",
        ["Celsius", "Fahrenheit", "Kelvin"]
    )

# Conversión a Celsius
def convertir_a_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    elif unidad == "Fahrenheit":
        return (valor - 32) * 5 / 9
    else:
        return valor - 273.15

# Conversión desde Celsius
def convertir_desde_celsius(valor, unidad):
    if unidad == "Celsius":
        return valor
    elif unidad == "Fahrenheit":
        return (valor * 9 / 5) + 32
    else:
        return valor + 273.15

# Botón para convertir
if st.button("Convertir temperatura"):
    if origen == "Kelvin" and temperatura < 0:
        st.error("La temperatura en Kelvin no puede ser negativa.")
    else:
        # Convertir primero a Celsius
        celsius = convertir_a_celsius(temperatura, origen)

        # Validar el cero absoluto
        if celsius < -273.15:
            st.error("La temperatura no puede ser inferior al cero absoluto.")
        else:
            resultado = convertir_desde_celsius(celsius, destino)

            st.success("Conversión realizada correctamente")

            st.metric(
                label=f"Temperatura en {destino}",
                value=f"{resultado:.2f} °" +
                      ("C" if destino == "Celsius"
                       else "F" if destino == "Fahrenheit"
                       else "K")
            )
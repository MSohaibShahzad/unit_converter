import streamlit as st

st.set_page_config(page_title="UNIT CONVERTER")
st.title("Unit Converter")

st.markdown("""
    <style>
        .result-box {
        background-color: #077ef7;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 40px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    } 
    </style>
""",unsafe_allow_html=True)

# converter type 
category = st.selectbox("",["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"]) 

# unit list
if category == "Area":
    units = {
        "Square kilometre": 1_000_000,
        "Square metre": 1,
        "Square mile": 2_589_988.11,
        "Square yard": 0.836127,
        "Square foot": 0.092903,
        "Square inch": 0.00064516,
        "Hectare": 10_000,
        "Acre": 4046.86
    }

elif category == "Data Transfer Rate":
    units = {
        "bps": 1,
        "Kbps": 1000,
        "Mbps": 1_000_000,
        "Gbps": 1_000_000_000,
        "Tbps": 1_000_000_000_000
    }
    
elif category == "Digital Storage":
    units = {
        "Bit": 1,
        "Byte": 8,
        "Kilobyte": 8 * 1024,
        "Megabyte": 8 * 1024**2,
        "Gigabyte": 8 * 1024**3,
        "Terabyte": 8 * 1024**4
    }

elif category == "Energy":
    units = {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,
        "Kilocalorie": 4184,
        "Watt-hour": 3600,
        "Kilowatt-hour": 3.6e6,
        "BTU": 1055.06
    }

elif category == "Frequency":
    units = {
        "Hertz": 1,
        "Kilohertz": 1000,
        "Megahertz": 1_000_000,
        "Gigahertz": 1_000_000_000
    }

elif category == "Fuel Economy":
    units = {
         "MPG (US)": 1,
        "MPG (UK)": 1.20095,
        "L/100km": 235.215
    }

elif category == "Length":
    units = {
        "Kilometre": 1000,
        "Metre": 1,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Micrometre": 1e-6,
        "Nanometre": 1e-9,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }

elif category == "Mass":
    units = {
        "Tonne": 1000,
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Microgram": 1e-9,
        "Imperial Ton": 1016.05,
        "US Ton": 907.1847,
        "Stone": 6.35029,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }

elif category == "Plane Angle":
    units = {
         "Degree": 1,
        "Radian": 57.2958,
        "Gradian": 0.9
    }

elif category == "Pressure":
    units = {
         "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100_000,
        "PSI": 6894.76,
        "Atmosphere": 101325
    }

elif category == "Speed":
    units = {
        "m/s": 1,
        "km/h": 0.277778,
        "mph": 0.44704,
        "knot": 0.514444
    }

elif category == "Temperature":
   units = {
        "Celsius": "c",
        "Fahrenheit": "f",
        "Kelvin": "k"
    }

elif category == "Time":
    units = {
        "Second": 1,
        "Millisecond": 0.001,
        "Microsecond": 1e-6,
        "Nanosecond": 1e-9,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2628000,   
        "Year": 31536000
    }

elif category == "Volume":
    units = {
        "Cubic metre": 1,
        "Litre": 0.001,
        "Millilitre": 1e-6,
        "Cubic inch": 1.6387e-5,
        "Cubic foot": 0.0283168,
        "Gallon (US)": 0.00378541,
        "Gallon (UK)": 0.00454609
    }

def convert(val, from_u, to_u):
    if category == "Temperature":
        if from_u == to_u:
            return val
        elif from_u == "Celsius":
            if to_u == "Fahrenheit":
                return (val * 9/5) + 32
            elif to_u == "Kelvin":
                return val + 273.15
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (val - 32) * 5/9
            elif to_u == "Kelvin":
                return ((val - 32) * 5/9) + 273.15
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return val - 273.15
            elif to_u == "Fahrenheit":
                return ((val - 273.15) * 9/5) + 32
    else:
        base = val * units[from_u]
        return round(base / units[to_u],4)


# set auto value
if "left_value" not in st.session_state:
    st.session_state.left_value = 1
if "right_value" not in st.session_state:
    st.session_state.right_value = 1
if "from_unit" not in st.session_state:
    st.session_state.from_unit = list(units.keys())[0]
if "to_unit" not in st.session_state:
    st.session_state.to_unit = list(units.keys())[0]
if "last_edited" not in st.session_state:
    st.session_state.last_edited = "left"

# function for real time update

# update value of right side
def update_from_left():
    try:
        value = float(st.session_state.left_input)
        st.session_state.right_value = convert(value, st.session_state.from_unit, st.session_state.to_unit)
        st.session_state.left_value = value
        st.session_state.last_edited = "left"
    except:
        pass

# update value of left side
def update_from_right():
    try:
        value = float(st.session_state.right_input)
        st.session_state.left_value = convert(value, st.session_state.to_unit, st.session_state.from_unit)
        st.session_state.right_value = value
        st.session_state.last_edited = "right"
    except:
        pass

# update value when change unit
def update_units():
        st.session_state.right_value = convert(st.session_state.left_value, st.session_state.from_unit, st.session_state.to_unit)


# dropdown to select unit
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("", list(units.keys()), key="from_unit", on_change=update_units)
with col2:
    to_unit = st.selectbox("", list(units.keys()), key="to_unit", on_change=update_units)

# input fields 
col3, col4 = st.columns(2)

with col3:
    st.text_input("", 
                  key="left_input", 
                  value= str(st.session_state.left_value),
                  on_change=update_from_left, 
                  label_visibility="collapsed", 
                  placeholder="0")

with col4:
    st.text_input("", 
                  key="right_input", 
                  value= str(st.session_state.right_value),
                  on_change=update_from_right, 
                  label_visibility="collapsed", 
                  placeholder="0")

# result 
st.markdown(f"""
<div class="result-box">
    <span>{st.session_state.left_value} {from_unit}</span>
    <span>=</span>
    <span>{st.session_state.right_value} {to_unit}</span>
</div>
""", unsafe_allow_html=True)




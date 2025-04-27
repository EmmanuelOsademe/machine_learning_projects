import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import folium
import flood_tool as ft
from flood_tool.common.utils_visualization import (
    format_data,
    dummy_pipeline,
    high_risk_stations,
    format_rainfall,
    Risk_HeatMap,
    plot_flood_risk_map,
    get_heavy_rainfall_data,
    get_color
)
from sklearn import set_config
set_config(transform_output="pandas")
from flood_tool.geo import get_gps_lat_long_from_easting_northing
REQUIRED_COLUMNS = [
    "postcode",
    "easting",
    "northing",
    "soilType",
    "elevation",
    "nearestWatercourse",
    "distanceToWatercourse",
    "localAuthority",
]

post_data = pd.read_csv(
    "flood_tool/example_data/postcodes_unlabelled.csv"
)
coordinates_lat = get_gps_lat_long_from_easting_northing(post_data['easting'], post_data['northing'])
coordinates_df = pd.DataFrame({
    'latitude':coordinates_lat[0],
    'longitude':coordinates_lat[1]})

post = pd.concat([post_data, coordinates_df], axis=1)
POSTCODE = post.postcode.tolist()

station = pd.read_csv("flood_tool/resources/stations.csv")
STATION_ID = station.stationReference.tolist()

sector_data = pd.read_csv("flood_tool/resources/sector_data.csv")

@st.cache_resource
def create_tool():
    tool = ft.Tool()
    return tool
tool = create_tool()


# typical_weather = pd.read_csv("flood_tool/example_data/typical_day.csv")
# typical_weather = get_heavy_rainfall_data(typical_weather, station)
# wet_weather = pd.read_csv("flood_tool/example_data/wet_day.csv")
# wet_weather = get_heavy_rainfall_data(wet_weather, station)

st.sidebar.title("Flood Risk")

option = st.sidebar.selectbox(
    "Choose an option :", ["CSV File", "Post Code", "Latitude and Longitude"]
)

if option == "CSV File":
    st.sidebar.subheader("Upload your CSV with unlabelled data")
    uploaded_file = st.sidebar.file_uploader(
        "Select your CSV file", type="csv"
        )
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            missing_columns = [
                col for col in REQUIRED_COLUMNS if col not in df.columns
                ]
            if missing_columns:
                st.sidebar.error(
                    f"Missing Columns : {', '.join(missing_columns)}"
                )
            else:
                st.sidebar.success("All necessary columns are present.")

                if set(df.columns) != set(REQUIRED_COLUMNS):
                    st.sidebar.warning(
                        "Some columns are not useful and will be removed."
                    )
                    df = df[REQUIRED_COLUMNS]

                st.sidebar.write("Preview of the dataset :")
                st.sidebar.dataframe(df)
                st.write("### Risk map of the area selected")
                st.write("A dummy pipeline is used to generate the data, because we didn't have time to connect the models with streamlit")
                data = dummy_pipeline(df)
                merged_data = format_data(data, post)
                total_value = merged_data["house_price"].sum()
                folium_static(Risk_HeatMap(merged_data, sector_data))

                st.markdown(
                    """
                <div style="background-color: white;
                    border: 2px solid grey; padding: 10px; font-size: 14px;">
                    <strong>Legend:</strong><br>
                    <span style="color: black;">Info-sign Marker:</span>
                    Most Dangerous Area (Risk: 7)
                </div>
                """,
                    unsafe_allow_html=True,
                )

                st.metric(
                    label="Total value of houses", value=f"{total_value:,} £"
                    )
                # if st.button("Plot plot"):
                #     st.dataframe(merged_data)
                #     st.dataframe(wet_weather)
                #     folium_static(plot_flood_risk_map(merged_data,wet_weather))

                if st.button("Get rainfall data for high risk points"):
                    st.write(
                        "Rainfall data for high risk points (Risk Label = 7)"
                        )
                    hr_station = high_risk_stations(station, merged_data)
                    rainfall_data_station = format_rainfall(hr_station)
                    st.write(rainfall_data_station)

        except Exception as e:
            st.sidebar.error(f"Error will reading the file : {e}")

elif option == "Post Code":
    st.sidebar.subheader("Choose Post Code")
    selected_postcode = st.sidebar.selectbox(
        "Select Post Code:", POSTCODE
        )
    st.write(f'Prediction flood risk for postcode : {selected_postcode}')
    df = tool.predict_flood_class_from_postcode([selected_postcode]).to_frame().reset_index().rename(columns={'index': 'postcode', 0: 'riskLabel'})
    merged_data = format_data(df, post)
    st.title("Flood Risk Prediction Map")
    st.write("Click on the makers for further information")
    try:
        m = folium.Map(
        location=[merged_data['latitude'].mean(), merged_data['longitude'].mean()],
        zoom_start=8
    )
        marker_cluster = MarkerCluster().add_to(m)
        for _, row in merged_data.iterrows():
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=8,
                color=get_color(row['riskLabel']),
                fill=True,
                fill_color=get_color(row['riskLabel']),
                fill_opacity=0.7,
                popup=f"Postcode: {row['postcode']}<br>Risk Level: {row['riskLabel']}"
            ).add_to(marker_cluster)
        # Display the map in the Streamlit app
        folium_static(m)
    except ValueError:
        st.error("Postcode not found in the database")

    # Predict postcode and display the postcode on the map

# Not enough time to implement this feature
elif option == "Latitude and Longitude":
    st.sidebar.subheader("Type coordinates")
    latitude = st.sidebar.number_input("Latitude", format="%.6f")
    longitude = st.sidebar.number_input("Longitude", format="%.6f")
    if latitude or longitude:
        st.sidebar.write(f"Latitude : {latitude}, Longitude : {longitude}")
    st.title("WIP 👷🏻‍♀️")
    st.write("Not implemeted yet")

        # Predict latitude and longitude

import streamlit as st

st.set_page_config(page_title="Speedtest", page_icon="🏁", layout="wide")



def speedytest():
    c1, c2, c3 = st.columns(3)
    import speedtest as sp
    sts = sp.Speedtest()
    best_serv = sts.get_best_server()

    with c2:
        st.header("Starting speedtest")
        st.subheader(f"Found the best server : {best_serv['host']} in {best_serv['country']}")
    download = sts.download()
    upload = sts.upload()
    ping = sts.results.ping
    result = [f"Download : {download / 1024 / 1024:.2f} Mbps", f"Upload : {upload / 1024 / 1024:.2f} Mbps",
              f"Ping : {ping:.2f}"]
    with c2:
        st.success(result[0])
        st.error(result[1])
        st.warning(result[2])

st.title("UTTER FAILURE DONT USE")
if st.button("Start Speedtest"):
    speedytest()

import streamlit as st

st.set_page_config(page_title="Tính Tiền Phòng Trọ", page_icon="🏠")

st.image("logo.jpg", use_container_width=True)

st.title("🏠 Tính tiền phòng trọ - ĐỀ TÀI 1 ĐẶNG THỊ NGỌC HÂN 23030122; LÝ GIA HÂN 23030244; NGUYỄN NGỌC NHI 23030026; ĐỒNG THỊ LAN ANH 23030112; LÊ THỊ THANH TRÚC 23030125; ĐÀO THỊ NGỌC ÁNH 23030104")

# Nhập tiền phòng
A = st.number_input("Nhập số tiền phòng (đồng)", min_value=0.0, value=2000000.0)

st.subheader("⚡ Tiền điện")
a = st.number_input("Số điện đầu tháng", min_value=0.0, value=1500.0)
b = st.number_input("Số điện cuối tháng", min_value=0.0, value=1600.0)
c = st.number_input("Đơn giá 1 số điện (đồng)", min_value=0.0, value=3400.0)

B = (b - a) * c

st.subheader("💧 Tiền nước")
x = st.number_input("Số nước đầu tháng", min_value=0.0, value=200.0)
y = st.number_input("Số nước cuối tháng", min_value=0.0, value=210.0)
z = st.number_input("Đơn giá 1 số nước (đồng)", min_value=0.0, value=12000.0)

C = (y - x) * z

st.subheader("📌 Chi phí khác")
E = st.number_input("Nhập tiền WiFi", min_value=0.0, value=100000.0)

if st.button("💰 Tính tiền phòng"):
    D = A + B + C + E

    st.success(f"### Tổng số tiền phòng trọ của 1 tháng: {D:,.0f} đồng")

    st.write("### Chi tiết")
    st.write(f"- Tiền phòng: **{A:,.0f} đồng**")
    st.write(f"- Tiền điện: **{B:,.0f} đồng**")
    st.write(f"- Tiền nước: **{C:,.0f} đồng**")
    st.write(f"- Tiền WiFi: **{E:,.0f} đồng**")

# import streamlit as st
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# fig, ax = plt.subplots()
# ax.plot(x, y, color='green', marker='o')
# ax.set_title("Grafik Linear Sederhana")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")

# st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

jurusan = ["Informatika", "Sistem Informasi", "Desain", "Manajemen"]
jumlah = [120, 90, 60, 110]

plt.bar(jurusan, jumlah, color='orange')
plt.title("Jumlah Mahasiswa per Jurusan")
plt.xlabel("Jurusan")
plt.ylabel("Jumlah Mahasiswa")
plt.grid(True)
st.pyplot(plt.gcf())
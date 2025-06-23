# 🖼️ Image Size Reducer (Offline & Secure)

A simple, privacy-focused Python tool to **reduce image file sizes** without uploading to the internet. Ideal for compressing images for online forms, applications, or email attachments — while keeping sensitive data safe.

---

## 🚀 Features

- 📉 **Reduces image size by lowering quality incrementally**
- 🔒 **Works completely offline** – no data ever leaves your system
- 📂 Supports common formats: `.jpg`, `.jpeg`, `.png`
- ⚙️ Customizable output quality range (maintains quality at ~70–80%)
- ⚡ Fast and lightweight
- 🧠 Ideal for compressing scanned documents or passport-size photos

---

## 🖥️ How It Works

The script loops through supported images and compresses them by reducing their quality step-by-step until a size threshold is met or the quality drops below a set limit. This ensures balance between **file size** and **readable quality**.

---

## 📸 Screenshots

>![image](https://github.com/user-attachments/assets/bee7ef27-6baf-4636-8e49-bab238a348e1)


---

## 🛠️ Technologies Used

- Python 3.x
- PIL (Pillow)

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/image-size-reducer.git
cd image-size-reducer
pip install -r requirements.txt


import qrcode

# Создаем объект QRCode с текстом, который будет закодирован в QR-коде
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("Hello, World!")

# Создаем изображение QR-кода
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Сохраняем изображение QR-кода в файл
img.save("qr_code.png")

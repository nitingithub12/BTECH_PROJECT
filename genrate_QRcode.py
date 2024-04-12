import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
    
)
data="http://www.youtube.com/@Concept_in_11min"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('text.png')



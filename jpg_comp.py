from PIL import Image
jpg_path = 'src/images/highlights/1755944564768.png'
img = Image.open(jpg_path)
# img = img.resize((640, 480), Image.ANTIALIAS)
img.save(jpg_path, quality=85, optimize=True)

from PIL import Image

# 画像ファイルのパスを指定して読み込み
image_path = "path/to/your/image.jpg"
image = Image.open(image_path)

# アップスケールと高画質化の処理
upscaled_image = image.resize((image.width * 2, image.height * 2), resample=Image.LANCZOS)

# 処理後の画像を保存
upscaled_image.save("path/to/save/upscaled_image.jpg")
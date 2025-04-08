from fastapi import UploadFile
import cloudinary.uploader
import os

async def upload_file(file: UploadFile, folder: str) -> str:
    contents = await file.read()
    extension = os.path.splitext(file.filename)[-1].lower()

    upload_options = {"folder": folder}
    if extension not in [".jpg", ".jpeg", ".png"]:
        upload_options["format"] = "jpg"

    result = cloudinary.uploader.upload(contents, **upload_options)
    return result["secure_url"]

def extract_public_id(url: str) -> str:
    # Eliminar extensión
    without_extension = url.rsplit('.', 1)[0]

    # Buscar carpetas conocidas
    for folder in ["profile-images", "servicios"]:
        if f"/{folder}/" in without_extension:
            index = without_extension.index(f"/{folder}/")
            return without_extension[index + 1:]

    raise ValueError("URL no válida: no contiene carpetas conocidas")

async def delete_file(url: str):
    try:
        if not any(folder in url for folder in ["profile-images", "servicios"]):
            return
        public_id = extract_public_id(url)
        cloudinary.uploader.destroy(public_id)
    except Exception:
        pass  # Silenciar errores como en el servicio original

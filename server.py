python
     from fastapi import FastAPI, UploadFile, File
     import uvicorn
     from drive_service import upload_file_to_drive
     from PIL import Image
     import io

     app = FastAPI()

     @app.post("/upload/")
     async def upload_file(file: UploadFile = File(...)):
         contents = await file.read()
         image = Image.open(io.BytesIO(contents))
         file_path = f"temp/{file.filename}"
         image.save(file_path)
         file_id = upload_file_to_drive(file_path, file.filename)
         return {"file_id": file_id}

     if __name__ == "__main__":
         uvicorn.run(app, host="0.0.0.0", port=8000)
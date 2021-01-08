from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):    
    return {        
        "file_size": len(file)
        }


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):    
    contents = await file.read()
    print(contents)
    return {
        "file": file.file,        
        "filename": file.filename,
        "content_type": file.content_type,
        }

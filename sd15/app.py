from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

app = FastAPI()

# Load Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate", response_class=FileResponse)
def generate_image(req: PromptRequest):
    try:
        image = pipe(req.prompt).images[0]
        filename = f"/tmp/{uuid.uuid4().hex}.png"
        image.save(filename)
        return FileResponse(filename, media_type="image/png", filename="generated.png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

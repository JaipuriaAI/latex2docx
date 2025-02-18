from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
import tempfile
from fastapi.responses import FileResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class LatexRequest(BaseModel):
    latex: str

@app.post("/convert")
async def convert_latex_to_word(request: LatexRequest):
    try:
        # Create a temporary LaTeX file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".tex") as tmp_tex:
            tmp_tex.write(request.latex.encode('utf-8'))
            tmp_tex_path = tmp_tex.name

        # Create a temporary Word file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
            tmp_docx_path = tmp_docx.name

        # Convert LaTeX to Word using Pandoc
        subprocess.run(
            ["pandoc", tmp_tex_path, "-o", tmp_docx_path],
            check=True
        )

        return FileResponse(tmp_docx_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename="document.docx")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the application, use the command: uvicorn main:app --reload

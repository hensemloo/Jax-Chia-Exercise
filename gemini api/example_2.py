import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
app = FastAPI(title="Text Translator API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", api_key=GEMINI_API_KEY)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}. Translate the provided sentence only."
        ),
        (
            "human",
            "{input}"
        ),
    ]
)

chain = prompt | llm | StrOutputParser()


class TranslationRequest(BaseModel):
    input_language: str
    output_language: str
    text_input: str


class TranslationResponse(BaseModel):
    translated_text: str


@app.post("/translate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        result = chain.invoke(
            {
                "input_language": request.input_language,
                "output_language": request.output_language,
                "input": request.text_input,
            }
        )
        return TranslationResponse(translated_text=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")


@app.get("/")
def root():
    return {"message": "Text Translator API is running"}

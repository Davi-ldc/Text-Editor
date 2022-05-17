import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Corrija isso para Português:\nportugues e minha materia fovorita \n\nPortuguês é minha matéria favorita.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

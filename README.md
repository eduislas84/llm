# llm

ollama serve

ollama list

# Api generate response (Respuesta Separada)
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola",
}'

# Respuesta Junta
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola",
  "stream":false
}'
# seed.py
import json
import os
from google import genai
from google.cloud import firestore
from google.cloud.firestore_v1.vector import Vector
import time

db = firestore.Client(database="coffee-menu")
client = genai.Client(
   vertexai=True,
   project=os.environ.get("PROJECT_ID"),
   location="us-central1"
)

with open("menu.json", "r") as f:
   menu_items = json.load(f)

for item in menu_items:
   # Use the name as the document ID
   doc_id = item["name"].lower().replace(" ", "-")

   # Generate text embedding using Gemini Enterprise Agent Platform text-embedding-005 model
   text_to_embed = f"{item['name']}: {item['description']}"
   response = client.models.embed_content(
       model="text-embedding-005",
       contents=text_to_embed,
   )
   embedding = response.embeddings[0].values

   # Add embedding vector to the menu item data
   item["embedding"] = Vector(embedding)

   db.collection("menu").document(doc_id).set(item)
   time.sleep(2)

print("Firestore menu collection seeded with vector embeddings successfully!")

import json
import os

def make_json (title, body, url, author, media, created_at, category, image_url, file_name = "test") :

    data = {
        "title" : title,
        "body" : body,
        "media" : media,
        "author" : author,
        "url" : url,
        "category" : category,
        "created_at" : created_at,
        "image_url" : image_url
        }


    base_path = "../sample"
    extension = ".json"

    file_path = os.path.join(base_path, file_name) + extension
    
    
    with open(file_path, "w", encoding = "utf-8") as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)

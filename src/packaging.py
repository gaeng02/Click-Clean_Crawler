import json
import os

def make_json (title, raw_contents, url, reporter, media, date, tag = "기타", file_name = "test") :

    data = {
        "title" : title,
        "body" : raw_contents,
        "media" : media,
        "author" : reporter,
        "url" : url,
        "category" : tag,
        "created_at" : date
        }


    base_path = "../sample"
    extension = ".json"

    file_path = os.path.join(base_path, file_name) + extension
    
    
    with open(file_path, "w", encoding = "utf-8") as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)

    print("Done")

if (__name__ == "__main__") : 
    make_json ("Title", "<article> text</article>", "https://www.url.com", "Name", "Media", "2024-11-14. 09:30", "테스트")

import json
import os

def make_json (title, raw_contents, url, reporter, media, date, tag = "기타", file_name = "test") :

    data = {
        "title" : title,
        "raw_contents" : raw_contents,
        "url" : url,
        "reporter" : reporter,
        "media" : media,
        "date" : date,
        "tag" : tag
        }

    base_path = "../sample"
    file_path = os.path.join(base_path, file_name)
    file_path += ".txt"
    
    with open(file_path, "w", encoding = "utf-8") as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)

    print("Done")

if (__name__ == "__main__") : 
    make_json ("Title", "<article> text</article>", "https://www.url.com", "Name", "Media", "2024-11-14. 09:30", "테스트")

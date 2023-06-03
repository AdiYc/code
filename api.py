
import requests
import json

api_key = "dJkUViTXu5IrkESj9/of3A==Avh9awTJPrVhqJfF"

class api: 

    def textsimilarity(text_1, text_2): 
        if len(text_1) == 0 or len(text_2) == 0: 
            return "itu teks kosong kocak"
        
        api_url = "https://api.api-ninjas.com/v1/textsimilarity"

        body = {
            "text_1": f"{text_1}",
            "text_2": f"{text_2}"
        }

        res = requests.post(api_url, headers={'X-Api-Key': f'{api_key}'}, json=body)

        if res.status_code == 200: 
            response_json = json.loads(res.text)  
            similarity_score = response_json["similarity"]
            return similarity_score
        
        return res.status_code, res.text
        
    def objectdetection(image_url): 
        if len(image_url) == 0:
            return "mana gambar nya kocak" 

        api_url = 'https://api.api-ninjas.com/v1/objectdetection'

        image_file = open(f'{image_url}', 'rb')
        file = {'image': image_file}
        res = requests.post(api_url, headers={'X-Api-Key': f'{api_key}'}, files=file)
        
        if res.status_code == 200 : return res.text
        
        return res.status_code, res.text

    def ip_lookup(ip): 
        api_url = 'https://api.api-ninjas.com/v1/iplookup?address={}'.format(ip)

        res = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})

        if res.status_code == 200: return res.text

        return res.status_code, res.text

print(api.ip_lookup("103.63.24.99"))
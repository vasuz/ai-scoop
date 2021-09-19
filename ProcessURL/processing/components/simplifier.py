import requests
import json

def diff_limiter(original, incoming, max_multi):
    endpoint = "https://api.diffchecker.com/public/text?email=no-reply@pizzahut.com&diff_level=word&output_type=json"

    resp = json.loads(requests.post(endpoint, json = {"left": original, "right": incoming}).content)
    resp = resp.get("rows", [])

    # Find all differences between original & incoming text
    # If original*max_multi is a lower length than incoming, keep original
    output = ""
    for row in resp:
        for l, r in zip(row.get("left").get("chunks"), row.get("right").get("chunks")):
            if l.get("type") == "remove" and r.get("type") == "insert":
                l_val = l.get("value")
                r_val = r.get("value")
                l_size = len(l_val.split(' '))
                r_size = len(r_val.split(' '))
                
                if l_size * max_multi > r_size:
                    #print(f"Replacing {l_val} with {r_val}")
                    output += r_val
                else:
                    #print(f"Keeping {l_val} as-is")
                    output += l_val
            else:
                output += l.get("value")

    return output

def clean_text(text):
    text = text.strip(' ') \
        .replace('  ', ' ') \
        .replace(' .', '.')
    return text

def simplify_text(text):
    endpoint = "https://rewordify.com/rwprocess.php"
    data= {
        's': text
    }
    request = requests.post(endpoint, data=data).json()

    request_words = request["RewordifiedString"].replace("%@", "")[:-36]

    tilde_round = ""
    flag = False
    for char in request_words:
        if not flag and char != "~":
            tilde_round += char
            continue
        
        if flag and char == "~":
            flag = False
        elif not flag and char == "~":
            flag = True

    tag_round = ""
    flag = False
    for char in tilde_round:
        if not flag and char != "<":
            tag_round += char
            continue

        if flag and char == ">":
            flag = False
        elif not flag and char == "<":
            flag = True

    simplified = tag_round.replace("[_", "").replace("_]", "")

    # Cap diff sizes to 3x original text
    simplified = diff_limiter(text, simplified, 3.0)

    # Clean final output
    simplified = clean_text(text)
    
    return simplified
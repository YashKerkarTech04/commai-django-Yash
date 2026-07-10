import requests

def evaluate_conversation_grammar(text):
    url = "https://api.languagetool.org/v2/check"

    data = {
        "text": text,
        "language": "en-US",
    }

    try:
        response = requests.post(url, data=data, timeout=10)

        # Debugging (temporary)
        print("LanguageTool Status:", response.status_code)

        if response.status_code != 200:
            print("LanguageTool Response:")
            print(response.text)
            return []

        try:
            result = response.json()
        except ValueError:
            print("LanguageTool returned invalid JSON")
            print(response.text)
            return []

        corrections = []

        for match in result.get("matches", []):
            start = match["offset"]
            end = start + match["length"]

            corrections.append({
                "full_text": text,
                "before_error": text[:start],
                "error_text": text[start:end],
                "after_error": text[end:],
                "suggestion": [r["value"] for r in match.get("replacements", [])[:6]],
                "message": match.get("message", ""),
                "offset": match.get("offset", 0),
                "length": match.get("length", 0),
            })

        return corrections

    except requests.exceptions.RequestException as e:
        print("LanguageTool Request Failed:", e)
        return []

def evaluate_grammer_spelling(text):
    if text is None:
        return {"Grammar and Spelling": []}
    
    return {"Grammar and Spelling": evaluate_conversation_grammar(text)}



# print(evaluate_grammer_spelling("Remember the name - Ankit and Yash , they are the founders of Commai"))




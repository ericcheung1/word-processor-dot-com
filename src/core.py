import httpx

def format_payload(comments):
    """
    """
    
    payload = {
        "user_id": [],
        "comment_id": [],
        "comments": []
    }
    for comment in comments:
        payload["user_id"].append(comment["user_id"])
        payload["comment_id"].append(comment["comment_id"])
        payload["comments"].append(comment["comment"])

    return payload

def call_sentiment_endpoint(payload):
    """
    """

    # TODO: in call_sentiment_endpoint define api endpoint at client start-time
    response = httpx.post("", json=payload)
    # TODO: in call_sentiment_endpoint add error handling
    return response.json()

def calculate_final_sentiment(response_json):
    """
    """

    sentiment_count = {"NEGATIVE": 0, "POSITIVE": 0}
    sentiment_confidence = float(0)

    for result in response_json:

        sentiment_confidence+=max(result["sentiment_confidence"])

        if result["sentiment_classification"] == "NEGATIVE":
            sentiment_count["NEGATIVE"]+=1
        else:
            sentiment_count["POSITIVE"]+=1

    mean_conf = sentiment_confidence/len(response_json)
    return [{"sentiment_count": sentiment_count},
            {"sentiment_confidence": round(mean_conf, 3)},
            {"sentiment_results": response_json}]


def orchestrate_pipeline(comments):
    """
    """
    payload = format_payload(comments)

    response = call_sentiment_endpoint(payload)

    final_result = calculate_final_sentiment(response)

    return final_result

if __name__ == "__main__":
    result = orchestrate_pipeline("")
    print(result)
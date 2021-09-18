from processing import processor

def process(url):
    proc = processor.Processor(url)

    return {
        "url": url,
        "summary": proc.summarize(),
        "cw_puzzle": "imageurlhere",
        "ws_puzzle": "imageurlhere",
        "keywords": proc.keywords()
    }
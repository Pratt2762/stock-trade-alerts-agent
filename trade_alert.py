from playwright.sync_api import sync_playwright

def get_latest_tweets(username, count=5):
    tweets = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://twitter.com/{username}")

        page.wait_for_selector('article', timeout=10000)  # wait for tweets to load

        articles = page.query_selector_all('article')
        for article in articles[:count]:
            try:
                tweet_text = article.inner_text()
                tweets.append(tweet_text)
            except Exception as e:
                print("Error reading tweet:", e)

        browser.close()
    return tweets

# Example usage
tweets = get_latest_tweets("VVVStockAnalyst", count=1)
for tweet in tweets:
    print("------\n", tweet)
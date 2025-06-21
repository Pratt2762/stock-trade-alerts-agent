from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_latest_tweets(username, count=3):
    # Configure Brave browser
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open Twitter profile page
    driver.get(f"https://twitter.com/{username}")
    time.sleep(5)  # Wait for tweets to load

    # Scroll down slightly to make sure multiple tweets load
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(3)

    # Grab tweets
    tweets = []
    articles = driver.find_elements(By.TAG_NAME, "article")
    
    for article in articles[:count]:
        try:
            tweet_text = article.text
            tweets.append(tweet_text)
        except Exception as e:
            print("Error extracting tweet:", e)

    driver.quit()
    return tweets

# Example usage
latest = get_latest_tweets("VVVStockAnalyst", count=3)
for i, tweet in enumerate(latest, 1):
    print(f"\n--- Tweet {i} ---\n{tweet}")
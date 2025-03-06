import sys
import logging

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_twitter_scraper(username):
    try:
        import snscrape.modules.twitter as twitter
        logger.info("Successfully imported Twitter module")
        
        # Test user scraper
        try:
            user_scraper = twitter.TwitterUserScraper(username)
            logger.info(f"Created scraper for user: {username}")
            
            # Try to get items
            items = list(user_scraper.get_items())
            logger.info(f"Retrieved {len(items)} items")
            
            # Print details of first item if available
            if items:
                first_item = items[0]
                print("First item details:")
                print(f"Type: {type(first_item)}")
                print(f"Str representation: {str(first_item)}")
            else:
                print("No items retrieved")
        
        except Exception as e:
            logger.error(f"Error in user scraper: {e}")
            import traceback
            traceback.print_exc()
    
    except ImportError as e:
        logger.error(f"Import error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else 'textfiles'
    test_twitter_scraper(username)

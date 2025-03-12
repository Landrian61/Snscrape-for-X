import sys
import logging
# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_twitter_scraper(username):
    try:
        import snscrape.modules.twitter as twitter
        logger.info("Successfully imported Twitter module")
        
        # Initialize the auth token manager with OAuth credentials
        oauth_credentials = {
            'consumer_key': 'n8GF7hIL10M608i3LYRXFxumP',
            'consumer_secret': 'D6RYY5JCtNQYTbrq4IDX220AohY2UH3C5LpUG5WQwp3x9abGVr',
            'access_token': '1602626818070249472-uetAnmjpWed3AtT4dpX9uUU2XbUeFJ',
            'access_token_secret': 'mbND7wwOV3Rfo4ixHmwGqFeakWtpHB15WJdzd9C6hAm4v'
        }
        
        # You can also provide your bearer token as a fallback
        bearer_token = 'AAAAAAAAAAAAAAAAAAAAAM8CzwEAAAAAX%2BgOFzmH6aMGamdoyFQ%2Bc1XrUX8%3DRjyZP06xnBUvOfubhQkS3RfENHIqbr7BEnFLhL46ZvOCZsq3Rq'
        
        # Try creating a basic scraper first to check compatibility
        logger.info("Testing basic scraper before adding authentication")
        basic_scraper = twitter.xUserScraper(username)
        
        # Create the auth manager - check if the class exists and has the expected signature
        try:
            if hasattr(twitter, 'AuthTokenManager'):
                auth_manager = twitter.AuthTokenManager(oauth_credentials, bearer_token)
                logger.info("Created authentication token manager")
                
                # Test user scraper with authentication
                user_scraper = twitter.xUserScraper(username, authTokenManager=auth_manager)
                logger.info(f"Created authenticated scraper for user: {username}")
            else:
                logger.warning("AuthTokenManager not found, falling back to unauthenticated mode")
                user_scraper = basic_scraper
        except Exception as auth_error:
            logger.error(f"Authentication setup error: {auth_error}")
            logger.warning("Falling back to unauthenticated mode")
            user_scraper = basic_scraper
        
        # Try to get items
        try:
            logger.info("Attempting to retrieve items")
            # Limited number of items to avoid potential rate limits
            items = []
            for i, item in enumerate(user_scraper.get_items()):
                items.append(item)
                if i >= 10:  # Limit to 10 items
                    break
            
            logger.info(f"Retrieved {len(items)} items")
            
            # Print details of first item if available
            if items:
                first_item = items[0]
                print("First item details:")
                print(f"Type: {type(first_item)}")
                print(f"Str representation: {str(first_item)}")
            else:
                print("No items retrieved")
                
        except TypeError as type_error:
            if "json" in str(type_error):
                logger.error("Detected JSON parameter error in the snscrape library")
                logger.info("This version of snscrape has an incompatibility with the _request() method")
                logger.info("You may need to modify the snscrape library or use a different version")
            raise
        except Exception as e:
            logger.error(f"Error in scraper: {e}")
            import traceback
            traceback.print_exc()
    
    except ImportError as e:
        logger.error(f"Import error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else 'textfiles'
    test_twitter_scraper(username)
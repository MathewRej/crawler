import argparse
import logging

logger = None


def parse_args():
    parser = argparse.ArgumentParser(description="Web crawler")
    parser.add_argument(
        "-d", "--debug", help="Enable debug logging", action="store_true"
    )
    return parser.parse_args()


def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("crawler")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter(
        "[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s"
    )
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)


def crawl():
    logger.debug("Crawling starting")
    for i in range(10):
        logger.debug("Fetching URL %s", i)
        print("https://....")
    logger.debug("Completed crawling")


def main():
    args = parse_args()
    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)

    crawl()


if __name__ == "__main__":
    main()
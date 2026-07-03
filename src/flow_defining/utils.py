import logging

logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")


def banner(title: str, char: str = "=", width: int = 70) -> None:
    logger.info(char * width)
    logger.info(title)
    logger.info(char * width)


SOURCE_PROMPTS = [
    {
        "key": "youtube_links",
        "title": "YOUTUBE VIDEOS/CHANNELS",
        "hints": [
            "Individual video URLs (e.g., https://youtube.com/watch?v=abc123)",
            "Channel URLs (e.g., https://youtube.com/@channelname)",
            "Multiple links separated by commas",
        ],
        "prompt": "Enter YouTube links (or press Enter to skip): ",
    },
    {
        "key": "webpage_links",
        "title": "WEB PAGES/ARTICLES",
        "hints": [
            "Documentation URLs",
            "Blog posts or tutorials",
            "Multiple links separated by commas",
        ],
        "prompt": "Enter web page URLs (or press Enter to skip): ",
    },
    {
        "key": "research_paper_links",
        "title": "RESEARCH PAPERS (arXiv)",
        "hints": [
            "arXiv URLs (e.g., https://arxiv.org/abs/2103.xxxxx)",
            "Paper titles or arXiv IDs",
            "Multiple entries separated by commas",
        ],
        "prompt": "Enter research paper links/queries (or press Enter to skip): ",
    },
    {
        "key": "document_paths",
        "title": "DOCUMENTS (PDF/Text/Markdown)",
        "hints": [
            "Local file paths to PDFs",
            "Text file paths (.txt)",
            "Markdown file paths (.md, .mdx)",
            "Multiple paths separated by commas",
        ],
        "prompt": "Enter document paths (or press Enter to skip): ",
    },
]

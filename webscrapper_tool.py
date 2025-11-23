import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig,CacheMode,PruningContentFilter,DefaultMarkdownGenerator


async def Webscrapper(url):
    print(f"Acessando o URL: {url}")

    pruning_filter = PruningContentFilter(
        threshold=0.10, 
        threshold_type="fixed",
        min_word_threshold=1 
    )
    md_generator = DefaultMarkdownGenerator(
        content_filter=pruning_filter,
        options={
            "ignore_links": False,  
            "ignore_images": True,   
            "escape_html": False   
        }
    )

    Config = CrawlerRunConfig(
        markdown_generator=md_generator,
        excluded_tags=['nav', 'footer', 'header', 'aside', 'script', 'style', 'noscript'],
        
        word_count_threshold=1,

        js_code= """
        await new Promise(r => setTimeout(r,10000))
    window.scrollTo(0, document.body.scrollHeight);
            await new Promise(r => setTimeout(r, 2000));
            window.scrollTo(0, document.body.scrollHeight);
            document.querySelectorAll('svg').forEach(el => el.remove());
            document.querySelectorAll('img').forEach(el => el.remove());
    """,

    cache_mode=CacheMode.BYPASS,
    delay_before_return_html=20.0,
    )
 
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            config=Config
        )
        return result



if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        url=sys.argv[1]
    else:
        url = "https://www.senai-ce.org.br/cursos?cidade=44"
    resultado = asyncio.run(Webscrapper(url))
    print(resultado.markdown[0:1000])

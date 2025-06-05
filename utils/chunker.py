from os import listdir
from markitdown import MarkItDown
from chonkie import RecursiveChunker

def chunkFiles():
    for f in listdir("data"):
        md = MarkItDown()
    result = md.convert(f"data/{f}")
    markdown_doc = result.text_content
    chunker = RecursiveChunker.from_recipe("markdown", lang="en")
    chunks = chunker.chunk(markdown_doc)
    print(chunks)
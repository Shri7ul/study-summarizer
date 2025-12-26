# text chunking logic
def chunk_text(blocks, chunk_size=3):
    """
    blocks: list[str]  (cleaned slide/page texts)
    chunk_size: how many slides/pages per chunk
    returns: list[str] (combined chunks)
    """

    chunks = []
    current_chunk = []

    for idx, block in enumerate(blocks, start=1):
        current_chunk.append(block)

        if idx % chunk_size == 0:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = []

    # leftover blocks
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    return chunks

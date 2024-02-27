import wikipedia
import hashlib


def get_wikipedia_page_text(page_title: str = "Line_(geometry)") -> str:    
    # auto_suggest=False because https://stackoverflow.com/a/69886635
    page = wikipedia.page(title=page_title, auto_suggest=False)
    return page.content
    

def build_chunk_df(wiki_urls: list[str]) -> pd.DataFrame:
    chunk = []
    chunk_hash = []
    source_url = []
    
    for url in wiki_urls:
        docs = load_wikipedia_page_chunks(url)
        for d in docs:
            chunk.append(d.page_content)
            hash = hashlib.md5(d.page_content.encode()).hexdigest()
            chunk_hash.append(hash)
            source_url.append(url)

    return pd.DataFrame({
        "chunk": chunk,
        "chunk_hash": chunk_hash,
        "source_url": source_url,
    })


def get_x_is_kind_of_y_from_df(chunk_df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    xy_dfs = []
    thoughts = []
    for _, row in chunk_df.iterrows():
        chatgpt_answer = get_x_is_a_kind_of_y_from_chunk(row.chunk)
        thoughts.append(chatgpt_answer.thoughts)
        df = chatgpt_csv_output_to_pandas(chatgpt_answer.csv_output)
        df["chunk_hash"] = row.chunk_hash
        xy_dfs.append(df)
        
    all_xy_df = pd.concat(xy_dfs)
    return all_xy_df, thoughts
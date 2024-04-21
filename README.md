Extracting a knowledge graph from Wikipedia articles on Geometry using LLMs.

Have a look at the notebooks:
- `manually_annotate_polygon_wikipedia_article.ipynb`
- `extract_kg.ipynb`

### TODO:

1. calculate metrics better, accounting for equivalences in the graph, e.g. `square -> 4-gon -> polygon` is almost as good as
`square <- polygon -> 4-gon`
2. add annotations for same-as relationship, e.g. 3-gon is same as triangle
3. use pydantic and `tools` API to format ChatGPT output in a JSON
4. take a long-context model like Claude instead of atomic chunks, compare the results
5. Try extracting all terms as NER first, then do $N^2$ calls to check if connections exist. Compare the connection calls with and without context chunk.

# Text Cleaning

## Interface

### Object Types

We either clean `text` or `tokens`.
The `tokens` can be either `str` or `data_structures.Token`.
The `data_structures` module is the repository `doublethinklab/data-structures.git`.

### Pipelines

Pipelines apply to either `text` or `tokens`, and a `genre` and `language`.

Most basic interface example:

```python
from text_cleaning import get_pipelines

clean_text, clean_tokens = get_pipelines('en', 'facebook')
text = clean_text('Whatever the text is')
# note that tokens can be either a string or `data_structures.Token`s
tokens = some_nlp_function_that_tokenizes(text)
tokens = clean_tokens(tokens)
```

Note that we also have a `'generic'` option for the genre.

The idea is that behind the scenes there are decisions already made about how
best to clean the text and tokens for each genre and language.
Consumers can just use these cleaners without need to worry about the details.
However, the design does allow for tweaking any of those details.
Just be aware that experience shows that testing any given configuration of 
cleaning functions into a pipeline is actually quite sensitive and fraught with 
errors.
Quite some time was spent making the unit tests pass.

## Dependencies

Some cleaning functions break if another goes before them.
The following table attempts to track these dependencies.
Note that since all classes are in the `text_cleaning` module, we omit that
for brevity here.

|Function|Dependencies|
|-|-|
|`functions.text.StandardizeText`|`functions.text.LowerCaseText`|

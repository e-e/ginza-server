### Endpoint

`http://localhost:5000?text=これは本です。それは本でした。`

### Output

```
[
    {
        "original_sentence": "これは本です。",
        "parts": [
            {
                "dep": "iobj",
                "head_index": 2,
                "index": 0,
                "lemma": "此れ",
                "pos": "PRON",
                "tag": "代名詞",
                "word": "これ"
            },
            {
                "dep": "case",
                "head_index": 0,
                "index": 1,
                "lemma": "は",
                "pos": "ADP",
                "tag": "助詞-係助詞",
                "word": "は"
            },
            {
                "dep": "ROOT",
                "head_index": 2,
                "index": 2,
                "lemma": "本",
                "pos": "NOUN",
                "tag": "名詞-普通名詞-一般",
                "word": "本"
            },
            {
                "dep": "cop",
                "head_index": 2,
                "index": 3,
                "lemma": "です",
                "pos": "AUX",
                "tag": "助動詞",
                "word": "です"
            },
            {
                "dep": "punct",
                "head_index": 2,
                "index": 4,
                "lemma": "。",
                "pos": "PUNCT",
                "tag": "補助記号-句点",
                "word": "。"
            }
        ]
    },
    {
        "original_sentence": "それは本でした。",
        "parts": [
            {
                "dep": "nsubj",
                "head_index": 7,
                "index": 5,
                "lemma": "其れ",
                "pos": "PRON",
                "tag": "代名詞",
                "word": "それ"
            },
            {
                "dep": "case",
                "head_index": 5,
                "index": 6,
                "lemma": "は",
                "pos": "ADP",
                "tag": "助詞-係助詞",
                "word": "は"
            },
            {
                "dep": "ROOT",
                "head_index": 7,
                "index": 7,
                "lemma": "本",
                "pos": "NOUN",
                "tag": "名詞-普通名詞-一般",
                "word": "本"
            },
            {
                "dep": "aux",
                "head_index": 7,
                "index": 8,
                "lemma": "です",
                "pos": "AUX",
                "tag": "助動詞",
                "word": "でし"
            },
            {
                "dep": "aux",
                "head_index": 7,
                "index": 9,
                "lemma": "た",
                "pos": "AUX",
                "tag": "助動詞",
                "word": "た"
            },
            {
                "dep": "punct",
                "head_index": 7,
                "index": 10,
                "lemma": "。",
                "pos": "PUNCT",
                "tag": "補助記号-句点",
                "word": "。"
            }
        ]
    }
]
```

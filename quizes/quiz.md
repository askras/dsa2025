---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python editable=true slideshow={"slide_type": ""}
import json

from jupyterquiz import display_quiz
```

```python editable=true slideshow={"slide_type": ""}
def quiz(lab_n, questions_num=10):
    with open(f'questions_{str(lab_n).zfill(2)}.json', 'rb') as f:
        questions = json.loads(f.read())
    display_quiz(questions, num=questions_num, shuffle_questions=True, shuffle_answers=True)
```

```python editable=true slideshow={"slide_type": ""}
quiz(1)
```

```python

```

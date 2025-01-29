import re


def replace_using_dict(original_string, replacements) -> str:
    for old, new in replacements.items():
        original_string = original_string.replace(old, new)
    return original_string


def separate_camel_case(s) -> str:
    # Use regex to find positions in the camel case string
    separated = re.sub("([a-z])([A-Z])", r"\1 \2", s)
    return separated


def contains_multiple_entities(question) -> bool:
    keywords = [
        "and",
        "or",
        "as well as",
        "both",
        "along with",
        "together with",
        "in addition to",
        "besides",
        "also",
    ]
    question = question.lower()
    return any(
        f" {keyword} " in question
        or question.startswith(f"{keyword} ")
        or question.endswith(f" {keyword}")
        for keyword in keywords
    )


def fix_query_spacing(query: str) -> str:
    # Add a space after 'select' if it's followed immediately by a variable (e.g., ?x, ?y)
    query = re.sub(r"(select)(\?\w+)", r"\1 \2", query)
    # Add a space before any variable in a predicate-object pair
    query = re.sub(r"(\w+:\w+)(\?\w+)", r"\1 \2", query)
    return query

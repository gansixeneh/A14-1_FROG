import re
from datetime import datetime

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

def legal_entity_label(url):
    parts = url.strip('/').split('/')
    transformed_parts = []
    
    month_mapping = {
        "January": "Januari", "February": "Februari", "March": "Maret", "April": "April", "May": "Mei", "June": "Juni",
        "July": "Juli", "August": "Agustus", "September": "September", "October": "Oktober", "November": "November", "December": "Desember"
    }
    
    for i, part in enumerate(parts):
        if part == "lex2kg":
            transformed_parts = []
            continue
        if part == "uu":
            transformed_parts.append("UU")
        elif part.isdigit() and len(part) <= 2:
            transformed_parts.append(f"no {part}")
        elif part.isdigit() and len(part) == 4 and int(part) >= 1945:
            transformed_parts.append(f"tahun {part}")
        elif part.isdigit() and len(part) == 8:
            try:
                date_obj = datetime.strptime(part, "%Y%m%d")
                formatted_date = date_obj.strftime("%-d %B %Y")
                for eng, indo in month_mapping.items():
                    formatted_date = formatted_date.replace(eng, indo)
                transformed_parts.append(formatted_date)
            except ValueError:
                transformed_parts.append(part)
        elif part.isdigit():
            num = str(int(part))
            transformed_parts.append(num)
        else:
            transformed_parts.append(separate_camel_case(part).lower())
    
    return ' '.join(transformed_parts)

def legal_property_label(x):
    return separate_camel_case(x.split(":")[-1]).lower()
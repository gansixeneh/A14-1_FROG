import re

def get_next_variable(curr):
    if curr == "w":
       return "y"

    last_char = curr[-1]

    if last_char == "z":
        if all(c == "z" for c in curr):
            return "a" * (len(curr) + 1)
        return curr[:-1] + chr(ord(curr[-1]) + 1)
    else:
        return curr[:-1] + chr(ord(last_char) + 1)

def replace_prefix_wikidata(iri):
    iri = iri.replace("http://www.wikidata.org/prop/direct/", "wdt:")
    iri = iri.replace("http://www.wikidata.org/entity/", "wd:")
    return iri

def is_wikidata_entity_iri(iri):
    # Define the regex pattern for a valid Wikidata entity IRI
    pattern = r"^http:\/\/www\.wikidata\.org\/entity\/Q[0-9]+$"

    # Use re.match to check if the IRI matches the pattern
    if re.match(pattern, iri):
        return True
    return False

def replace_prefix_dbpedia(iri):
    iri = iri.replace("http://dbpedia.org/resource/Category:", "dbc:")
    iri = iri.replace("http://dbpedia.org/datatype/", "dbd:")
    iri = iri.replace("http://dbpedia.org/ontology/", "dbo:")
    iri = iri.replace("http://dbpedia.org/resource/", "dbr:")
    iri = iri.replace("http://dbpedia.org/property/", "dbp:")
    return iri

def is_dbpedia_entity_iri(iri):
    tmp = replace_prefix_dbpedia(iri)
    return tmp != iri

def concat_str_with_datatype(literal):
    datetime_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$"
    if bool(re.fullmatch(datetime_pattern, literal)):
        return f'"{literal}"^^xsd:dateTime'
    else:
        return f'"{literal}"'

def concat_str_with_datatype_rdflib(literal):
    if type(literal) is int:
        return literal
    return f'{literal}'
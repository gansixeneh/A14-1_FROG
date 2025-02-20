import json

WIKIDATA_DBPEDIA_EXTRACT_ENTITY_FEW_SHOTS = [
    {
        "input": "how much is 1 tablespoon of water?",
        "output": {"names": ["Tablespoon"]},
    },
    {
        "input": "how are glacier caves formed?",
        "output": {"names": ["Glacier cave"]},
    },
    {
        "input": "how much are the harry potter movies worth?",
        "output": {"names": ["Harry Potter"]},
    },
    {
        "input": "how big is auburndale florida?",
        "output": {"names": ["Auburndale", "Florida"]},
    },
    {
        "input": "what country is jakarta in?",
        "output": {"names": ["Jakarta"]},
    },
    {
        "input": "how deep can be drill for deep underwater?",
        "output": {"names": ["Deepwater drilling"]},
    },
    {
        "input": "how many continents there are in indonesia?",
        "output": {"names": ["Continent", "Indonesia"]},
    },
    {
        "input": "Largest cities of the world",
        "output": {"names": ["City"]},
    },
    {
        "input": "Popular surnames among fictional characters",
        "output": {"names": ["Fictional character"]},
    },
    {
        "input": "WWII battle durations",
        "output": {"names": ["WWII", "battle"]},
    },
    {
        "input": "How many inhabitants does the largest city in Canada have?",
        "output": {"names": ["Canada"]},
    },
    {
        "input": "What is the population of Cairo?",
        "output": {"names": ["Cairo"]},
    },
    {
        "input": "How high is the Yokohama Marine Tower?",
        "output": {"names": ["Yokohama Marine Tower"]},
    },
    {
        "input": "Which programming languages were influenced by Perl?",
        "output": {"names": ["Perl"]},
    },
    {
        "input": "Give me all Australian nonprofit organizations.",
        "output": {"names": ["Australia", "Nonprofit organization"]},
    },
    {
        "input": "Which ingredients do I need for carrot cake?",
        "output": {"names": ["Carrot cake"]},
    },
    {
        "input": "How tall is Claudia Schiffer?",
        "output": {"names": ["Claudia Schiffer"]},
    },
    {
        "input": "In which films did Julia Roberts as well as Richard Gere play?",
        "output": {"names": ["Julia Roberts", "Richard Gere"]},
    },
    {
        "input": "Who produced the most films?",
        "output": {"names": ["Film"]},
    },
    {
        "input": "Show me all basketball players that are higher than 2 meters.",
        "output": {"names": ["Basketball player"]},
    },
    {
        "input": "How many films did Leonardo DiCaprio star in?",
        "output": {"names": ["Leonardo DiCaprio"]},
    },
    {
        "input": "Give me all companies in the advertising industry.",
        "output": {"names": ["Company", "Advertising"]},
    },
    {
        "input": "How many movies did Park Chan-wook direct?",
        "output": {"names": ["Park Chan-wook"]},
    },
    {
        "input": "Who wrote the Game of Thrones theme?",
        "output": {"names": ["Game of Thrones"]},
    },
]

ENTERPRISE_EXTRACT_ENTITY_FEW_SHOTS = [
    {
        "input": "What faculty mandatory course that have 'Test' and 'Task' as evaluation method?",
        "output": {"names": ["Faculty Mandatory Course", "Test", "Task"]},
    },
    {
        "input": "What courses have prerequisites that falls under the category of Faculty Mandatory Course?",
        "output": {"names": ["Faculty Mandatory Course"]},
    },
    {
        "input": "How many research groups does the 'Computer Science Special Topics' have?",
        "output": {"names": ["Computer Science Special Topics"]},
    },
    {
        "input": "What evaluation methods does Software engineering have?",
        "output": {"names": ["Software Engineering"]},
    },
    {
        "input": "What evaluation methods does Deep Learning have?",
        "output": {"names": ["Deep Learning"]},
    },
    {
        "input": "How many courses have 'Programming projects and demos' as the evaluation method?",
        "output": {"names": ["Programming Projects and Demos"]},
    },
    {
        "input": "What courses are included in the research group of Reliable Software Engineering?",
        "output": {"names": ["Reliable Software Engineering"]},
    },
    {
        "input": "What courses have 'Introduction to Artificial Intelligence and Data Science' as a prerequisite course?",
        "output": {
            "names": ["Introduction to Artificial Intelligence and Data Science"]
        },
    },
]


INTENT_CLASSIFICATION_FEW_SHOTS = [
    {
        "input": "How many species of birds?",
        "output": {"is_global": True},
    },
    {
        "input": "Who is the current president of Indonesia?",
        "output": {"is_global": False},
    },
    {
        "input": "What is the tallest building?",
        "output": {"is_global": True},
    },
    {
        "input": "Give me the list of films directed by Christopher Nolan.",
        "output": {"is_global": False},
    },
]


GENERATE_RELATED_PROPERTIES_FEW_SHOTS = [
    {
        "input": "How many inhabitants does the largest city in Canada have?",
        "output": {"properties": ["population", "populationTotal", "governedAs"]},
    },
    {
        "input": "What is the population of Cairo?",
        "output": {"properties": ["population", "populationTotal", "populationAsOf"]},
    },
    {
        "input": "How high is the Yokohama Marine Tower?",
        "output": {"properties": ["height", "elevation", "structure"]},
    },
    {
        "input": "Which programming languages were influenced by Perl?",
        "output": {"properties": ["influencedBy", "influenced", "programmingLanguage"]},
    },
    {
        "input": "Give me all Australian nonprofit organizations.",
        "output": {"properties": ["foundation", "charity", "organization"]},
    },
    {
        "input": "Which ingredients do I need for carrot cake?",
        "output": {"properties": ["ingredient", "recipeIngredient", "foodIngredient"]},
    },
    {
        "input": "How tall is Claudia Schiffer?",
        "output": {"properties": ["height", "elevation"]},
    },
    {
        "input": "In which films did Julia Roberts as well as Richard Gere play?",
        "output": {"properties": ["starring", "film", "actor"]},
    },
    {
        "input": "Who produced the most films?",
        "output": {"properties": ["producer", "producedBy", "film"]},
    },
    {
        "input": "Show me all basketball players that are higher than 2 meters.",
        "output": {"properties": ["height", "athlete", "basketballPlayer"]},
    },
    {
        "input": "How many films did Leonardo DiCaprio star in?",
        "output": {"properties": ["starring", "film", "actor"]},
    },
    {
        "input": "Give me all companies in the advertising industry.",
        "output": {"properties": ["company", "industry"]},
    },
    {
        "input": "How many movies did Park Chan-wook direct?",
        "output": {"properties": ["director"]},
    },
    {
        "input": "Who wrote the Game of Thrones theme?",
        "output": {"properties": ["composer", "music", "composition"]},
    },
]

INTENT_CLASSIFICATION_FEW_SHOTS = [
    {
        "input": "How many species of birds?",
        "output": {"is_global": True},
    },
    {
        "input": "Who is the current president of Indonesia?",
        "output": {"is_global": False},
    },
    {
        "input": "What is the tallest building?",
        "output": {"is_global": True},
    },
    {
        "input": "Give me the list of films directed by Christopher Nolan.",
        "output": {"is_global": False},
    },
]


GENERATE_RELATED_PROPERTIES_FEW_SHOTS = [
    {
        "input": "How many inhabitants does the largest city in Canada have?",
        "output": {"properties": ["population", "populationTotal", "governedAs"]},
    },
    {
        "input": "What is the population of Cairo?",
        "output": {"properties": ["population", "populationTotal", "populationAsOf"]},
    },
    {
        "input": "How high is the Yokohama Marine Tower?",
        "output": {"properties": ["height", "elevation", "structure"]},
    },
    {
        "input": "Which programming languages were influenced by Perl?",
        "output": {"properties": ["influencedBy", "influenced", "programmingLanguage"]},
    },
    {
        "input": "Give me all Australian nonprofit organizations.",
        "output": {"properties": ["foundation", "charity", "organization"]},
    },
    {
        "input": "Which ingredients do I need for carrot cake?",
        "output": {"properties": ["ingredient", "recipeIngredient", "foodIngredient"]},
    },
    {
        "input": "How tall is Claudia Schiffer?",
        "output": {"properties": ["height", "elevation"]},
    },
    {
        "input": "In which films did Julia Roberts as well as Richard Gere play?",
        "output": {"properties": ["starring", "film", "actor"]},
    },
    {
        "input": "Who produced the most films?",
        "output": {"properties": ["producer", "producedBy", "film"]},
    },
    {
        "input": "Show me all basketball players that are higher than 2 meters.",
        "output": {"properties": ["height", "athlete", "basketballPlayer"]},
    },
    {
        "input": "How many films did Leonardo DiCaprio star in?",
        "output": {"properties": ["starring", "film", "actor"]},
    },
    {
        "input": "Give me all companies in the advertising industry.",
        "output": {"properties": ["company", "industry"]},
    },
    {
        "input": "How many movies did Park Chan-wook direct?",
        "output": {"properties": ["director"]},
    },
    {
        "input": "Who wrote the Game of Thrones theme?",
        "output": {"properties": ["composer", "music", "composition"]},
    },
]


DBPEDIA_GENERATE_SPARQL_FEW_SHOTS = [
    {
        "input": """How many inhabitants does the largest city in Canada have?""",
        "output": {
            "thoughts": [
                "1. The question asks for the population of the largest city in Canada.",
                "2. To retrieve this information from DBpedia, identify the correct URI for 'Canada' and the relevant properties associated with cities and population.",
                "3. From the context, 'Canada' has multiple possible URIs, with 'dbr:Canada' being the correct general URI.",
                "4. The term 'largest city' suggests we should find the entity linked to Canada that represents its largest city, which requires identifying the property that connects 'Canada' to its largest city.",
                "5. From the list of ontology candidates, 'dbo:largestCity' is the most relevant object property for retrieving the largest city of a place, with both the domain and range indicating populated places.",
                "6. After obtaining the largest city, we need to retrieve its population. The 'dbo:populationTotal' data property provides the total population for a city and is appropriate for this purpose.",
                "7. Formulate the query to first find the largest city of Canada using 'dbo:largestCity' and then retrieve its population using 'dbo:populationTotal'.",
            ],
            "sparql": "SELECT DISTINCT ?num WHERE { dbr:Canada dbo:largestCity ?city . ?city dbo:populationTotal ?num }",
        },
    },
    {
        "input": """What is the population of Cairo?""",
        "output": {
            "thoughts": [
                "1. The question seeks the population of 'Cairo'.",
                "2. From the context, there are multiple resources labeled 'Cairo', but the correct URI for Cairo, Egypt, is 'dbr:Cairo'.",
                "3. To find the population of Cairo, identify a relevant data property that retrieves population information.",
                "4. In the ontology candidates, 'dbo:populationTotal' is a suitable data property to retrieve the total population of a populated place.",
                "5. Formulate the query to select the population of 'dbr:Cairo' using the 'dbo:populationTotal' property.",
            ],
            "sparql": "SELECT ?pop WHERE { dbr:Cairo dbo:populationTotal ?pop }",
        },
    },
    {
        "input": """How high is the Yokohama Marine Tower?""",
        "output": {
            "thoughts": [
                "1. The question is asking for the height of 'Yokohama Marine Tower'.",
                "2. The context provides a single URI for 'Yokohama Marine Tower', specifically 'dbr:Yokohama_Marine_Tower', which can be used directly in the query.",
                "3. To retrieve the height, identify a data property related to the height or elevation of a structure.",
                "4. In the ontology, 'dbo:height' is a relevant data property that does not have a specific domain or range but matches the information requested.",
                "5. Formulate the query to select the height of 'dbr:Yokohama_Marine_Tower' using the 'dbo:height' property.",
            ],
            "sparql": "SELECT DISTINCT ?num WHERE { dbr:Yokohama_Marine_Tower dbo:height ?num }",
        },
    },
    {
        "input": """Which programming languages were influenced by Perl?""",
        "output": {
            "thoughts": [
                "1. The question seeks to identify programming languages influenced by 'Perl'.",
                "2. Multiple resources were retrieved, but the resource 'dbr:Perl' is the relevant one here as it specifically refers to the programming language.",
                "3. The ontology provides 'dbo:influenced' and 'dbo:influencedBy', both of which relate to influence relationships that could identify languages influenced by Perl.",
                "4. Since the question does not specify a time period or further context, a UNION clause can be used to cover both cases—where Perl influenced other languages and where it is marked as having influenced a language.",
                "5. The query should retrieve distinct URIs of programming languages influenced by Perl by using both 'dbo:influencedBy' and 'dbo:influenced' properties in a UNION pattern.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { { ?uri dbo:influencedBy dbr:Perl } UNION { dbr:Perl dbo:influenced ?uri } }",
        },
    },
    {
        "input": """Give me all Australian nonprofit organizations.""",
        "output": {
            "thoughts": [
                "1. The question asks for nonprofit organizations located in Australia.",
                "2. Multiple URIs for 'Australia' were retrieved, but 'dbr:Australia' best represents the country as a whole.",
                "3. The relevant resources and ontology include 'dbr:Nonprofit_organization' and the class 'dbo:Non-ProfitOrganisation', which indicates nonprofit entities.",
                "4. The properties 'dbo:locationCountry' and 'dbo:location' are useful, with 'dbo:locationCountry' directly linking organizations to their country and 'dbo:location' providing a location reference that can include countries.",
                "5. A UNION pattern can cover both cases to ensure all nonprofits in Australia are captured, either by directly using 'dbo:locationCountry' or by using 'dbo:location' with an additional check for country.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri dbo:type dbr:Nonprofit_organization . { ?uri dbo:locationCountry dbr:Australia } UNION { ?uri dbo:location ?x . ?x dbo:country dbr:Australia } }",
        },
    },
    {
        "input": """Which ingredients do I need for carrot cake?""",
        "output": {
            "thoughts": [
                "1. The question asks for the ingredients needed to make carrot cake.",
                "2. The retrieved resources show 'dbr:Carrot_cake' as the primary URI for 'Carrot cake'.",
                "3. The ontology data includes 'dbo:ingredient' as a relevant object property, which can link food items to their ingredients.",
                "4. Since there is no domain and range for 'dbo:ingredient,' it's likely general enough to use directly in the query.",
                "5. To answer the question, query all ?uri values linked to 'dbr:Carrot_cake' via 'dbo:ingredient'.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { dbr:Carrot_cake dbo:ingredient ?uri }",
        },
    },
    {
        "input": """How tall is Claudia Schiffer?""",
        "output": {
            "thoughts": [
                "1. The question is asking for Claudia Schiffer's height.",
                "2. From the retrieved resources, 'dbr:Claudia_Schiffer' is identified as the URI representing Claudia Schiffer.",
                "3. The ontology data includes 'dbo:height' as a relevant data property, which is commonly used to indicate a person's height.",
                "4. Although there is no domain and range for 'dbo:height,' it should still be appropriate to retrieve the height data directly for the given URI.",
                "5. To answer the question, query the ?height value associated with 'dbr:Claudia_Schiffer' via 'dbo:height'.",
            ],
            "sparql": "SELECT DISTINCT ?height WHERE { dbr:Claudia_Schiffer dbo:height ?height }",
        },
    },
    {
        "input": """In which films did Julia Roberts as well as Richard Gere play?""",
        "output": {
            "thoughts": [
                "1. The question asks for films in which both Julia Roberts and Richard Gere acted together.",
                "2. From the retrieved resources, 'dbr:Julia_Roberts' and 'dbr:Richard_Gere' are the URIs representing Julia Roberts and Richard Gere, respectively.",
                "3. The ontology contains 'dbo:starring' as an object property with the domain 'dbo:Work' and the range 'dbo:Actor,' which is suitable for identifying films with specific actors.",
                "4. Since we're looking for shared appearances, we should query for films (dbo:Film) where both actors are linked through 'dbo:starring'.",
                "5. Formulate the query to select unique film URIs that have both 'dbr:Julia_Roberts' and 'dbr:Richard_Gere' as values for 'dbo:starring'.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri rdf:type dbo:Film ; dbo:starring dbr:Julia_Roberts ; dbo:starring dbr:Richard_Gere }",
        },
    },
    {
        "input": """Who produced the most films?""",
        "output": {
            "thoughts": [
                "1. The question asks for the entity that has produced the most films, suggesting a need to count the number of films linked to each producer.",
                "2. From the resources and ontology, the class 'dbo:Film' represents films, and the property 'dbo:producer' links films to their producers.",
                "3. The query should retrieve entities linked via 'dbo:producer' to instances of 'dbo:Film'.",
                "4. We need to count the films associated with each producer, order by this count in descending order, and select the top result.",
                "5. Formulate the query to select distinct producer URIs, counting the films they produced, and order by the count in descending order to find the producer with the most films.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?film rdf:type dbo:Film . ?film dbo:producer ?uri . } ORDER BY DESC(COUNT(?film)) OFFSET 0 LIMIT 1",
        },
    },
    {
        "input": """Show me all basketball players that are higher than 2 meters.""",
        "output": {
            "thoughts": [
                "1. The question specifies basketball players who are taller than 2 meters, so we need entities of type dbo:BasketballPlayer with a height greater than 2 meters.",
                "2. The ontology provides dbo:BasketballPlayer as the appropriate class for basketball players and dbo:height as the property representing height.",
                "3. The query should use a filter to select only players with heights exceeding 2.0 meters.",
                "4. Structure the query to retrieve unique URIs for basketball players meeting this height criterion.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri a dbo:BasketballPlayer ; dbo:height ?n FILTER ( ?n > 2.0 ) }",
        },
    },
    {
        "input": """How many films did Leonardo DiCaprio star in?""",
        "output": {
            "thoughts": [
                "1. The question requires counting the number of films Leonardo DiCaprio starred in.",
                "2. We need to retrieve entities of type dbo:Film, where Leonardo DiCaprio is listed as the star.",
                "3. The dbo:starring property links films to actors, so we can use this property with dbr:Leonardo_DiCaprio as the object.",
                "4. To get the count, we use COUNT(DISTINCT ?uri) to ensure each film is counted only once, and return the result as ?c.",
            ],
            "sparql": "SELECT (COUNT(DISTINCT ?uri) AS ?c) WHERE { ?uri a dbo:Film ; dbo:starring dbr:Leonardo_DiCaprio }",
        },
    },
    {
        "input": """Give me all companies in the advertising industry.""",
        "output": {
            "thoughts": [
                "1. The question asks for companies in the advertising industry.",
                "2. We can identify companies using the dbo:Company class.",
                "3. The dbo:industry property links a company to its industry, and dbr:Advertising can represent the advertising industry.",
                "4. To ensure we capture relevant companies even if their industry isn't explicitly 'Advertising,' we add a regex filter to match industries with 'advertising' in the label.",
                "5. The query structure includes both direct matches with dbr:Advertising and regex matches to ensure broader coverage.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri a dbo:Company { ?uri dbo:industry dbr:Advertising } UNION { ?uri dbo:industry ?industry FILTER regex(?industry, 'advertising', 'i') } }",
        },
    },
    {
        "input": """How many movies did Park Chan-wook direct?""",
        "output": {
            "thoughts": [
                "1. The question asks for the number of movies directed by Park Chan-wook.",
                "2. Park Chan-wook is represented by the URI dbr:Park_Chan-wook.",
                "3. The dbo:director property associates a film with its director.",
                "4. We need to count the unique films where Park Chan-wook is the director, using the dbo:Film class as the target entity.",
            ],
            "sparql": "SELECT COUNT(DISTINCT ?uri AS ?uri) WHERE { ?uri dbo:director dbr:Park_Chan-wook . }",
        },
    },
    {
        "input": """Who wrote the Game of Thrones theme?""",
        "output": {
            "thoughts": [
                "1. The question asks for the composer of the Game of Thrones theme.",
                "2. The resource for Game of Thrones is identified by the URI 'dbr:Game_of_Thrones'.",
                "3. The relevant property to identify the composer of a theme or soundtrack is 'dbo:composer', which links a work with its creator or composer.",
                "4. The query should retrieve the URI of the composer associated with the Game of Thrones series.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { dbr:Game_of_Thrones dbo:composer ?uri }",
        },
    },
]


WIKIDATA_GENERATE_SPARQL_FEW_SHOTS = [
    {
        "input": """How many inhabitants does the largest city in Canada have?""",
        "output": {
            "thoughts": [
                "1. The question asks for the population of the largest city in Canada.",
                "2. To retrieve this information from Wikidata, identify the correct URI for 'Canada' and the relevant properties associated with cities and population.",
                "3. From the provided URIs, 'wd:Q16' is the correct identifier for the country 'Canada' in Wikidata.",
                "4. The term 'largest city' requires identifying Canadian cities and sorting them by population to determine the largest.",
                "5. Based on the ontology, the 'wdt:P17' property links entities to their respective countries, which helps identify cities in Canada.",
                "6. The 'wdt:P31 wd:Q515' construct allows filtering for entities that are instances of or subclasses of 'city' (Q515).",
                "7. The 'wdt:P1082' property specifies the population of cities, which is necessary to sort and retrieve the largest city by population.",
                "8. Formulate a SPARQL query to find all cities in Canada, retrieve their populations using 'wdt:P1082', and sort the results in descending order to determine the largest city by population.",
            ],
            "sparql": "SELECT DISTINCT ?val WHERE { ?uri wdt:P17 wd:Q16 ; wdt:P31 wd:Q515 ; wdt:P1082 ?val } ORDER BY DESC(?val) LIMIT 1",
        },
    },
    {
        "input": """What is the population of Cairo?""",
        "output": {
            "thoughts": [
                "1. The question seeks the population of 'Cairo'.",
                "2. From the retrieved resources, the correct URI for Cairo, the capital city of Egypt, is 'wd:Q85' in Wikidata.",
                "3. To retrieve the population, we need to identify a relevant property that provides population data.",
                "4. From the retrieved ontology, the property 'wdt:P1082' represents the total population of an entity and is suitable for this query.",
                "5. Formulate a SPARQL query to retrieve the population of 'wd:Q85' using the 'wdt:P1082' property.",
            ],
            "sparql": "SELECT DISTINCT ?val WHERE { wd:Q85 wdt:P1082 ?val . }",
        },
    },
    {
        "input": """How high is the Yokohama Marine Tower?""",
        "output": {
            "thoughts": [
                "1. The question seeks the height of the 'Yokohama Marine Tower'.",
                "2. From the retrieved resources, the correct URI for 'Yokohama Marine Tower' is 'wd:Q1207989' in Wikidata.",
                "3. To retrieve the height, a property representing height information is required.",
                "4. In the retrieved ontology, the property 'wdt:P2048' represents the height of a structure and is appropriate for this query.",
                "5. Formulate a SPARQL query to retrieve the height of 'wd:Q1207989' using the 'wdt:P2048' property.",
            ],
            "sparql": "SELECT DISTINCT ?num WHERE { wd:Q1207989 wdt:P2048 ?num . }",
        },
    },
    {
        "input": """Which programming languages were influenced by Perl?""",
        "output": {
            "thoughts": [
                "1. The question seeks to identify programming languages influenced by 'Perl'.",
                "2. From the retrieved resources, the correct URI for 'Perl' as a programming language is 'wd:Q42478'.",
                "3. To find programming languages influenced by Perl, a property representing influence relationships is needed.",
                "4. In the retrieved ontology, the property 'wdt:P737' represents the influence relationship, where the subject is influenced by the object.",
                "5. A SPARQL query can be formulated to retrieve entities classified as programming languages (wd:Q9143) that are influenced by 'wd:Q42478' using the 'wdt:P737' property.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri wdt:P31 wd:Q9143 ; wdt:P737 wd:Q42478 . }",
        },
    },
    {
        "input": """Give me all Australian nonprofit organizations.""",
        "output": {
            "thoughts": [
                "1. The question seeks all nonprofit organizations located in Australia.",
                "2. From the retrieved resources, the correct URI for 'Australia' as a country is 'wd:Q408'.",
                "3. For 'nonprofit organization', the correct URI is 'wd:Q163740', representing organizations operated for collective benefit.",
                "4. To find Australian nonprofit organizations, entities classified as 'nonprofit organizations' (wd:Q163740) should be retrieved and filtered based on their location being in Australia (wd:Q408).",
                "5. The properties 'wdt:P31' (instance of), 'wdt:P17' (country), and 'wdt:P159' (headquarters location) are relevant for identifying nonprofit organizations in Australia.",
                "6. A SPARQL query can be formulated to retrieve all entities that are instances of 'nonprofit organization' (wd:Q163740) and are either located in Australia (wdt:P17 wd:Q408) or have their headquarters there (wdt:P159 wd:Q408).",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri wdt:P31 wd:Q163740 . { ?uri wdt:P159|wdt:P17 wd:Q408 . } UNION { ?uri wdt:P159|wdt:P17 ?city . ?city wdt:P159 wd:Q408 } }",
        },
    },
    {
        "input": """Which ingredients do I need for carrot cake?""",
        "output": {
            "thoughts": [
                "1. The question seeks the ingredients needed to make carrot cake.",
                "2. From the retrieved resources, the correct URI for 'Carrot cake' as a sweet dish is 'wd:Q656071'.",
                "3. To identify the ingredients, a property that specifies components or ingredients is required.",
                "4. In the retrieved ontology, the property 'wdt:P527' represents components or parts of an entity, making it suitable for retrieving ingredients.",
                "5. A SPARQL query can be formulated to retrieve all entities linked to 'wd:Q656071' through the 'wdt:P527' property, representing the ingredients of carrot cake.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { wd:Q656071 wdt:P527 ?uri . }",
        },
    },
    {
        "input": """How tall is Claudia Schiffer?""",
        "output": {
            "thoughts": [
                "1. The question seeks the height of Claudia Schiffer.",
                "2. The retrieved resources do not include Claudia Schiffer explicitly, but her Wikidata URI can be identified as 'wd:Q76717' based on external context.",
                "3. To find her height, a property representing physical height is required.",
                "4. In the retrieved ontology, the property 'wdt:P2048' represents height and is suitable for retrieving this information.",
                "5. A SPARQL query can be formulated to retrieve the height value for 'wd:Q76717' using the 'wdt:P2048' property.",
            ],
            "sparql": "SELECT DISTINCT ?val WHERE { wd:Q76717 wdt:P2048 ?val . }",
        },
    },
    {
        "input": """In which films did Julia Roberts as well as Richard Gere play?""",
        "output": {
            "thoughts": [
                "1. The question seeks films in which both Julia Roberts and Richard Gere acted.",
                "2. From the retrieved resources, 'wd:Q40523' is the correct URI for Julia Roberts, and 'wd:Q48410' is the correct URI for Richard Gere.",
                "3. To identify shared films, entities classified as 'films' (wd:Q11424) must be retrieved and filtered based on the two actors being part of the cast.",
                "4. The property 'wdt:P161' (cast member) is relevant for linking actors to films.",
                "5. A SPARQL query can be formulated to retrieve all film entities where both 'wd:Q40523' (Julia Roberts) and 'wd:Q48410' (Richard Gere) appear as cast members using the 'wdt:P161' property.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri wdt:P31 wd:Q11424 . ?uri wdt:P161 wd:Q48410 . ?uri wdt:P161 wd:Q40523 . }",
        },
    },
    {
        "input": """Who produced the most films?""",
        "output": {
            "thoughts": [
                "1. The question asks for films in which both Julia Roberts and Richard Gere acted together.",
                "2. From the retrieved resources, 'wd:Q40523' and 'wd:Q48410' are the Wikidata URIs representing Julia Roberts and Richard Gere, respectively.",
                "3. The ontology contains 'P161' as a property indicating 'cast member,' which is suitable for identifying films with specific actors.",
                "4. Since we're looking for shared appearances, we need to query for films (instances of Q11424, which represents 'film') where both actors are listed as values for 'P161' (cast member).",
                "5. Formulate the query to select distinct film URIs that have both 'wd:Q40523' (Julia Roberts) and 'wd:Q48410' (Richard Gere) as values for the 'P161' property.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?film wdt:P31 wd:Q11424 . ?film wdt:P162 ?uri . } GROUP BY ?uri ORDER BY DESC(COUNT(?film)) LIMIT 1",
        },
    },
    {
        "input": """Show me all basketball players that are higher than 2 meters.""",
        "output": {
            "thoughts": [
                "1. The question asks for basketball players taller than 2 meters, so we need to identify individuals of the relevant type and with height data available.",
                "2. From the retrieved resources, basketball players can be represented by the entity class 'wd:Q3665646' (basketball player).",
                "3. The ontology provides 'P2048' as the property for height, which can be used to determine the physical height of individuals.",
                "4. A filter must be applied to retrieve only players whose height exceeds 200 centimeters (2 meters).",
                "5. Formulate the query to select distinct basketball player URIs where the 'P2048' value is greater than 200.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri wdt:P106 wd:Q3665646 . ?uri wdt:P2048 ?height .  FILTER(?height > 200)}",
        },
    },
    {
        "input": """How many films did Leonardo DiCaprio star in?""",
        "output": {
            "thoughts": [
                "1. The question asks for the total number of films Leonardo DiCaprio has starred in.",
                "2. Leonardo DiCaprio is represented by the Wikidata URI 'wd:Q38111'.",
                "3. Films are identified as instances of 'wd:Q11424' (film), and 'P161' (cast member) links films to their actors.",
                "4. To count the films Leonardo DiCaprio has starred in, we must query for distinct film URIs where he is listed as a value for the 'P161' property.",
                "5. Use the COUNT(DISTINCT ?uri) function in the query to count the number of unique films and return the result as ?c.",
            ],
            "sparql": "SELECT (COUNT(DISTINCT ?uri) AS ?c) WHERE { ?uri wdt:P31 wd:Q11424 ; wdt:P161 wd:Q38111 . }",
        },
    },
    {
        "input": """Give me all companies in the advertising industry.""",
        "output": {
            "thoughts": [
                "1. The question seeks companies that operate in the advertising industry.",
                "2. Companies can be represented by the Wikidata class 'wd:Q783794' (company).",
                "3. The property 'P452' (industry) links companies to the industries they are involved in.",
                "4. The advertising industry can be represented by the entity 'wd:Q37038' (advertising).",
                "5. Formulate the query to retrieve unique URIs for companies ('wd:Q783794') where the 'P452' property value matches 'wd:Q37038' (advertising).",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { ?uri wdt:P31 wd:Q4830453 ; wdt:P452 wd:Q39809 . }",
        },
    },
    {
        "input": """How many movies did Park Chan-wook direct?""",
        "output": {
            "thoughts": [
                "1. The question asks for the total number of movies directed by Park Chan-wook.",
                "2. Park Chan-wook is represented by the Wikidata URI 'wd:Q315484'.",
                "3. The property 'P57' (director) links films to their directors, making it appropriate for this query.",
                "4. The goal is to count distinct film entities ('wd:Q11424', representing films) where Park Chan-wook is listed as the director using 'P57'.",
                "5. Use the COUNT(DISTINCT ?uri) function to determine the number of unique films directed by Park Chan-wook and return the result as ?count.",
            ],
            "sparql": "SELECT (COUNT(DISTINCT ?uri) as ?count) WHERE {  ?uri wdt:P57 wd:Q315484 . }",
        },
    },
    {
        "input": """Who wrote the Game of Thrones theme?""",
        "output": {
            "thoughts": [
                "1. The question asks for the composer of the Game of Thrones theme.",
                "2. The specific entity representing the 'Game of Thrones Theme' is identified by the URI 'wd:Q27813929'.",
                "3. The relevant property to find the composer is 'P86' (composer), which links musical works to their composers.",
                "4. The query should retrieve the URI of the composer associated with the 'Game of Thrones Theme' using the property 'P86'.",
            ],
            "sparql": "SELECT DISTINCT ?uri WHERE { wd:Q23572 wdt:P86 ?uri . }",
        },
    },
]

ENTERPRISE_GENERATE_SPARQL_FEW_SHOTS = [
    {
        "input": """What faculty mandatory course that have 'Test' and 'Task' as evaluation method?""",
        "output": {
            "thoughts": [
                "1. The question asks for faculty mandatory courses that use both 'Test' and 'Task' as evaluation methods.",
                "2. According to the ontology, 'ns1:faculty_mandatory_course' represents the category of faculty mandatory courses.",
                "3. The property 'ns1:has_course_category' links a course to its category (e.g., faculty mandatory course).",
                "4. The property 'ns1:has_evaluation_method' specifies the evaluation methods of a course, where the range is 'ns1:evaluation'.",
                "5. The terms 'Test' and 'Task' appear to correspond to evaluation methods, which can be linked using 'ns1:has_evaluation_method'.",
                "6. To retrieve the required courses, filter for entities that are categorized as 'faculty mandatory courses' and have both 'Test' and 'Task' as evaluation methods.",
                "7. Construct a SPARQL query that first identifies courses with the 'faculty mandatory course' category and then ensures they are linked to both 'Test' and 'Task' evaluation methods.",
            ],
            "sparql": "select ?x { ?x ns1:has_course_category ns1:faculty_mandatory_course . ?x ns1:has_evaluation_method ns1:test . ?x ns1:has_evaluation_method ns1:task . }",
        },
    },
    {
        "input": """What courses have prerequisites that falls under the category of Faculty Mandatory Course?""",
        "output": {
            "thoughts": [
                "1. The question asks for courses that have prerequisites belonging to the 'Faculty Mandatory Course' category.",
                "2. In the ontology, 'ns1:faculty_mandatory_course' is an entity representing this category.",
                "3. The property 'ns1:has_prerequisite_course' links a course to its prerequisite courses.",
                "4. The property 'ns1:has_course_category' links a course to its specific category.",
                "5. To solve this, identify all courses with a prerequisite that is categorized as a 'Faculty Mandatory Course'.",
                "6. Construct a SPARQL query that filters courses with prerequisites that have 'Faculty Mandatory Course' as their category.",
            ],
            "sparql": "select ?x { ?x ns1:has_prerequisite_course ?y . ?y ns1:has_course_category ns1:faculty_mandatory_course . }",
        },
    },
    {
        "input": """How many research groups does the 'Computer Science Special Topics' have?""",
        "output": {
            "thoughts": [
                "1. The question asks for the number of research groups associated with 'Computer Science Special Topics'.",
                "2. The entity 'ns1:computer_science_special_topics' represents the course in question.",
                "3. The property 'ns1:has_research_group' links a course to its associated research groups.",
                "4. To solve this, count all the research group entities linked to 'Computer Science Special Topics'.",
                "5. Construct a SPARQL query using the COUNT function to determine the number of research groups for this course.",
            ],
            "sparql": "select (count(?x) as ?cnt) { ns1:computer_science_special_topics ns1:has_research_group ?x . }",
        },
    },
    {
        "input": """What evaluation methods does Software engineering have?""",
        "output": {
            "thoughts": [
                "1. The question asks for all evaluation methods used in the 'Software Engineering' course.",
                "2. The entity 'ns1:software_engineering' represents the course in question.",
                "3. The property 'ns1:has_evaluation_method' links a course to its evaluation methods.",
                "4. To solve this, retrieve all entities connected to 'Software Engineering' via the 'has_evaluation_method' property.",
                "5. Construct a SPARQL query to list all evaluation methods for the 'Software Engineering' course.",
            ],
            "sparql": "select ?x { ns1:software_engineering ns1:has_evaluation_method ?x . }",
        },
    },
    {
        "input": """What evaluation methods does Deep Learning have?""",
        "output": {
            "thoughts": [
                "1. The question asks for all evaluation methods used in the 'Deep Learning' course.",
                "2. The entity 'ns1:deep_learning' represents the course in question.",
                "3. The property 'ns1:has_evaluation_method' links a course to its evaluation methods.",
                "4. To solve this, retrieve all entities connected to 'Deep Learning' via the 'has_evaluation_method' property.",
                "5. Construct a SPARQL query to list all evaluation methods for the 'Deep Learning' course.",
            ],
            "sparql": "select ?x { ns1:deep_learning ns1:has_evaluation_method ?x . }",
        },
    },
    {
        "input": """How many courses have 'Programming projects and demos' as the evaluation method?""",
        "output": {
            "thoughts": [
                "1. The question asks for the number of courses that use 'Programming projects and demos' as an evaluation method.",
                "2. The entity 'ns1:programming_projects_and_demos' represents the evaluation method in question.",
                "3. The property 'ns1:has_evaluation_method' links a course to its evaluation methods.",
                "4. To solve this, count all courses linked to 'Programming projects and demos' via the 'has_evaluation_method' property.",
                "5. Construct a SPARQL query using the COUNT function to determine the number of such courses.",
            ],
            "sparql": "select (count(?x) as ?cnt) { ?x ns1:has_evaluation_method ns1:programming_projects_and_demos . }",
        },
    },
    {
        "input": """What courses are included in the research group of Reliable Software Engineering?""",
        "output": {
            "thoughts": [
                "1. The question asks for courses that are part of the 'Reliable Software Engineering' research group.",
                "2. The entity 'ns1:reliable_software_engineering' represents the research group in question.",
                "3. The property 'ns1:has_research_group' links a course to its research group.",
                "4. To solve this, retrieve all courses linked to 'Reliable Software Engineering' via the 'has_research_group' property.",
                "5. Construct a SPARQL query to list all courses associated with this research group.",
            ],
            "sparql": "select ?x { ?x ns1:has_research_group ns1:reliable_software_engineering . }",
        },
    },
    {
        "input": """What courses have 'Introduction to Artificial Intelligence and Data Science' as a prerequisite course?""",
        "output": {
            "thoughts": [
                "1. The question asks for courses that have 'Introduction to Artificial Intelligence and Data Science' as a prerequisite.",
                "2. The entity 'ns1:introduction_to_artificial_intelligence_and_data_science' represents the prerequisite course in question.",
                "3. The property 'ns1:has_prerequisite_course' links a course to its prerequisite courses.",
                "4. To solve this, retrieve all courses linked to 'Introduction to Artificial Intelligence and Data Science' via the 'has_prerequisite_course' property.",
                "5. Construct a SPARQL query to list all courses with this prerequisite.",
            ],
            "sparql": "select ?x { ?x ns1:has_prerequisite_course ns1:introduction_to_artificial_intelligence_and_data_science . }",
        },
    },
]
LEGAL_EXTRACT_ENTITY_FEW_SHOTS = [
    # simple 1
    {
        "input": "Apa isi teks dari UU No. 23 Tahun 2006 Pasal 86 Ayat 2 versi 29 Desember 2006?",
        "output": {"names": ["UU tahun 2006 no 23 pasal 86 versi 29 Desember 2006 ayat 2 text"]},
    },
    {
        "input": "Apa saja huruf yang terdapat dalam UU No. 22 Tahun 1997 Pasal 11 Ayat 4 versi 1 September 1997?",
        "output": {"names": ["UU tahun 1997 no 22 pasal 11 versi 1 September 1997 ayat 4 huruf"]},
    },
    {
        "input": "Ada berapa banyak pasal pada UU Nomor 9 Tahun 2020?",
        "output": {"names": ["UU tahun 2020 no 9"]},
    },
    # simple 2
    {
        "input": "Undang-undang apa saja yang merujuk pada UU No. 31 Tahun 2002 Pasal 27 Ayat 1 versi 27 Desember 2002?",
        "output": {"names": ["UU tahun 2002 no 31 pasal 27 versi 27 Desember 2002 ayat 1"]},
    },
    {
        "input": "Undang-undang apa yang menghapus UU No. 28 Tahun 2002 Pasal 16 versi 20 Juli 2011?",
        "output": {"names": ["UU tahun 2002 no 28 pasal 16 versi 20 Juli 2011"]},
    },
    {
        "input": "Berapa jumlah undang-undang yang merujuk ke UU No. 12 Tahun 1992 Pasal 43 Ayat 1 versi 30 April 1992?",
        "output": {"names": ["UU tahun 1992 no 12 pasal 43 versi 30 April 1992 ayat 1"]},
    },
    # complex 1
    {
        "input": "Undang-undang apa saja yang disahkan pada tanggal 26 Oktober 1957 dan disahkan oleh Soekarno?",
        "output": {"names": []},
    },
    # complex 2
    {
        "input": "Undang-undang apa saja yang mengubah undang-undang yang dibuat pada tanggal 2 November 2020?",
        "output": {"names": []},
    }
]

LEGAL_GENERATE_SPARQL_FEW_SHOTS = [
    # simple 1 normal
    { 
        "input": "Apa isi teks dari UU No. 23 Tahun 2006 Pasal 86 Ayat 2 versi 29 Desember 2006?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta isi atau teks dari ayat tertentu dalam undang-undang: 'UU No. 23 Tahun 2006 Pasal 86 Ayat 2 versi 29 Desember 2006'.",
                "2. Dalam ontologi, entitas yang merepresentasikan ayat ini mengikuti struktur 'lex2kg/uu/2006/23/pasal/0086/versi/20061229/ayat/0002/text'.",
                "3. Properti 'lex2kg-o:teks' digunakan untuk menghubungkan suatu ayat dengan teks isinya.",
                "4. Untuk menyelesaikan ini, cari entitas 'lex2kg/uu/2006/23/pasal/0086/versi/20061229/ayat/0002/text' dan ambil isinya melalui properti 'lex2kg-o:teks'.",
                "5. Susun query SPARQL untuk mengambil isi dari 'UU No. 23 Tahun 2006 Pasal 86 Ayat 2 versi 29 Desember 2006'."
            ],
            "sparql": "SELECT ?x WHERE { <https://example.org/lex2kg/uu/2006/23/pasal/0086/versi/20061229/ayat/0002/text> lex2kg-o:teks ?x . }"
        }
    },
    # simple 1 normal
    {
        "input": "Apa saja huruf yang terdapat dalam UU No. 22 Tahun 1997 Pasal 11 Ayat 4 versi 1 September 1997?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta informasi tentang huruf yang terdapat dalam 'UU No. 22 Tahun 1997 Pasal 11 Ayat 4 versi 1 September 1997'.",
                "2. Dalam ontologi, entitas yang merepresentasikan undang-undang ini mengikuti struktur 'lex2kg/uu/1997/22/pasal/0011/versi/19970901/ayat/0004/huruf'.",
                "3. Huruf-huruf dalam pasal ini direpresentasikan sebagai entitas yang memiliki hubungan dengan ayat tertentu melalui properti 'lex2kg-o:huruf'.",
                "4. Untuk menyelesaikan ini, cari semua entitas huruf yang terhubung dengan 'lex2kg/uu/1997/22/pasal/0011/versi/19970901/ayat/0004/huruf' melalui properti 'lex2kg-o:huruf'.",
                "5. Susun query SPARQL untuk mengambil huruf-huruf yang ada dalam 'UU No. 22 Tahun 1997 Pasal 11 Ayat 4 versi 1 September 1997'."
            ],
            "sparql": "select ?huruf { <https://example.org/lex2kg/uu/1997/22/pasal/0011/versi/19970901/ayat/0004/huruf> lex2kg-o:huruf ?huruf . }"
        }
    },
    # simple 1 count
    {
        "input": "Ada berapa banyak pasal pada UU Nomor 9 Tahun 2020?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta jumlah pasal dalam undang-undang 'UU Nomor 9 Tahun 2020'.",
                "2. Dalam ontologi, entitas yang merepresentasikan undang-undang ini mengikuti struktur 'lex2kg/uu/2020/9'.",
                "3. Pasal-pasal dalam undang-undang ini direpresentasikan sebagai entitas yang memiliki hubungan dengan undang-undang melalui properti 'lex2kg-o:pasal'.",
                "4. Untuk menyelesaikan ini, cari semua entitas pasal yang terhubung dengan 'lex2kg/uu/2020/9' melalui properti 'lex2kg-o:pasal'.",
                "5. Susun query SPARQL untuk menghitung jumlah pasal dalam 'UU Nomor 9 Tahun 2020'."
            ],
            "sparql": "select (count(?x) AS ?jumlahPasal) { <https://example.org/lex2kg/uu/2020/9> lex2kg-o:pasal ?x . }"
        }
    },
    # simple 2 normal
    { 
        "input": "Undang-undang apa saja yang merujuk pada UU No. 31 Tahun 2002 Pasal 27 Ayat 1 versi 27 Desember 2002?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta daftar undang-undang yang merujuk pada 'UU No. 31 Tahun 2002 Pasal 27 Ayat 1 versi 27 Desember 2002'.",
                "2. Dalam ontologi, entitas yang merepresentasikan pasal ini mengikuti struktur 'lex2kg/uu/2002/31/pasal/0027/versi/20021227/ayat/0001'.",
                "3. Properti 'lex2kg-o:merujuk' digunakan untuk menunjukkan hubungan referensi dari satu undang-undang ke pasal lain.",
                "4. Untuk menyelesaikan ini, cari semua entitas undang-undang yang memiliki hubungan 'lex2kg-o:merujuk' dengan 'lex2kg/uu/2002/31/pasal/0027/versi/20021227/ayat/0001'.",
                "5. Susun query SPARQL untuk mengambil semua undang-undang yang merujuk ke pasal ini."
            ],
            "sparql": "select ?x { ?x lex2kg-o:merujuk <https://example.org/lex2kg/uu/2002/31/pasal/0027/versi/20021227/ayat/0001> . }"
        }
    },
    # simple 2 normal
    {
        "input": "Undang-undang apa yang menghapus UU No. 28 Tahun 2002 Pasal 16 versi 2 November 2020?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta informasi tentang undang-undang yang menghapus 'UU No. 28 Tahun 2002 Pasal 16 versi 2 November 2020'.",
                "2. Dalam ontologi, entitas yang merepresentasikan pasal ini mengikuti struktur 'lex2kg/uu/2002/28/pasal/0016/versi/20201102'.",
                "3. Properti 'lex2kg-o:menghapus' digunakan untuk menunjukkan hubungan antara undang-undang yang menghapus pasal lain.",
                "4. Untuk menyelesaikan ini, cari semua entitas undang-undang yang memiliki hubungan 'lex2kg-o:menghapus' dengan 'lex2kg/uu/2002/28/pasal/0016/versi/20201102'.",
                "5. Susun query SPARQL untuk mengambil semua undang-undang yang menghapus pasal ini."
            ],
            "sparql": "select ?x { ?x lex2kg-o:menghapus <https://example.org/lex2kg/uu/2002/28/pasal/0016/versi/20201102> . }"
        }
    },
    # simple 2 count
    {
        "input": "Berapa jumlah undang-undang yang merujuk ke UU No. 12 Tahun 1992 Pasal 43 Ayat 1 versi 30 April 1992?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta jumlah undang-undang yang merujuk pada 'UU No. 12 Tahun 1992 Pasal 43 Ayat 1 versi 30 April 1992'.",
                "2. Dalam ontologi, entitas yang merepresentasikan pasal ini mengikuti struktur 'lex2kg/uu/1992/12/pasal/0043/versi/19920430/ayat/0001'.",
                "3. Properti 'lex2kg-o:merujuk' digunakan untuk menunjukkan hubungan antara suatu undang-undang dan pasal yang dirujuknya.",
                "4. Untuk menyelesaikan ini, cari semua entitas undang-undang yang memiliki hubungan 'lex2kg-o:merujuk' dengan 'lex2kg/uu/1992/12/pasal/0043/versi/19920430/ayat/0001'.",
                "5. Susun query SPARQL untuk menghitung jumlah undang-undang yang merujuk pada pasal ini."
            ],
            "sparql": "select (count(?x) as ?cnt) { ?x lex2kg-o:merujuk <https://example.org/lex2kg/uu/1992/12/pasal/0043/versi/19920430/ayat/0001> . }"
        }
    },
    # complex 1
    {
        "input": "Undang-undang apa saja yang disahkan pada tanggal 26 Oktober 1957 dan disahkan oleh Soekarno?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta informasi tentang undang-undang yang disahkan pada tanggal 26 Oktober 1957 dan disahkan oleh SOEKARNO.",
                "2. Tidak ada entitas eksplisit yang bisa diekstrak, tetapi perlu mendeteksi dua literal utama:",
                "   - '26 Oktober 1957' sebagai literal dengan format tanggal '1957-10-26'^^xsd:date.",
                "   - 'SOEKARNO' sebagai literal dalam format semua karakter berupa huruf kapital.",
                "3. Dalam ontologi, properti 'lex2kg-o:disahkanPada' digunakan untuk menunjukkan tanggal pengesahan undang-undang.",
                "4. Properti 'lex2kg-o:disahkanOleh' digunakan untuk menunjukkan siapa yang mengesahkan undang-undang.",
                "5. Untuk menyelesaikan ini, cari semua entitas undang-undang yang memiliki nilai '1957-10-26' pada properti 'lex2kg-o:disahkanPada' dan nilai 'SOEKARNO' pada properti 'lex2kg-o:disahkanOleh'.",
                "6. Susun query SPARQL untuk mendapatkan hasil yang sesuai."
            ],
            "sparql": "select ?x { ?x lex2kg-o:disahkanPada '1957-10-26'^^xsd:date . ?x lex2kg-o:disahkanOleh 'SOEKARNO' . }"
        },
    },
    # complex 2
    {
        "input": "Undang-undang apa saja yang mengubah undang-undang yang dibuat pada tanggal 20 Juli 2011?",
        "output": {
            "thoughts": [
                "1. Pertanyaan ini meminta informasi tentang undang-undang yang mengubah undang-undang lain yang dibuat pada 20 Juli 2011.",
                "2. Tidak ada entitas spesifik yang bisa diekstrak, tetapi perlu mendeteksi literal utama:",
                "   - '20 Juli 2011' sebagai literal dengan format tanggal '2011-07-20'^^xsd:date.",
                "3. Dalam ontologi, properti 'lex2kg-o:tanggal' digunakan untuk menunjukkan tanggal pembuatan undang-undang.",
                "4. Properti 'lex2kg-o:mengubah' digunakan untuk menunjukkan hubungan antara undang-undang yang mengubah pasal lain.",
                "5. Untuk menyelesaikan ini, cari semua entitas undang-undang yang memiliki hubungan 'lex2kg-o:mengubah' dengan undang-undang yang dibuat pada tanggal '2011-07-20'.",
                "6. Susun query SPARQL untuk mendapatkan hasil yang sesuai."
            ],
            "sparql": "select ?x { ?x lex2kg-o:mengubah ?law . ?law lex2kg-o:tanggal '2011-07-20'^^xsd:date . }"
        },
    }
]
for fs in [
    WIKIDATA_DBPEDIA_EXTRACT_ENTITY_FEW_SHOTS,
    ENTERPRISE_EXTRACT_ENTITY_FEW_SHOTS,
    INTENT_CLASSIFICATION_FEW_SHOTS,
    GENERATE_RELATED_PROPERTIES_FEW_SHOTS,
    DBPEDIA_GENERATE_SPARQL_FEW_SHOTS,
    WIKIDATA_GENERATE_SPARQL_FEW_SHOTS,
    ENTERPRISE_GENERATE_SPARQL_FEW_SHOTS,
    LEGAL_EXTRACT_ENTITY_FEW_SHOTS,
    LEGAL_GENERATE_SPARQL_FEW_SHOTS,
]:
    for f in fs:
        f["output"] = json.dumps(f["output"], indent=4)

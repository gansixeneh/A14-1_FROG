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

LEGAL_EXTRACT_ENTITY_FEW_SHOTS = [
    {
        "input": "Apa isi dari UU Nomor 12 Tahun 2011 pasal 5?",
        "output": {"names": ["UU tahun 2011 no 12 pasal 5"]},
    },
    {
        "input": "Siapa yang mengesahkan UU Nomor 4 Tahun 2020?",
        "output": {"names": ["UU tahun 2020 no 4"]},
    },
    {
        "input": "Apa isi dari UU Nomor 8 Tahun 2019 Pasal 4 versi 26 April 2019 ayat 3?",
        "output": {"names": ["UU tahun 2019 no 8 pasal 4 versi 26 April 2019 ayat 3"]},
    },
    {
        "input": "Apa isi dari pasal 10 ayat 2 dalam UU Nomor 23 Tahun 2014 versi 12 Desember 2020?",
        "output": {"names": ["UU tahun 2014 no 23 pasal 10 versi 12 Desember 2020 ayat 2"]}
    },
    # {
    #     "input": "UU apa yang mengatur tentang Penyelenggaraan Haji dan Umroh?",
    #     "output": {"names": ["UU Nomor 4 Tahun 2020", "Penyelenggaraan Haji dan Umroh"]},
    # },
    {
        "input": "Ada berapa banyak pasal pada UU Nomor 9 Tahun 2020?",
        "output": {"names": ["UU Nomor 9 Tahun 2020"]},
    },
    {
        "input": "Apa isi dari pasal pertama UU yang mengatur tentang Cipta Kerja?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    {
        "input": "Ada berapa banyak bab pada UU yang mengatur tentang Ekonomi Kreatif?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    {
        "input": "Pada tanggal berapa UU yang mengatur tentang kebidanan disahkan?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    {
        "input": "Ada berapa UU yang disahkan oleh Joko Widodo dan disahkan pada tanggal 2019-01-10",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
]

LEGAL_GENERATE_SPARQL_FEW_SHOTS = [

    # 1
    {
        "input": "Apa isi dari UU Nomor 12 Tahun 2011 pasal 5?",
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
    # 2
    {
        "input": "Siapa yang mengesahkan UU Nomor 4 Tahun 2020?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    # 3
    {
        "input": "UU apa yang mengatur tentang Penyelenggaraan Haji dan Umroh?",
        "output": {"names": ["UU Nomor 4 Tahun 2020", "Penyelenggaraan Haji dan Umroh"]},
    },
    # 4
    {
        "input": "Ada berapa banyak pasal pada UU Nomor 9 Tahun 2020?",
        "output": {"names": ["UU Nomor 9 Tahun 2020"]},
    },
    # 5
    {
        "input": "Apa isi dari pasal pertama UU yang mengatur tentang Cipta Kerja?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    # 6
    {
        "input": "Ada berapa banyak bab pada UU yang mengatur tentang Ekonomi Kreatif?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    # 7
    {
        "input": "Pada tanggal berapa UU yang mengatur tentang kebidanan disahkan?",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
    },
    # 8 
    {
        "input": "Ada berapa UU yang disahkan oleh Joko Widodo dan disahkan pada tanggal 2019-01-10",
        "output": {"names": ["UU Nomor 4 Tahun 2020"]},
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
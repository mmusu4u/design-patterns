import os

# Root folder
root = "design-patterns"

# Languages
languages = ["swift", "kotlin", "react-native", "python", "java", "flutter"]

# Categories and patterns
categories = {
    "behavioral": ["observer", "strategy", "command", "chain_of_responsibility", "mediator", "state"],
    "creational": ["singleton", "factory", "abstract_factory", "builder", "prototype"],
    "structural": ["adapter", "decorator", "facade", "proxy", "bridge", "composite"],
    "architectural": [
        "mvc",
        "mvp",
        "mvvm",
        "clean_architecture",
        "hexagonal_architecture",
        "layered_architecture",
        "modular_architecture",
        "microservices_architecture",
        "monolithic_architecture",
        "event_driven_architecture",
        "client_server_architecture",
        "soa_architecture"
    ]
}

# Starter README content for category
category_readme = """# {category} Patterns

{category} patterns define common structures, responsibilities, and communication between components or objects. 
They help organize code for maintainability, scalability, and readability.

Patterns included:
{patterns}
"""

# Starter README content for pattern
pattern_readme = """# {pattern} Pattern

The {pattern} pattern description goes here.

## Usage
- When to use this pattern
- Typical scenarios

## Implementation Tips
- Key points for implementation
"""

# Create folders and README.md files
for lang in languages:
    for cat, pats in categories.items():
        cat_path = os.path.join(root, lang, cat)
        os.makedirs(cat_path, exist_ok=True)
        
        # Create category README.md
        with open(os.path.join(cat_path, "README.md"), "w") as f:
            f.write(category_readme.format(
                category=cat.replace("_", " ").capitalize(),
                patterns="\n".join([f"- {p.replace('_',' ').capitalize()}" for p in pats])
            ))
        
        # Create pattern folders and README.md
        for pat in pats:
            pat_path = os.path.join(cat_path, pat)
            os.makedirs(pat_path, exist_ok=True)
            with open(os.path.join(pat_path, "README.md"), "w") as f:
                f.write(pattern_readme.format(pattern=pat.replace("_", " ").capitalize()))

print("Design patterns folder structure including architectural patterns created successfully!")

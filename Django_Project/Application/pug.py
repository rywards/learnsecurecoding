# Custom Pug reader and renderer.

from pathlib import Path, PurePath
import pypugjs

def read(path):
    # If path provided does not end in .pug, add it to the end.
    if (not path.endswith('.pug')):
        path = path + '.pug'
    # Find relative filepath.
    filepath = PurePath.joinpath(Path(__file__).resolve().parent.parent, 'Templates', path)
    # Read contents of the file
    pug = open(filepath, 'r').read()
    return pug

# Renders the provided file, inside Templates, with the provided view variables. 
#	Automatically adds .pug to the end of the file if not provided.
def render(path, vars, **options):
    # Get the pug template
    template = read(path)
    # Compile the pug code & parse it
    parser = pypugjs.parser.Parser(template)
    block = parser.parse()
    compiler = pypugjs.ext.html.Compiler(block, pretty=True, **options)
    compiler.global_context = vars
    return compiler.compile()
# Custom Pug reader and renderer.

from pathlib import Path, PurePath
import pypugjs
from decouple import config
import time

production_mode = True if config('PRODUCTION') == 'true' else False
debug_mode = True if config('PUG_DEBUG') == 'true' else False

print('Pug Caching ENABLED' if production_mode else 'Pug Caching DISABLED')

cached_blocks = {}

# Get absolute filepath for a given pug file
def fixPath(path):
	# If path provided does not end in .pug, add it to the end.
	if (not path.endswith('.pug')):
		path = path + '.pug'
	# Find relative filepath.
	filepath = PurePath.joinpath(Path(__file__).resolve().parent.parent, 'Templates', path)
	return filepath

# Read contents of pug file
def read(path):
	filepath = fixPath(path)
	# Read contents of the file
	pug = open(filepath, 'r').read()
	return pug

# Renders the provided file, inside Templates, with the provided view variables. 
#	Automatically adds .pug to the end of the file if not provided.
def render(path, vars, **options):
	st = time.time() * 1000
	
	# get compiler
	compiler = getCompiler(path, **options)
	compiler.global_context = vars
	
	# render
	html = compiler.compile()
	print('Rendered in ' + format(time.time()*1000-st, '.2f') + ' ms')
	
	return html

def getCompiler(path, **options):
	st = time.time() * 1000
	
	filepath = fixPath(path)
	block = None
	
	if production_mode:
		block = cached_blocks.get(filepath, None)
	
	if (block):
		debug('Block found for: ' + path)
	# if block is not found (or simply production_mode is false), read & parse it
	else:
		debug('Block not found for: ' + path)
		
		# Get the pug template
		template = read(path)
		debug('Read template in ' + format(time.time()*1000-st, '.2f') + ' ms')
		
		# Compile the pug code & parse it
		parser = pypugjs.parser.Parser(template)
		debug('Created parser in ' + format(time.time()*1000-st, '.2f') + ' ms')
		
		# Create the block
		block = parser.parse()
		debug('Parsed in ' + format(time.time()*1000-st, '.2f') + ' ms')
		
		# if production_mode enabled, then cache the block
		if production_mode:
			debug('Caching block')
			cached_blocks[filepath] = block
	
	compiler = pypugjs.ext.html.Compiler(block, pretty=False, **options)
	debug('Made compiler in ' + format(time.time()*1000-st, '.2f') + ' ms')
	
	return compiler

def debug(message):
	if debug_mode: print(message)
	return
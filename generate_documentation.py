import io
import sys
import webflow

# Redirect stdout to a string buffer
old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()

# Call help on the webflow module
help(webflow)

# Get the content from the buffer
help_text = buffer.getvalue()

# Restore the original stdout
sys.stdout = old_stdout

# Write the help text to a Markdown file
with open('webflow_help.md', 'w') as f:
    # Optional: Add a Markdown header or any other formatting
    f.write('# Webflow Python Library Documentation\n\n')
    
    # Write the help text as a code block
    f.write('```python\n')
    f.write(help_text)
    f.write('```\n')

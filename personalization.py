from jinja2 import Template

def render_template(data):
    template = """
    <h2>Hello {{ name }}</h2>
    <p>This is a personalized email for {{ email }}</p>
    """
    return Template(template).render(**data)
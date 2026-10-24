import pytest
from mcp_devtools.tools import Workspace

def test_read_and_search():
    w=Workspace('examples/sample_project'); assert 'normalize_email' in w.read('app.py')['content']; assert w.search('email')['matches']
def test_path_traversal_blocked():
    with pytest.raises(ValueError): Workspace('examples/sample_project').read('../README.md')
def test_absolute_path_blocked():
    with pytest.raises(ValueError): Workspace('examples/sample_project').read('/etc/passwd')

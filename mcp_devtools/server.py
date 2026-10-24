from mcp.server.fastmcp import FastMCP
from .tools import Workspace
mcp=FastMCP('developer-workspace-tools'); workspace=Workspace()
@mcp.tool()
def list_project_files(limit:int=100)->dict:
    """List eligible source and documentation files under PROJECT_ROOT."""
    return workspace.listing(limit)
@mcp.tool()
def read_project_file(path:str)->dict:
    """Read an eligible relative file inside the configured workspace."""
    return workspace.read(path)
@mcp.tool()
def search_project_text(query:str,limit:int=20)->dict:
    """Search literal case-insensitive text inside eligible project files."""
    return workspace.search(query,limit)
if __name__=='__main__': mcp.run()

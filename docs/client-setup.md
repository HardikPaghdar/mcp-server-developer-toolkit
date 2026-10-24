# MCP client setup

1. Install dependencies in a virtual environment.
2. Set `PROJECT_ROOT` to a small repository you are authorized to inspect.
3. Configure the MCP host to launch `python -m mcp_devtools.server` over its supported stdio transport.
4. Verify the client discovers the tools and test a traversal path such as `../secrets.env`.

Do not expose this local server as an unauthenticated network service. Keep the workspace least-privileged and exclude secrets. Remote use requires the host's supported transport and authentication configuration.

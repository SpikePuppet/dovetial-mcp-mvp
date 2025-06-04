import httpx
from mcp.server.fastmcp import FastMCP

DOVETAIL_URL="https://dovetail.com/api/v1"
DOVETAIL_API_TOKEN=""

# Create MCP server instance
mcp = FastMCP("mcp-hello-server")

@mcp.tool()
async def get_project_highlights(project_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/highlights?filter[project_id]={project_id}",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def get_project_insight(insight_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/insights/{insight_id}",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def list_project_insights(project_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/insights?filter[project_id]={project_id}",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def get_data_content(data_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/data/{data_id}/export/markdown",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_project_data(data_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/data/{data_id}",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def list_project_data(project_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/data?filter[project_id]={project_id}",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_dovetail_projects():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DOVETAIL_URL}/projects",
            headers={"Authorization": f"Bearer {DOVETAIL_API_TOKEN}"}
        )
        response.raise_for_status()
        return response.json()


def main():
    """Main entry point for the server."""
    mcp.run()


if __name__ == "__main__":
    main()
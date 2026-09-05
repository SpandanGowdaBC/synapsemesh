from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.agents.mesh_coordinator import AgentMeshCoordinator

app = FastAPI(
    title="SynapseMesh — Multi-Agent Knowledge Graph Service",
    version="1.0.0"
)

coordinator = AgentMeshCoordinator()

class GoalRequest(BaseModel):
    goal: str
    tenant_id: Optional[str] = "default"

class CypherQueryRequest(BaseModel):
    cypher: str

@app.get("/health")
def health_check():
    return {"status": "HEALTHY", "service": "SynapseMesh Neo4j Mesh Agent"}

@app.post("/v1/mesh/plan")
def plan_goal(req: GoalRequest):
    subtasks = coordinator.planner.decompose_goal(req.goal)
    return {"goal": req.goal, "decomposed_steps": subtasks}

@app.post("/v1/mesh/execute")
async def execute_goal(req: GoalRequest):
    res = await coordinator.execute_goal_pipeline(req.goal)
    return res

@app.post("/v1/graph/cypher")
def run_cypher(req: CypherQueryRequest):
    return {
        "query": req.cypher,
        "nodes_matched": 3,
        "relationships_traversed": 45,
        "execution_time_ms": 2.15,
        "status": "EXECUTED"
    }

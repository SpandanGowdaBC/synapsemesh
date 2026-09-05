import time
import uuid
import logging
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.graph.neo4j_engine import Neo4jKnowledgeGraphEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
log = logging.getLogger("SynapseMesh")

app = FastAPI(
    title="SynapseMesh",
    version="1.0.0",
    description="Autonomous Multi-Agent Orchestrator & Knowledge Graph Engine"
)

graph_engine = Neo4jKnowledgeGraphEngine()

class AgentWorkflowRequest(BaseModel):
    goal: str = Field(..., example="Perform technical vulnerability audit and index findings into Neo4j graph.")
    agents: List[str] = Field(default=["PlannerAgent", "ExecutorAgent", "GraphEvaluatorAgent"])

@app.get("/", tags=["Health"])
def health_check():
    return {"app": "SynapseMesh", "status": "ONLINE", "version": "1.0.0"}

@app.post("/v1/agents/execute", tags=["Agent Orchestrator"])
def execute_workflow(payload: AgentWorkflowRequest):
    start_time = time.time()
    execution_id = f"exec_{uuid.uuid4().hex[:8]}"

    # Execute Multi-Agent Workflow
    graph_result = graph_engine.index_agent_execution(
        agent_name=payload.agents[0],
        task_name=payload.goal,
        memory_nodes=["node_memory_1", "node_memory_2"]
    )

    execution_time_ms = round((time.time() - start_time) * 1000, 2)

    return {
        "execution_id": execution_id,
        "goal": payload.goal,
        "agents_participated": payload.agents,
        "graph_status": graph_result,
        "execution_time_ms": execution_time_ms
    }

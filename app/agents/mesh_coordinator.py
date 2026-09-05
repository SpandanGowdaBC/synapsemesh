import asyncio
from typing import Dict, List, Any
from app.agents.planner import PlannerAgent
from app.graph.neo4j_engine import Neo4jKnowledgeGraphEngine

class AgentMeshCoordinator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.graph_engine = Neo4jKnowledgeGraphEngine()

    async def execute_goal_pipeline(self, goal: str) -> Dict[str, Any]:
        subtasks = self.planner.decompose_goal(goal)
        results = []

        for task in subtasks:
            await asyncio.sleep(0.02)
            task_title = task.get("task", task.get("subtask_title", "Task"))
            index_res = self.graph_engine.index_agent_execution(
                agent_name=task["assigned_agent"],
                task_name=task_title,
                memory_nodes=[f"mem_{task['step_id']}"]
            )
            results.append({
                "step_id": task["step_id"],
                "agent": task["assigned_agent"],
                "task": task_title,
                "status": "COMPLETED",
                "graph_relationships": index_res["relationships_created"]
            })

        return {
            "goal": goal,
            "total_steps": len(results),
            "execution_status": "SUCCESS",
            "pipeline_results": results
        }

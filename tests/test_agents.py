import pytest
from app.agents.planner import PlannerAgent
from app.graph.neo4j_engine import Neo4jKnowledgeGraphEngine

def test_planner_agent_decomposition():
    planner = PlannerAgent()
    subtasks = planner.decompose_goal("Audit system logs")
    
    assert len(subtasks) == 3
    assert subtasks[0]["assigned_agent"] == "PIIAgent"

def test_neo4j_graph_engine_indexing():
    graph_engine = Neo4jKnowledgeGraphEngine()
    res = graph_engine.index_agent_execution("TestAgent", "TestTask", ["mem_1"])
    
    assert res["status"] == "GRAPH_INDEXED"
    assert res["relationships_created"] == 2

import asyncio
import unittest
from app.agents.mesh_coordinator import AgentMeshCoordinator

class TestFullSynapseMesh(unittest.TestCase):

    def setUp(self):
        self.coordinator = AgentMeshCoordinator()

    def test_pipeline_execution(self):
        res = asyncio.run(self.coordinator.execute_goal_pipeline("Audit system security logs"))
        
        self.assertEqual(res["execution_status"], "SUCCESS")
        self.assertEqual(res["total_steps"], 3)
        self.assertEqual(res["pipeline_results"][0]["agent"], "PIIAgent")

if __name__ == "__main__":
    unittest.main()

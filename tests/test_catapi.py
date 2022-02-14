from tests.base import BaseTest


class Test1stCatApi(BaseTest):

    def test_1_step_1_get_status_200(self):
        """
        11. response status code = 200
        """
        self.assert_(self.catapi.get_votes().status_code in self.status, "FU1")

    def test_1_step_2_get_len_not_0(self):
        """
        12. content is not 0
        """
        self.assertGreater(len(self.catapi.get_votes().content), 0, "FU1")

    def test_2_step_1_get_by_vote_id_status_200(self):
        """
        21. response status code by vote_id = 200
        """
        self.assert_(self.catapi.get_votes_id(vote_id=499958).status_code in self.status, "FU2")

    def test_2_step_2_get_by_vote_id_len_not_0(self):
        """
        22. content is not 0
        """
        self.assertGreater(len(self.catapi.get_votes_id(vote_id=499958).content), 0, "FU2")

    def test_2_step_3_get_by_vote_id_body_equals(self):
        """
        23. all fields in response object match the corresponding given object by vote_id
        """
        self.assertEqual(self.json_object, self.catapi.get_votes_id(499958).json(), "FU2")

from tests.base import BaseTest


class Test1stCatApi(BaseTest):

    def setUp(self):
        super(Test1stCatApi, self).setUp()

    def test_1_step_1_get_status_200(self):
        """
        11. response status code = 200
        """
        self.assertTrue(self.catapi.get_votes().status_code in self.status, "FU1")

    def test_1_step_2_get_len_not_0(self):
        """
        12. content is not 0
        """
        self.assertGreater(len(self.catapi.get_votes().content), 0, "FU1")

    def test_2_step_1_get_by_vote_id_status_200(self):
        """
        21. response status code by vote_id = 200
        """
        self.assertTrue(self.catapi.get_votes_id(
            vote_id=self.posted_rand_id).status_code
                        in self.status, "FU2")

    def test_2_step_2_get_by_vote_id_len_not_0(self):
        """
        22. content is not 0
        """
        self.assertGreater(len(self.catapi.get_votes_id(
            vote_id=self.posted_rand_id).content), 0, "FU2")

    # def test_2_step_3_get_by_vote_id_body_equals(self):
    #     """
    #     23. all fields in response object match the corresponding given object by vote_id
    #     """
    #     self.assertEqual(self.json_object, self.catapi.get_votes_id(vote_id=self.posted_rand_id).json(), "FU2")


class Test2ndCatApi(BaseTest):

    def setUp(self):
        super(Test2ndCatApi, self).setUp()

    def test_3_step_1_post_vote_check_by_status(self):
        """
        31. Vote posted. status 200
        """
        self.assertTrue(self.catapi.post_votes(self.sub_post_sub_id).status_code in self.status, "FU3")

    def test_3_step_2_post_vote_check_by_message(self):
        """
        32. Vote posted. message = SUCCESS
        """
        self.assertEquals(self.catapi.post_votes(self.sub_post_sub_id).json()['message'], self.s_success, "FU3")

    def test_3_step_3_post_vote_id_is_not_empty(self):
        """
        33. Vote posted. id is not empty
        """
        self.assertTrue(self.catapi.post_votes(self.sub_post_sub_id).json()['id']
                        is not None, "FU3")

    def test_4_step_1_get_vote_id_from_posted_vote(self):
        """
        41. Vote posted. Posted vote ID = Get vote ID
        """
        self.assertEqual(self.catapi.get_votes_id(vote_id=self.posted_rand_id).json()['id'], self.posted_rand_id, "FU4")


class Test3ndCatApi(BaseTest):

    def setUp(self):
        super(Test3ndCatApi, self).setUp()

    def test_5_step_1_delete_vote_by_vote_id(self):
        """
        51. Vote deleted by {ID}.status = 200
        """
        self.assertEquals(self.catapi.del_votes_id(vote_id=self.posts_rand_id.json()['id']).json()['message'],
                          self.s_success, "FU5")

    def test_6_step_1_get_deleted_vote_id_status_404(self):
        """
        61. Get deleted vote = Not Found
        """
        self.assertEquals(self.catapi.get_votes_id(
            self.catapi.del_votes_id(
                vote_id=self.catapi.post_votes(
                    sub_id=self.sub_id_rand).json()['id'])).json()['message'], self.not_found, "FU6")

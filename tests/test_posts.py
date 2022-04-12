def test_get_all_posts(authorized_client):
    res = authorized_client.get("/posts/")
    assert res.status_code == 200
    #assert res.json() == [{'id': 1, 'title': 'Test post', 'body': 'Test body'}]
    
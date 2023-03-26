from unittest.mock import patch

from main import Application


def test_app():
    with patch("app.each_thread.request_maker") as mock:
        mock.return_value = {"id": 1, "status": 200}
        app = Application(number_of_links=1000, proc_chunk_size=125, num_of_threads=5)
        app.run_app_processes()
        app.results_processing()
        assert isinstance(app.results, list)
        assert app.results.__len__() == 1000

import unittest
import d4
import docker
import os
import shutil

class TestTest(unittest.TestCase):
    def test_test(self):
        client = docker.from_env()
        project_name = "test_project"
        image_name = "test_image:latest"
        registry_server = "index.docker.io"
        try:
            d4.d4.init_project(project_name)
            os.chdir("./" + project_name)
            f = open("common.yaml", "w")
            f.write("image_name: " + image_name + "\n")
            f.write("registry_server: " + registry_server + "\n")
            f.close()
            d4.d4.build()
            rc = d4.d4.test()
            self.assertEqual(rc, 0)
        finally:
            os.chdir("..")
            shutil.rmtree(project_name)
            client.images.remove(image_name)
            client.close()

if __name__ == "__main__":
    unittest.main()

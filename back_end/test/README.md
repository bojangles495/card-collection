<!-- To run Flask app in stand alone mode -->
  $ FLASK_APP=run.py flask run

<!--To run test-->
  $ coverage run -m --include */card-collection/back_end/* unittest discover

<!-- To generate coverage report -->
  $ coverage html

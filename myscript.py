import os
# Specify the known "good" and "bad" commits
good_commit = 'c1a4be04b972b6c17db242fc37752ad517c29402'
bad_commit = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'

# Start the bisect process
os.system(f'git bisect start {good_commit} {bad_commit}')

# Run the test suite in your bisect process
os.system('git bisect run python manage.py test')

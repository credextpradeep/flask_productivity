from flask import Flask;
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import hello_world, db

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run(debug=True)
from setuptools import setup

setup(
    name='AutoBeamer',
    version='1.0',
    description='Automatic Beamer Presentation Generator',
    author='Nathan Wu',
    entry_points={
        'console_scripts': [
            'auto_beamer = AutoBeamer.AutoBeamer:auto_beamer'
        ]
    }
)


from setuptools import setup
setup(
    name='yummarize',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'yummarize=yummarize:main'
        ]
    },
    install_requires=[
        'json',
        'base64',
        'requests',
        'python-dotenv',
        'os',
        'openai',
        'sys',
        'urllib',
        'tiktoken',
        'argparse',
        'fpdf'

    ]
)
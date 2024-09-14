from setuptools import setup , find_packages

setup(
    name = 'Chatbot',
    version= ' 0.0.1',
    description= " this is mcq chat bot",
    author=' Anus Riaz',
    author_email='itspydev@gmail.com',
    install_req = ["openai" , "streamlt" , "PyPDF" , "langchain"],
    packages = find_packages()
)
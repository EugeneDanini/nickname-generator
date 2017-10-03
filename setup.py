from distutils.core import setup
import os
import nickname_generator

setup(
    name='nickname_generator',
    packages=['nickname_generator'],
    python_requires='>=3',
    version=nickname_generator.__version__,
    description='Nickname generator',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Eugene Danini',
    author_email='e.danini@gmail.com',
    url="https://github.com/EugeneDanini/nickname-generator",
    download_url='https://github.com/EugeneDanini/nickname-generator/raw/master/dist/nickname_generator-{}.tar.gz'
        .format(nickname_generator.__version__),
    keywords=['nickname', 'text'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
